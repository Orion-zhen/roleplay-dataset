from utils import list_files, is_subset, read_index, is_valid
from tqdm import tqdm
import sys


def validate(dir="data/", indexer="index.parquet"):
    all_file_paths = list_files(dir)
    print(f"All file paths (first 10): {all_file_paths[:10]}")
    indexed_files = read_index(indexer)
    print(f"Indexed files (first 10): {indexed_files[:10]}")
    if not is_subset(indexed_files, all_file_paths):
        print("No increasement on data!")
        sys.exit(1)

    for file_path in tqdm(all_file_paths):
        if not is_valid(file_path):
            print(f"{file_path} is invalid!")
            sys.exit(1)

    print("All files are valid!")


if __name__ == "__main__":
    validate()
