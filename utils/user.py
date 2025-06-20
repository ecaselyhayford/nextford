import csv
import os
from models.db import collection


class User:
    def __init__(self, age, gender, income, expenses, id=None):
        self.id = id  # MongoDB _id
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses  # dictionary of categories and amounts

    def to_dict(self):
        row = {
            "id": str(self.id),  # Include Mongo _id in CSV
            "age": self.age,
            "gender": self.gender,
            "income": self.income
        }
        row.update(self.expenses or {})
        return row

    @staticmethod
    def write_to_csv(users, filename="user_data.csv"):
        if not users:
            return

        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", filename)
        file_exists = os.path.isfile(file_path)

        fieldnames = set()
        for user in users:
            fieldnames.update(user.to_dict().keys())
        fieldnames = sorted(fieldnames)

        with open(file_path, mode="a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_exists or os.path.getsize(file_path) == 0:
                writer.writeheader()

            for user in users:
                writer.writerow(user.to_dict())
