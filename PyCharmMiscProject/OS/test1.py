import os
os.makedirs("test1_file", exist_ok=True)
os.chdir("test1_file")

for file in os.listdir("."):
    os.remove(file)

fake_files = ["螢幕擷取畫面 2026-01-01.png", "螢幕擷取畫面 2026-01-02.png", "螢幕擷取畫面 2026-01-03.png", "Screenshot_20260102.png",
              "Screenshot_20260103.png", "installer.exe", "video.mp4", "data.csv","test.zip"]

for file in fake_files:
    open(file, "a").close()

printlist = []
for file in os.listdir("."):
    # print(file)
    # x = file.find("螢幕擷取畫面")
    # print(x)
    try:
        if file.find("螢幕擷取畫面") > -1 or file.find("Screenshot") > -1:
            printlist.append(file)
    except:
        pass
    #print(file.index("螢幕擷取畫面"))


print(printlist)
