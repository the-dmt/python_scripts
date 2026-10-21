from moviepy import *
import os

video = input("Enter video file: ")

myclip = VideoFileClip(video)

# Here we just save in dir output with filename being his index (start at 0, then +1 for each frame)
os.mkdir("/Users/dion/Pictures/output")
myclip.write_images_sequence("/Users/dion/Pictures/output/%d.jpg")

# We set the FPS of our GIF at 10, and we leftpad name with 0 up to 4 digits
# myclip.write_images_sequence("./output/%04d.jpg")
