import numpy as np 
import sounddevice as sd 

def generate_brown_noise(duration=5, amplitude=0.5, sample_rate=44100):
    time_points = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    #Generate white noise
    white_noise = np.random.uniform(-1, 1, len(time_points))
    #Integrate to get brown noise
    brown_noise = np.cumsum(white_noise) / sample_rate
    #Normalize amplitude
    brown_noise = amplitude * (brown_noise / np.max(np.abs(brown_noise)))

    return brown_noise

def play_audio(audio_data, sample_rate=44100):
    sd.play(audio_data, sample_rate)
    sd.wait()

if __name__ == "__main__":
    duration = 5
    amplitude = 0.5

    brown_noise = generate_brown_noise(duration, amplitude)
    play_audio(brown_noise)





#     print("Time Points:", time_points)
#     print("White Noise:", white_noise)
#     print("Brown Noise:", brown_noise)

# generate_brown_noise()