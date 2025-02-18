# RPI4SignalGenerator 

> This Python script generates and plays a waveform (sine or square) of a 
> specified frequency, duration, and volume using the `pyaudio` and `numpy` 
> libraries.

## Requirements

- Python
- `numpy`
- `pyaudio`
- `argparse`

You can install these libraries using pip:

```bash
pip install numpy pyaudio argparse
```

## Usage
```bash
python siggen.py [type] [-d duration] [-f frequency] [-a amplitude]
```

### Arguments

type: (Optional) The type of waveform to generate. 
Can be sine or square. Defaults to sine.

-d, --duration: (Optional) The duration of the waveform 
in seconds. Defaults to 10.0.

-f, --frequency: (Optional) The frequency of the waveform in Hz. 
Defaults to 440.0.

-a, --amplitude: (Optional) The amplitude of the waveform, ranging 
from 0.0 to 1.0. Defaults to 0.5.

## Examples
- Play a sine wave with default parameters (10 seconds, 440Hz, 0.5 amplitude):
```Bash
python siggen.py
```
- Play a 5-second sine wave at 500 Hz with an amplitude of 0.7:
```Bash
python siggen.py sine -d 5 -f 500 -a 0.7
```
- Play a 10-second square wave at the default frequency and amplitude:
```Bash
python siggen.py square
```

## Description
The script uses numpy to generate the waveform samples and pyaudio to play the 
audio. It takes command-line arguments using the argparse module to customize 
the generated sound. The script calculates the samples for the specified 
waveform type (sine or square) and then plays them through the system's audio 
output. The amplitude is applied to the generated samples before they are 
converted to bytes and sent to the audio stream.

## Notes
- Ensure you have the necessary audio drivers installed for pyaudio to work correctly.
- The sampling rate is fixed at 44100 Hz.
- The script uses a float32 sample format.
- Signal output is dependent on system sink volume which can be set using the following command

```bash
 pactl -- set-sink-volume 0 100%
```
## Contact
Sid Chaudhary - contact.sid.chaudhary@gmail.com