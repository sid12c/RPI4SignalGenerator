# RPI4SignalGenerator 

> This Python script generates and plays a sine wave of a specified frequency, duration, and volume using the `pyaudio` and `numpy` libraries.

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
python src/main.py [-d DURATION] [-f FREQUENCY] [-v VOLUME]
```

### Arguments

-d, --duration: Duration of the waveform output in seconds (default: 10.0). Accepts float values.

-f, --frequency: Sine frequency in Hz (default: 440.0). Accepts float values.

-v, --volume: Sound volume from 0.0 (mute) to 1.0 (maximum) (default: 0.5). Accepts float values.

## Examples
- Play a 5-second sine wave at 500 Hz with a volume of 0.7:
```Bash
python sine_wave_generator.py -d 5 -f 500 -v 0.7
```
- Play a 10-second (default) sine wave at 440 Hz (default) with maximum volume:
```Bash
python sine_wave_generator.py -v 1.0
```
- Play a 2-second sine wave at 200 Hz with a volume of 0.2:
```Bash
python sine_wave_generator.py -d 2 -f 200 -v 0.2
```

## Description
The script uses argparse to handle command-line arguments for duration, frequency, and volume. It then generates a sine wave using numpy and plays it using pyaudio.  The script explicitly converts the numpy array of samples to a byte sequence using .tobytes() as required by pyaudio. The sample format used is paFloat32, meaning sample values must be within the range [-1.0, 1.0]. The script prints the frequency being played and the actual duration of the playback.

## Notes
- Ensure you have the necessary audio drivers installed for pyaudio to work correctly.
- The sampling rate is fixed at 44100 Hz.
- The script uses a float32 sample format.
- Signal output is dependent on system sink volume which can be set using the following command

```bash
 pactl -- set-sink-volume 0 100%
```