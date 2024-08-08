from utils import list_jsonl_files, update_index


if __name__ == "__main__":
    file_paths = list_jsonl_files("data/")
    update_index(file_paths, "index.parquet")
    print(f"reindexed to {file_paths}")
