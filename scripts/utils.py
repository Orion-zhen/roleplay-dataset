import os
import sys
import json
import email
import imaplib
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from tqdm import tqdm
from email.message import Message
from typing import List, Dict, Union, Optional


def list_files(root_dir="data/") -> List[str]:
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files
        if file.endswith(".json")
    ]


def update_index(file_paths: List[str], index_file="index.parquet"):
    table = pa.table({"file_paths": file_paths})
    pq.write_table(table, index_file)


def read_index(index_file="index.parquet") -> List[str]:
    table = pq.read_table(index_file)
    file_paths = table.column("file_paths").to_pylist()
    return file_paths


def is_subset(indexed_files: List[str], all_files: List[str]) -> bool:
    if indexed_files == []:
        return True
    # 必须为真子集
    if len(all_files) == len(indexed_files):
        return False
    indexed_set = set(indexed_files)
    all_set = set(all_files)
    return indexed_set.issubset(all_set)


def is_valid_file_or_bytes(file_or_bytes: Union[bytes, str]) -> bool:
    if isinstance(file_or_bytes, bytes):
        try:
            content = json.loads(file_or_bytes)
        except Exception as e:
            print(e)
            return False
    elif isinstance(file_or_bytes, str) and file_or_bytes.endswith(".json"):
        try:
            with open(file_or_bytes, "r", encoding="utf-8") as f:
                content = json.load(f)
        except Exception as e:
            print(e)
            return False
    else:
        return False

    return True


def is_sharegpt_format(contents: List[Dict[str, Union[str, List[Dict[str, str]]]]]):
    if not isinstance(contents, list):
        return False
    for content in contents:
        if not isinstance(content, dict):
            return False
        if "system" not in content.keys():
            return False
        if "conversations" not in content.keys():
            return False
        conversations = content.get("conversations")
        if not isinstance(conversations, list):
            return False
        for conversation in conversations:
            if not isinstance(conversation, dict):
                return False
            if "from" not in conversation.keys() or "value" not in conversation.keys():
                return False

    return True


def is_valid(file_path: str) -> bool:
    if not is_valid_file_or_bytes(file_path):
        return False
    with open(file_path, "r", encoding="utf-8") as f:
        content = json.load(f)
    if not is_sharegpt_format(content):
        return False

    return True


def save_attachment(part: Message, local_dir="data/") -> None:
    filename = part.get_filename()
    if filename and filename.endswith(".json"):
        file_content = part.get_payload(decode=True)
        if is_valid_file_or_bytes(file_content):
            with open(os.path.join(local_dir, filename), "wb") as f:
                f.write(file_content)
                print(f"Saved: {filename}")
        else:
            print(f"Invalid JSON format in attachment: {filename}")


def fetch_emails(
    email_addr: str,
    email_pwd: str,
    server="imap.gmail.com",
    criteria="UNSEEN",
    folder="dataset",
) -> None:
    mail = imaplib.IMAP4_SSL(server)
    mail.login(email_addr, email_pwd)
    mail.select(folder)

    status, messages = mail.search(None, criteria)
    assert status == "OK", "Status must be OK!"
    email_ids = messages[0].split()

    print(f"* Fetched {len(email_ids)} emails")

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        assert status == "OK", "Status must be OK!"

        msg = email.message_from_bytes(msg_data[0][1])

        print("\n================================")
        print(f"Date: {msg.get('Date')}")

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            save_attachment(part, "data/")

        mail.store(email_id, "+FLAGS", "\\Seen")

        print("================================\n")

    mail.logout()


def gather_files(root_dir="data/") -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
    all_files = list_files(root_dir)
    gathered_list = []
    for file in tqdm(all_files):
        with open(file, "r", encoding="utf-8") as f:
            content = json.load(f)
        assert isinstance(content, list)
        gathered_list += content
    return gathered_list


def to_parquet(
    formatted_contents: List[Dict[str, Union[str, Dict[str, str]]]],
    file_name="dataset.parquet",
):
    df = pd.DataFrame(formatted_contents)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_name)
    print(f"Parquet file '{file_name}' has been generated.")
