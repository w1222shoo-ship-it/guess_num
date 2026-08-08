import os

floder = "test3_file"

os.makedirs("test3_file", exist_ok=True)
os.chdir("test3_file")

for file in os.listdir("."):
    os.remove(file)

fake_files = ["report.pdf", "meme.jpg", "photo.png", "song.mp3",
              "notes.txt", "installer.exe", "video.mp4", "data.csv","test.zip"]

for file in fake_files:
    open(file, "a")

fileList = []

exp = ["jpg","png","gif"]
#os.chdir(floder)
for file in os.listdir('.'):
    try:
        if exp.index(file.split(".")[1]) > -1:
    # if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
            fileList.append(file)
    except:
        pass

print(fileList)

os.makedirs("memes", exist_ok=True)
for file in fileList:
    os.rename(file,os.path.join("memes",file))