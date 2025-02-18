import time
import numpy as np
import pyaudio
import argparse

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("type",
                    choices=["sine", "square"],
                    help="output type of the signal",
                    default="sine",
                    const="sine",
                    nargs="?")
parser.add_argument("-d", "--duration",
                    help="duration of waveform output in seconds",
                    type=float,
                    default=10.0)
parser.add_argument("-f", "--frequency",
                    help="wave frequency in Hz",
                    type=float,
                    default=440.0)
parser.add_argument("-a", "--amplitude",
                    help="wave amplitude from 0.0 to 1.0",
                    type=float,
                    default=0.5)
args = parser.parse_args()

p = pyaudio.PyAudio()

amplitude = args.amplitude  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = args.duration  # in seconds, may be float
f = args.frequency  # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
if args.type == "sine":
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
if args.type == "square":
    samples = (np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * f / fs))).astype(np.float32)

# per @yahweh comment explicitly convert to bytes sequence
output_bytes = (amplitude * samples).tobytes()

if args.type == "sine":
    print("Playing {:.1f} Hz sine wave".format(f))
if args.type == "square":
    print("Playing {:.1f} Hz square wave".format(f))

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different amplitude values (if done interactively)
start_time = time.time()
stream.write(output_bytes)
print("Waveform output for {:.2f} seconds".format(time.time() - start_time))

stream.stop_stream()
stream.close()

p.terminate()