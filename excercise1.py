
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


# میانگین سن‌ها و درآمدها چقدره؟ (یعنی به طور میانگین، بچه‌ها چند ساله‌ان و چقدر می‌گیرن؟)
# میانه‌شون چیه؟ ببین وسط عددها کدوم عدد وایساده؟
# کدوم مقدار توی income و age بیشتر از همه تکرار شده؟ اسمش چیه؟ (یعنی نماش!)
def calculations():
    age_mean = df['age'].mean()
    income_mean = df['income'].mean()
    mode_age = df['age'].mode()
    mode_income = df['income'].mode()
    print(mode_income)
    list_mode_age = list(mode_age)
    names = df[df['age'].isin(list_mode_age)][['name', 'last_name', 'age']].values.tolist()
    print(f'اسم افرادی که شباهت سنی دارند:\n')
    print(names)


if __name__ == "__main__":
    show_json_file()
    df = create_dataframe()
    calculations()