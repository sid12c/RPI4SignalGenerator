# SignalGenerator 

> This Python script generates and plays a waveform (sine or square) of a 
> specified frequency, duration, and amplitude using the `pyaudio` and `numpy` 
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
python siggen.py [type] [-d DURATION] [-f FREQUENCY] [-a AMPLITUDE] 
```

### Arguments

#### Positional arguments:
    {sine,square,sweep}     output type of the signal

#### Options:
    -h, --help              show this help message and exit

    -v, --version           show program's version number and exit

    -d DURATION, --duration DURATION

                            duration of waveform output in seconds

    -f FREQUENCY, --frequency FREQUENCY

                            wave frequency in Hz

    -a AMPLITUDE, --amplitude AMPLITUDE

                            wave amplitude from 0.0 to 1.0

    -e END_FREQUENCY, --end-frequency END_FREQUENCY

                            (sweep mode only) final frequency value of sweep in Hz

    -s STEP, --step STEP    (sweep mode only) step size of signal sweep

#### Defaults
|   Argument        |   Default Value   |
|   -------------   |   -------------   |
|   Type            |   sine            |
|   Duration        |   10.0            |
|   Frequency       |   440.0           |
|   Amplitude       |   0.5             |
|   End_Frequency   |   1440.0          |
|   Step            |   100             |

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
- Play a frequency sweep from 440Hz to 1440Hz with steps of 100Hz:
```Bash
python siggen.py sweep -f 440 -e 1440 -s 100
```

## Description

The script uses numpy to generate the waveform samples and pyaudio to play the 
audio. It takes command-line arguments using the argparse module to customize 
the generated sound.

- Sine and Square waves: The script calculates the samples for the specified 
  waveform type (sine or square) and then plays them through the system's audio 
  output. The amplitude is applied to the generated samples before they are 
  converted to bytes and sent to the audio stream.
  
- Sweep mode: The script generates a series of sine waves, incrementing the 
  frequency from the starting frequency to the ending frequency with the 
  specified step size. Each frequency is played for the specified duration.

## Notes

- Ensure you have the necessary audio drivers installed for pyaudio to work correctly.
- The sampling rate is fixed at 44100 Hz.
- The script uses a float32 sample format.
- Signal output is dependent on system sink volume.
- The sweep mode only generates sine waves.
- Signal output is dependent on system sink volume which can be set using the following command

```bash
 pactl -- set-sink-volume 0 100%
```

## Contact

Sid Chaudhary - contact.sid.chaudhary@gmail.com
