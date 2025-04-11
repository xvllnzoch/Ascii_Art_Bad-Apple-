# Original Sources:
# https://www.youtube.com/watch?v=v-fc1zv31zE&ab_ Bad Apple!! feat.SEKAI 
# Exact replica for Bad Apple!! Original Version
# Duh it's pain in the ass having to change the mp3 and mp4 and the ascii characters

import cv2
import numpy as np
import time
import os
import pygame

# ASCII characters 
ASCII_CHARS = '  .,:;+*&%@#$' # ascii_chars 
    # '  .,:;+*&%@#$' for Bad Apple!! feat.SEKAI (SEKAI version)

# Video path for capture
video_path = "SEKAI_Bad_apple!!.mp4" # change mp4 file path for different versions of Bad Apple!!
audio_path = "SEKAI_Bad_apple!!.mp3" # change mp3 file path for different versions of Bad Apple!!

cap = cv2.VideoCapture(video_path) # for mp4

# Output width
OUTPUT_WIDTH = 150  # terminal size (make sure to scroll the terminal to the top for full view 
                                    # or else you can't see the whole thing) or (zoom in on Visual Studio Community)
fps = cap.get(cv2.CAP_PROP_FPS) 
frame_time = 1 / fps  # Time per frame 

# audio using pygame
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.set_volume(1)  # Adjust accordingly (0.0 to 1.0)

# Function to convert the frame to ASCII 
def bad_apple_frame_to_ascii(frame, width=OUTPUT_WIDTH):
    height, orig_width = frame.shape
    aspect_ratio = orig_width / height
    new_height = int(width / aspect_ratio * 0.5)  # height scaling
    resized_frame = cv2.resize(frame, (width, new_height))

    ascii_frame = "\n".join(
        "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in row)
        for row in resized_frame
    )
    return ascii_frame

# Start audio (to sync in with the video) using pygame
pygame.mixer.music.play()
start_time = time.time()  # time tracking (making sure every frame counts)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  
        # If complete scroll down the terminal | for Visual Studio Community close down the terminal 
    # Convert frame to grayscale (hahaha)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert to ASCII
    ascii_art = bad_apple_frame_to_ascii(gray_frame)

    # Clear screen and print ASCII frame 
    # If the screen flashes abnormally make adjustments
    os.system("cls" if os.name == "nt" else "clear")  # Windows: cls
    print(ascii_art)

    # Sync with audio
    frame_count += 1
    expected_time = start_time + (frame_count * frame_time)
    sleep_time = max(0, expected_time - time.time())  # no negative 
    time.sleep(sleep_time)

# Finishes after the video ends
cap.release()
pygame.mixer.music.stop()
