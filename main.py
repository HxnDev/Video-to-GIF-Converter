from moviepy.editor import *


def convert_mp4_to_jpgs(path):
    clip = VideoFileClip(path).resize(0.3)
    clip.write_gif("garbled.gif")


if __name__ == "__main__":
    convert_mp4_to_jpgs("Garbled Image.mp4")