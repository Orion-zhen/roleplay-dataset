from scripts.utils import is_valid_jsonl, list_jsonl_files, is_subset, read_index
from tqdm import tqdm
import sys

if __name__ == "__main__":
    file_paths = list_jsonl_files("data/")
    print(f"File paths (first 10): {file_paths[:10]}")
    indexed_files = read_index("index.parquet")
    print(f"Indexed files (first 10): {indexed_files[:10]}")
    if not is_subset(indexed_files, file_paths):
        print("No increasement on data!")
        sys.exit(1)

    for file in tqdm(file_paths):
        if not is_valid_jsonl(file):
            print("Invalid file!")
            sys.exit(1)
    print("File valid!")
