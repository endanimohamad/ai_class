import json
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "datadata.txt")

with open(desktop_path, "r", encoding="utf-8") as file:
    data = json.load(file)

if isinstance(data, dict):
    print(" کلیدهای اصلی:")
    for key in data:
        print("-", key)
else:
    msg = f" فایل نوعش دیکشنری نیست: {type(data)}"
    print(msg)
    with open("key.txt", "w", encoding="utf-8") as f:
        f.write(msg)