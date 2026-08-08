import os

# dirName= "python_lab"
# try:
#     os.makedirs(dirName, exist_ok=False)
#     print(dirName, "資料夾建立成功")
# except FileExistsError:
#     print(dirName,"資料夾已存在，不重複建立")
# os.chdir("python_lab")
# print("現在的位置",os.getcwd())
#
# isExist = os.path.exists("os_test")
# if isExist == False:
#     os.mkdir("os_test")
# print(os.listdir("."))

# fin=open("poem.txt",encoding="utf-8")
# lines=fin.readlines()
# for line in lines:
#     print(line)
# fin.close()
# s='Python'
# fin=open("poem.txt","wt")
# fin.write(s)
# fin.close()

s='123\n456'
try:
    with open("poem.txt",'wt',encoding="utf-8") as fout:
        fout.write(s)
except:
    print("error")