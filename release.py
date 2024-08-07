from utils import list_jsonl_files, gen_format, to_parquet


if __name__ == '__main__':
    jsonl_files = list_jsonl_files("data/")
    formatted_contents = []
    for file in jsonl_files:
        with open(file) as f:
            data_list = f.readlines()
        formatted_contents.append(gen_format(data_list))
    to_parquet(formatted_contents, "dataset.parquet")