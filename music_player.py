import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Play selected song
def play_music():
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        song_label.config(text="Playing: " + file.split("/")[-1])

def stop_music():
    pygame.mixer.music.stop()
    song_label.config(text="Music stopped")

# Create GUI window
window = tk.Tk()
window.title("🎵 Music Player")
window.geometry("300x200")

song_label = tk.Label(window, text="Select a song to play", wraplength=250)
song_label.pack(pady=10)

play_button = tk.Button(window, text="▶️ Play", command=play_music)
play_button.pack(pady=5)

stop_button = tk.Button(window, text="⏹ Stop", command=stop_music)
stop_button.pack(pady=5)

window.mainloop()