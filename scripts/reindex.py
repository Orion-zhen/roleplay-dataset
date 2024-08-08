from utils import list_files, update_index


def reindex(dir="data/", indexer="index.parquet"):
    file_paths = list_files("data/")
    update_index(file_paths, "index.parquet")
    print(f"reindexed to {file_paths}")


if __name__ == "__main__":
    reindex()
