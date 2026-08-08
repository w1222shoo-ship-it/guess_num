import os

os.makedirs("test2", exist_ok=True)
os.chdir("test2")

for i in range(1,19):
    folder = ''
    if i < 10:
        folder = '0'+str(i)
    else:
        folder = str(i)
    os.makedirs("week"+folder ,exist_ok=True)
    