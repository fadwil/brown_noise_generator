import numpy as np 
import sounddevice as sd 
import tkinter as tk
from tkinter import Scale, Button

def generate_brown_noise(duration=5, amplitude=0.5, fade_duration=1.0, sample_rate=44100):
    time_points = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate white noise
    white_noise = np.random.uniform(-1, 1, len(time_points))
    # Integrate to get brown noise
    brown_noise = np.cumsum(white_noise) / sample_rate
    # Normalize amplitude
    brown_noise = amplitude * (brown_noise / np.max(np.abs(brown_noise)))

    # Apply fade-out
    fade_out_samples = int(fade_duration * sample_rate)
    brown_noise[-fade_out_samples:] *= np.linspace(1, 0, fade_out_samples)

    return brown_noise

def play_audio(audio_data, sample_rate=44100):
    sd.play(audio_data, sample_rate)
    sd.wait()

class BrownNoiseGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Brown Noise Generator")

        self.duration_scale = Scale(master, label="Duration (s)", from_=1, to=20, resolution=1, orient="horizontal", length=200)
        self.amplitude_scale = Scale(master, label="Amplitude", from_=0, to=2, resolution=0.01, orient="horizontal", length=200)
        self.amplitude_scale.set(0.5)  # Set default amplitude to 0.5

        self.fade_duration_scale = Scale(master, label="Fade Duration (s)", from_=0, to=10, resolution=0.1, orient="horizontal", length=200)
        self.fade_duration_scale.set(1.0)  # Set default fade duration to 1.0 seconds

        self.generate_button = Button(master, text="Generate and Play", command=self.generate_and_play)

        self.duration_scale.pack()
        self.amplitude_scale.pack()
        self.fade_duration_scale.pack()
        self.generate_button.pack()

    def generate_and_play(self):
        duration = self.duration_scale.get()
        amplitude = self.amplitude_scale.get()
        fade_duration = self.fade_duration_scale.get()

        brown_noise = generate_brown_noise(duration, amplitude, fade_duration)
        play_audio(brown_noise)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrownNoiseGeneratorApp(root)
    root.mainloop()
