from moviepy.editor import *


def convert_mp4_to_jpgs(path):
    clip = VideoFileClip(path).subclip((0,19.00),(0,25.0)).resize(0.3)
    clip.write_gif("counter.gif")


if __name__ == "__main__":
    convert_mp4_to_jpgs("Empty Counter Detection (Full Video).mp4")