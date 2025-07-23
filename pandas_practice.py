import os
import ast
import pandas as pd

def read_py_file():
    dpath = os.path.join("D:\\", "bank_customer.txt")
    with open(dpath, 'r', encoding="utf-8") as file:
        content = file.read()
        dataset = ast.literal_eval(content)
        df = pd.DataFrame(dataset)
    return df

df = read_py_file()
# اعمال شرط با پاندا
eligible = df[
    (df['age'] >= 25) &
    (df['age'] <= 60) &
    (df['work_experience'] >= 2)
]

# نمایش واجدین شرایط
print("افراد واجد شرایط دریافت وام:\n")
print(eligible[['name', 'last_name']].to_string())
