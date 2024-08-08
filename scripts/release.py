from utils import gather_files, to_parquet


def release(dir="data/", release_file="dataset.parquet"):
    gathered_list = gather_files(dir)
    to_parquet(gathered_list, release_file)


if __name__ == "__main__":
    release()
