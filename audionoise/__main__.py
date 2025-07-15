#!.venv/bin/python

import argparse
import os

from noise import generate_random_wave, write_tmp_file, export_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", "-d", type=int, default=2,
                        help="Duration in seconds (default: 2)")
    parser.add_argument("--rate", "-r", type=int,
                        default=44100, help="Sample rate in Hz (default: 44100)")
    parser.add_argument("--dir", "-o", type=str,
                        default="./output", help="Output directory (default: ./output)")
    parser.add_argument("--name", "-n", type=str,
                        default="sound", help="File name (default: sound)")
    parser.add_argument("--format", "-f", type=str,
                        default="wav", help="File format (wav, ogg, mp3) (default: wav)", choices=["wav", "ogg", "mp3"])
    args = parser.parse_args()
    duration = args.duration
    rate = args.rate
    output_dir = args.dir
    file_name = args.name.split(".")[0]
    file_format = args.format
    wave_data = generate_random_wave(
        duration_seconds=duration, sample_rate=rate)
    tmp_path = write_tmp_file(wave_data, rate)
    os.makedirs(output_dir, exist_ok=True)
    export_file(tmp_path, output_dir, file_name, file_format)
