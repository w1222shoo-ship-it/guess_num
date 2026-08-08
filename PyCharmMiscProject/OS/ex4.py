import os

os.makedirs("my_stuff/photos", exist_ok=True)
os.makedirs("my_stuff/videos", exist_ok=True)

test_files = [
    ("my_stuff/photos/pic1.jpg", 500),
    ("my_stuff/photos/pic2.jpg", 3000),
    ("my_stuff/videos/movie.mp4", 15000),
    ("my_stuff/videos/clip.mp4", 8000),
    ("my_stuff/note.txt", 100),
]


print()