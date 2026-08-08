import os


os.makedirs("downloads", exist_ok=True)
os.chdir("downloads")

for file in os.listdir("."):
    os.remove(file)

fake_files = ["report.pdf", "meme.jpg", "photo.png", "song.mp3",
              "notes.txt", "installer.exe", "video.mp4", "data.csv","test.zip"]
for file in fake_files:
    open(file, "a").close()

print("目前檔案",os.listdir("."))


# 分類
rules = {
    ".pdf": "文件",
    ".txt": "文件",
    ".csv": "文件",
    ".jpg": "圖片",
    ".png": "圖片",
    ".gif": "圖片",
    ".mp3": "音樂",
    ".mp4": "影片",
    ".exe": "程式",
}

for file in os.listdir("."):
    #print("目前檔案", file)
    #依rules搬檔案
    ext = os.path.splitext(file)[1].lower()
    rule = rules.get(ext)
    if rule == None:
        rule = "其他"
    #print(rule)
    os.makedirs(rule, exist_ok=True)
    os.rename(file, os.path.join(rule, file))
    print(file,"檔案分類至",os.getcwd(),"/",rule)