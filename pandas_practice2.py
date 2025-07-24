
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

  # ترتیب سن صعودی برای جوانگرایی
  sort_age_people = together_condition.sort_values(by= 'age')

  return sort_age_people[['name', 'last_name', 'age', 'income']]

# پرینت افراد واجد شرایط وام با در نظر گرفتن اولویت سن از کم به زیاد
print(conditions())


