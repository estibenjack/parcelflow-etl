import csv


def extract_csv(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        raw_data = list(reader)

    return raw_data