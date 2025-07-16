import json
import os


def find_names(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "name":
                print(value)
            else:
                find_names(value)
    elif isinstance(data, list):
        for item in data:
            find_names(item)

open_file = os.path.join(os.path.expanduser("~"), "Desktop", "home-page.txt")

try:
    with open(open_file, "r", encoding="utf-8") as file:
        read = json.load(file)
    print("اسم کسانی که پست گذاشته اند:")
    find_names(read)

except FileNotFoundError:
    print("❌ فایل یافت نشد. لطفاً مطمئن شوید فایل 'home-page.txt' روی دسکتاپ وجود دارد.")

except json.JSONDecodeError:
    print("❌ خطا در خواندن فایل JSON. ممکن است فایل خراب یا ناصحیح باشد.")

except Exception as e:
    print(f"❌ خطای ناشناخته: {e}")