
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



def filter_age_income():
    mean_age = df['age'].mean()
    filtered = df[(df['age'] < mean_age) & (df['income'] > 22000000)]
    two_filter = filtered[['name', 'income']]
    return two_filter




if __name__ == "__main__":
    show_json_file()
    df = create_dataframe()
    two_filter = filter_age_income()
    print("اسم و درامد افرادی که سنشان کم تر از میانگین و درامدشان بالای 22 میلیون تومان است")
    print(two_filter)