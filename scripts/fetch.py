from utils import fetch_emails
import os


def fetch(dir="data/"):
    if not os.path.exists(dir):
        os.makedirs(dir)
    email_addr = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    fetch_emails(email_addr, password)
    

if __name__ == "__main__":
    fetch()