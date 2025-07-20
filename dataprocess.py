import json
import os
#تست فایل
def read_json_file():
    try:
        desktop_path = os.path.join("D:\\", "home-page.txt")
        with open(desktop_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("❌ فایل یافت نشد. لطفاً مطمئن شوید فایل 'home-page.txt' روی درایو D وجود دارد.")
    except json.JSONDecodeError:
        print("❌ خطا در خواندن فایل JSON. ممکن است فایل خراب یا ناصحیح باشد.")
    except Exception as e:
        print(f"❌ خطای ناشناخته: {e}")
data = read_json_file()
# برای چاپ کل جیسون میشه این خط پایین رو هشتگشو برداشت
# print(data)

print("***تحلیل ساختار کلی فایل***")
print("---------------"*10)

#مشخصات فایل
def structure(data):
    print(":نوع داده اصلی", "\t", type(data).__name__)
    if isinstance(data, dict) or isinstance(data, list):
        print(":تعداد آیتم های سطح اول","\t" , len(data))
    else:
        print("لیست و یا دیکشنری موجود نیست")
structure(data)

def max_depth(data, depth = 1):
    if isinstance(data, dict):
        max_dict_depth = depth
        for value in data.values():
            child_depth = max_depth(value, depth+1)
            max_dict_depth = max(max_dict_depth, child_depth)
        return max_dict_depth
    elif isinstance(data, list):
        max_list_depth = depth
        for item in data:
            child_depth = max_depth(item, depth+1)
            max_list_depth = max(max_list_depth, child_depth)
        return max_list_depth

    return depth
print(":بیشترین عمق تو در تویی","\t",max_depth(data))
max_depth(data)



#اطلاعات به دست امده اماری عددی

print("داده های اماری:")
print("============="*10)

from collections import defaultdict

def count_data_types(data, counter=None):
    if counter is None:
        counter = defaultdict(int)

    if isinstance(data, dict):
        counter['dict'] += 1
        for value in data.values():
            count_data_types(value, counter)

    elif isinstance(data, list):
        counter['list'] += 1
        for item in data:
            count_data_types(item, counter)

    elif isinstance(data, str):
        counter['str'] += 1

    elif isinstance(data, int):
        counter['int'] += 1

    elif isinstance(data, float):
        counter['float'] += 1

    elif data is None:
        counter['NoneType'] += 1

    elif isinstance(data, bool):
        counter['bool'] += 1

    else:
        counter[str(type(data))] += 1  # برای داده‌های ناشناخته

    return counter

type_counts = count_data_types(data)

print("📊 شمارش انواع داده‌ها در فایل JSON:")
for dtype, count in type_counts.items():
    print(f"  - {dtype}: {count}")

print("==========="*15)

import  statistics

def extract_numbers(data, numbers=None):
    if numbers is None:
        numbers = []

    if isinstance(data, dict):
        for value in data.values():
            extract_numbers(value, numbers)
    elif isinstance(data, list):
        for item in data:
            extract_numbers(item, numbers)
    elif isinstance(data, (int, float)):
        numbers.append(data)

    return numbers
# استخراج مقادیر عددی
numbers = extract_numbers(data)

if numbers:
    print("🔢 اطلاعات عددی:")
    print(f"  - تعداد مقادیر عددی: {len(numbers)}")
    print(f"  - کمینه: {min(numbers)}")
    print(f"  - بیشینه: {max(numbers)}")
    print(f"  - میانگین: {sum(numbers) / len(numbers):.2f}")
    print(f"  - میانه: {statistics.median(numbers)}")
else:
    print("🔢 هیچ عددی در داده‌ها پیدا نشد.")
print("============"*15)

# مقادیر متنی
def analyze_text_data(data, text_list=None):
    if text_list is None:
        text_list = []

    if isinstance(data, dict):
        for value in data.values():
            analyze_text_data(value, text_list)
    elif isinstance(data, list):
        for item in data:
            analyze_text_data(item, text_list)
    elif isinstance(data, str):
        text_list.append(data)

    return text_list
text_data = analyze_text_data(data)  

total_strings = len(text_data)
unique_strings = len(set(text_data))

print("🔤 تحلیل رشته‌ها:")
print(f"  - تعداد کل رشته‌ها: {total_strings}")
print(f"  - تعداد مقادیر یکتای متنی: {unique_strings}")

print("============="*15)

from collections import defaultdict

def count_keys(data, counter=None):
    if counter is None:
        counter = defaultdict(int)

    if isinstance(data, dict):
        for key, value in data.items():
            counter[key] += 1
            count_keys(value, counter)
    elif isinstance(data, list):
        for item in data:
            count_keys(item, counter)

    return counter
keys_counter = count_keys(data)

# نمایش همه کلیدها
print("🔑 لیست تمام کلیدها:")
for key, count in keys_counter.items():
    print(f"- {key}: {count} بار")

# پیدا کردن بیشترین کلید تکراری
if keys_counter:
    max_key = max(keys_counter.items(), key=lambda x: x[1])
    print(f"\n🏆 بیشترین کلید تکرارشونده: «{max_key[0]}» با {max_key[1]} بار تکرار")
else:
    print("هیچ کلیدی پیدا نشد.")

