import os
from datetime import date

os.makedirs("diary", exist_ok=True)
d = str(date.today())
print(d)
folder = os.path.join("diary", d)
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, "日記.txt")
f = open(file_path, "a", encoding="utf-8")
f.write("Hello World\n")
f.close()
