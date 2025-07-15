# audio noise

A simple audio noise generator CLI in Python. The noise is a sine wave with a random frequency and amplitude.

## usage:

audionoise [-h] [--duration DURATION] [--rate RATE] [--dir DIR] [--name NAME] [--format {wav,ogg,mp3}]

## options:

-h, --help show this help message and exit

--duration, -d DURATION Duration in seconds (default: 2)

--rate, -r RATE Sample rate in Hz (default: 44100)

--dir, -o DIR Output directory (default: ./output)

--name, -n NAME File name (default: sound)

--format, -f {wav,ogg,mp3} File format (wav, ogg, mp3) (default: wav)
