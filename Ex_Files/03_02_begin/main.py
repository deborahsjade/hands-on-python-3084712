import csv
from datetime import datetime
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")
        laureate_date = datetime.strptime(laureate["year"], "%Y")
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        died_date = datetime.strptime(laureate["died"], "%Y-%m-%d")
        now_date = datetime.now()
        print("age when awarded prize:", laureate_date.year - born_date.year)
        print("years since he was born:", now_date.year - born_date.year)
        print("years since he won:", now_date.year - laureate_date.year)
        print("age when he died:", died_date.year - born_date.year)
        break
