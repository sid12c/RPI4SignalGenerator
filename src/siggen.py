__version__ = '2.0'
__author__ = 'Sid Chaudhary'

import time
import numpy as np
import pyaudio
import argparse
# from _version import __version__

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s ' + __version__
                    )
parser.add_argument('type',
                    choices=['sine', 'square', 'sweep'],
                    help='output type of the signal',
                    default='sine',
                    const='sine',
                    nargs='?'
                    )
parser.add_argument('-d', '--duration',
                    help='duration of waveform output in seconds',
                    type=float,
                    default=10.0
                    )
parser.add_argument('-f', '--frequency',
                    help='wave frequency in Hz',
                    type=float,
                    default=440.0
                    )
parser.add_argument('-a', '--amplitude',
                    help='wave amplitude from 0.0 to 1.0',
                    type=float,
                    default=0.5
                    )
parser.add_argument('-e', '--end-frequency',
                    help='(sweep mode only) wave frequency in Hz to end signal sweep',
                    type=float,
                    default=1440.0
                    )
parser.add_argument('-s', '--step',
                    help='(sweep mode only) step size of signal sweep',
                    type=float,
                    default=100
                    )

args = parser.parse_args()

p = pyaudio.PyAudio()

amplitude = args.amplitude  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = args.duration  # in seconds, may be float
f = args.frequency  # waveform frequency, Hz, may be float
ef = args.end_frequency  # wavefrome frequency to end sweep function in Hz
s = args.step  # step between frequencies for sweep function

if args.type != 'sweep':
    # generate samples, note conversion to float32 array
    if args.type == 'sine':
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
    if args.type == 'square':
        samples = (np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * f / fs))).astype(np.float32)

    # per @yahweh comment explicitly convert to bytes sequence
    output_bytes = (amplitude * samples).tobytes()

    if args.type == 'sine':
        print('Playing {:.1f} Hz sine wave'.format(f))
    if args.type == 'square':
        print('Playing {:.1f} Hz square wave'.format(f))

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different amplitude values (if done interactively)
    start_time = time.time()
    stream.write(output_bytes)
    print('Waveform output for {:.2f} seconds'.format(time.time() - start_time))

    stream.stop_stream()
    stream.close()
else:
    for i in range(0,int((ef-f)/s)+1):
        # generate samples, note conversion to float32 array
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * (f + (i * s)) / fs)).astype(np.float32)
        
        # per @yahweh comment explicitly convert to bytes sequence
        output_bytes = (amplitude * samples).tobytes()

        stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

        # play. May repeat with different amplitude values (if done interactively)
        start_time = time.time()
        stream.write(output_bytes)
        print('Output: {:.1f} Hz sine wave for {:.2f} seconds'
              .format(f + (i * s),
                      time.time() - start_time)
                      )
        # print('Waveform output for {:.2f} seconds'.format(time.time() - start_time))

        stream.stop_stream()
        stream.close()

p.terminate()