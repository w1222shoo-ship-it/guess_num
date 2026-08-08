import os
import random

os.makedirs("movies", exist_ok=True)
os.chdir("movies")
list = ["凡人修仙傳.mkv","腦筋急轉彎.mp4","神鬼戰士.mp4","惡靈古堡.mp4","惡靈古堡.jpg"]
for file in list:
    open(file, "w").close()

movies = []
for file in os.listdir("."):
    if file.endswith(".mp4") or file.endswith(".mkv"):
        movies.append(file)

print(random.choice(movies))