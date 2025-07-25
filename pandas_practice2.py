
import json
import os
import pandas as pd

# with open("D:\\data_people.json", "w", encoding="utf-8") as file:
#   json.dump(data, file, ensure_ascii= False, indent=3)

# خواندن فایل جیسون
def read_json():
  dpath = os.path.join("D:\\", "data_people.json")
  with open(dpath, "r", encoding="utf-8") as file:
    content = json.load(file)
  return content

# ایجاد دیتا فریم
def load_dataframe():
  load_json = read_json()
  df = pd.DataFrame(load_json)
  return df

# نوشتن یک فایل تکست توسط دیتا فریم ساخته شده از فایل جیسون
def write_txt(df):
  with open("D:\\text.txt", "w", encoding="utf-8") as text:
    write = text.write(df.to_string())
  return write

# بخش سوم – فیلتر کنین، برای اینکه مدل شرطی کار کنین :
# حالا یه فیلتر بنویس که فقط آدم‌هایی رو نشون بده که:
# سنشون کمتر از میانگین سِنه
# و درآمدشون بیشتر از ۶۰۰ هست
# فقط اسم و درآمد اون افراد رو چاپ کن.
# ساختن شروط پاندایی
def conditions(df):
  condition_age_income = (df['age'] >= 22) & (df['income'] >= 22000000)

  condition_home = df['has_house'] == 'ندارد'

  condition_gender = df['gender'] == 'مرد'

  filter_condition = df[condition_age_income & condition_gender & condition_home]

  sort_age_people = filter_condition.sort_values(by= 'age')

  return sort_age_people[['name', 'last_name', 'age', 'income']]

# بخش اول – گرم کردن:
# محاسبه های اماری با پاندا
def calculation(df):
 # میانگین سن‌ها
  age_mean = df['age'].mean()
  print(f' : میانگین سنی افراد متقاضی وام: {age_mean}')
  # میانگین درآمدها
  income_mean = df['income'].mean()
  print(f' : میانگین درامد افراد متقاضی وام: {income_mean}')
  print("\n")
  # میانه‌شون چیه؟ ببین وسط عددها کدوم عدد وایساده؟
  age_median = df['age'].median()
  print(f' : میانه(تقریبا متوسط) سنی افراد متقاضی وام: {age_median}')
  income_median = df['income'].median()
  print(f' : میانه(تقریبا متوسط) درامدی افراد متقاضی وام: {income_median}')
  print("\n")
  # کدوم مقدار توی income و age بیشتر از همه تکرار شده؟ اسمش چیه؟
  age_mode = df['age'].mode()
  print(f' نمای (بیشترین) سن پرتکرار افراد متقاضی وام: {age_mode}')

  name_mode = df['name'].mode()
  print(f' : نمای (بیشترین) اسم پرتکرار افراد متقاضی وام: {name_mode}')

  car_mode = df['car'].mode()
  print(f'  نمای (بیشترین) ماشین پرتکرار افراد متقاضی وام: {car_mode}')

  education_mode = df['education'].mode()
  print(f'  نمای (بیشترین) مدرک تحصیلی پرتکرار افراد متقاضی وام: {education_mode}')

  return income_median

# بخش دوم – یه کم جدی‌تر:
def count_values(df, counter_ali = 0, counter_income = 0, counter_age = 0):
  income_median = calculation(df)
  # چند نفر اسمشون "Ali" هست؟
  for ali in df['name']:
    if ali == 'علی':
      counter_ali += 1
  # چند نفر درآمدشون دقیقاً همون مقداریه که میانه گفت؟
  for count_income in df['income']:
    if count_income == income_median:
      counter_income += 1
  # سن کدوم بچه بیشتر از بقیه تکرار شده؟ چند بار تکرار شده؟
  for count_age in df['age']:
  #  چون از قبل میدانیم سن پرتکرار 22 است پس مینویسیم
    if count_age == 22:
      counter_age += 1
  return counter_ali, counter_income, counter_age

if __name__ == "__main__":
  df = load_dataframe()
  counter_ali, counter_income, counter_age = count_values(df)
  write_txt(df)
  print(f'افراد واجد شرایط دریافت وام \n {conditions(df)}')
  print("\n")
  print(f'تعداد اسم علی :{counter_ali}')
  print("\n")
  print(f'تعداد درامد برابر با میانه:{counter_income}')
  print("\n")
  print(f'تعداد سن پر تکرا 22 برابر است با {counter_age} بار')
  calculation(df)



