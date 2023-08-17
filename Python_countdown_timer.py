import time
import tkinter as tk
from tkinter import messagebox
import pygame
import os


class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_label = tk.Label(root, text="Time Remaining: ")
        self.time_label.pack()

        #self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        #self.start_button.pack()

        self.duration = 0
        self.running = False

        pygame.mixer.init()
        alarm_sound_path = os.path.join(os.path.dirname(__file__), "alarm.mp3")
        self.alarm_sound = pygame.mixer.music.load("alarm.mp3")
        self.alarm_sound = self.load_alarm_sound()
        self.start_widget()

    def start_widget(self):
        self.label = tk.Label(self.root, text="Enter the number of minutes for the timer: ")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.button.pack()
        

    def start_timer(self):
        if not self.running:
            self.duration = self.get_user_input()
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.running and self.duration > 0:
            minutes, secs = divmod(self.duration, 60)
            timeformat = '{:02d}:{:02d}'.format(minutes, secs)
            self.time_label.config(text="Time Remaining: " + timeformat)
            self.duration -= 1
            self.root.after(1000, self.update_timer)
        elif self.duration == 0:
            self.running = False
            self.show_time_up_message()
            self.time_label.config(text="Time Remaining: ")

    def load_alarm_sound(self):
        try:
            pygame.mixer.music.load("alarm.mp3")
            return pygame.mixer.music
        except pygame.error:
            print("Unable to load alarm sound: " + pygame.get_error())
            
    def show_time_up_message(self):
        self.alarm_sound.play()
        messagebox.showinfo("Time's Up", "Time's Up!")
        self.alarm_sound.stop()
        
    def get_user_input(self):
        try:
            minutes = int(self.entry.get())#("Enter the number of minutes for the timer: "))
            seconds = minutes * 60
            return seconds
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.get_user_input()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()