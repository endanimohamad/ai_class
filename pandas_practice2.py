
import json
import pandas as pd

# with open("D:\\data_people.json", "w", encoding="utf-8") as file:
#   json.dump(data, file, ensure_ascii= False, indent=3)

# خواندن فایل جیسون
def read_json():
  with open("D:\\data_people.json", "r", encoding="utf-8") as file:
    content = json.load(file)
  return content

# ایجاد دیتا فریم
fade_json = read_json()
df = pd.DataFrame(fade_json)

# نوشتن یک فایل تکست توسط دیتا فریم ساخته شده از فایل جیسون
def write_txt():
  with open("D:\\text.txt", "w", encoding="utf-8") as text:
    write = text.write(df.to_string())
  return write
write_txt()

# ساختن شروط پاندایی
def conditions():
  condition_age_income = (df['age'] >= 22) & (df['income'] >= 22000000)

  condition_home = df['has_house'] == 'ندارد'

  condition_gender = df['gender'] == 'مرد'

  together_condition = df[condition_age_income & condition_gender & condition_home]

  sort_age_people = together_condition.sort_values(by= 'age')

  return sort_age_people[['name', 'last_name', 'age', 'income']]

print(f' \n                                                                                      :افراد واجد شرایط دریافت وام{conditions()}')


def calculation():
  age_mean = df['age'].mean()
  print(f' : میانگین سنی افراد متقاضی وام: {age_mean}')
  income_mean = df['income'].mean()
  print(f' : میانگین درامد افراد متقاضی وام: {income_mean}')
  print("\n")

  age_median = df['age'].median()
  print(f' : میانه(تقریبا متوسط) سنی افراد متقاضی وام: {age_median}')
  income_median = df['income'].median()
  print(f' : میانه(تقریبا متوسط) درامدی افراد متقاضی وام: {income_median}')
  print("\n")
  age_mode = df['age'].mode().iloc[0]
  print(f' نمای (بیشترین) سن پرتکرا افراد متقاضی وام: {age_mode}')

  name_mode = df['name'].mode().iloc[0]
  print(f' : نمای (بیشترین) اسم پرتکرا افراد متقاضی وام: {name_mode}')

  car_mode = df['car'].mode().iloc[0]
  print(f'  نمای (بیشترین) ماشین پرتکرا افراد متقاضی وام: {car_mode}')

  education_mode = df['education'].mode().iloc[0]
  print(f'  نمای (بیشترین) مدرک تحصیلی پرتکرا افراد متقاضی وام: {education_mode}')

calculation()


