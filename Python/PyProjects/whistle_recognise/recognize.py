
import pyaudio
import numpy as np
from scipy import signal
import time

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True)

distinct_whistles = 0
whistle_start_time = None

try:
    while True:
        data = stream.read(1024)
        data = np.frombuffer(data, dtype=np.float32)

        freqs = np.fft.fftfreq(len(data))
        sos = signal.butter(30, 0.2, 'hp', fs=44100, output='sos')
        data = signal.sosfilt(sos, data)
        peaks = signal.find_peaks(data, height:=0.5)[0]

        if len(peaks) > 0:
            if whistle_start_time is None:
                whistle_start_time = time.time()

            if time.time() - whistle_start_time >= 3:
                distinct_whistles += 1
                print('Whistle count:', distinct_whistles)
                whistle_start_time = None

except KeyboardInterrupt:
    pass

finally:
    stream.stop_stream()
    stream.close()

p.terminate()