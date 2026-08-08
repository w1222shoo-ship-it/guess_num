import os

# os.makedirs("test4_fake", exist_ok=True)
# os.chdir("test4_fake")
#
# for file in os.listdir("."):
#     os.remove(file)
#
# fake_files = ["report.pdf", "meme.jpg", "photo.png", "song.mp3",
#               "notes.txt", "installer.exe", "video.mp4", "data.csv","test.zip"]
fileName = []
keyword = input("請輸入要查詢的檔名關鍵字:")

def selectFolder(folder,keyword):
    if folder.find(".") != -1:
        if (folder.split('.')[0].find(keyword) != -1):
            fileName.append(os.getcwd()+"\\"+folder)
    else:
        try:
            os.chdir(folder)
        except:
            os.chdir("../"+folder)
        for file in os.listdir("."):
            if file.find(".") != -1:
                if(file.split('.')[0].find(keyword) != -1):
                    fileName.append(os.getcwd()+"\\"+file)
            else:
                return selectFolder(file, keyword)

os.chdir('.')
source = os.getcwd()
for file in os.listdir("."):
    if file.find(".") != -1:
        if (file.split('.')[0].find(keyword) != -1):
            fileName.append(os.getcwd()+"\\"+file)
    else:
        os.chdir(source+"/"+file)
        for file in os.listdir("."):
            f = selectFolder(file, keyword)
            if f != None:
                fileName.append(f)
    # os.chdir(source)

#selectFolder()
print("檔名符合",keyword,"關鍵字的檔案如下:")
for file in fileName:
    print(file)