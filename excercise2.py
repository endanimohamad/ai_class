
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



def ali_name():
    counter_ali = 0
    for i in df['name']:
        if i == "علی":
            counter_ali += 1
    return counter_ali



def income_median_equality():
    counter_median = 0
    median_income = df['income'].median()
    for i in df['income']:
        if i == median_income:
            counter_median += 1
    return counter_median



def age_mode_count():
    ages_count = df['age'].value_counts()
    max_age_count = ages_count.max()
    age_repeat = ages_count[ages_count == max_age_count]
    return age_repeat



if __name__ == "__main__":
    show_json_file()
    df = create_dataframe()
    counter_ali = ali_name()
    counter_income = income_median_equality()
    age_repeat = age_mode_count()
    print(f' اسم علی {counter_ali} بار تکرار شده است')
    print(f'تعداد {counter_income} درامد دقیقا برابر میانه است')
    print("سن‌هایی که بیشترین تکرار را دارند:")
    for age,count in age_repeat.items():
        print(f"سن{age} به تعداد {count} بار تکرار شده است. ")