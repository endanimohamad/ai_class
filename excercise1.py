
import json
import os
import pandas as pd

def show_json_file():
    dpath = os.path.join("D:\\", "data_people.json")
    with open(dpath, "r", encoding="utf-8") as file:
        load_json = json.load(file)
        return load_json

def create_dataframe():
    data_frame = pd.DataFrame(show_json_file())
    return data_frame



def calculations():
    age_mean = df['age'].mean()
    income_mean = df['income'].mean()
    age_mode = df['age'].mode().tolist()
    income_mode = df['income'].mode().tolist()
    names = df[df['age'].isin(age_mode)][['name', 'last_name', 'age']].values.tolist()
    return age_mean, income_mean, age_mode, income_mode, names


if __name__ == "__main__":
    show_json_file()
    df = create_dataframe()
    age_mean, income_mean, age_mode, income_mode, names = calculations()
    print(f"\nمیانگین سن: {age_mean}")
    print(f"میانگین درآمد: {income_mean}")
    print(f"پرتکرارترین سن‌ها: {age_mode}")
    print(f"پرتکرارترین درآمدها: {income_mode}")
    print("\nافرادی با سن پرتکرار:")
    for person in names:
        print(person)
