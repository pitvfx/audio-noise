import os
import shutil
import tempfile
from typing import Literal

import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment


def generate_random_wave(duration_seconds: int = 2, sample_rate: int = 44100, ) -> np.int16:
    num_samples = duration_seconds * sample_rate
    t = np.linspace(0, duration_seconds, num_samples, endpoint=False)
    # random frequency between 100Hz and 2kHz
    freq = np.random.uniform(100, 2000)
    waveform = 0.5 * np.sin(2 * np.pi * freq * t)
    # Add some noise
    waveform += 0.1 * np.random.randn(*waveform.shape)
    waveform = np.clip(waveform, -1.0, 1.0)
    waveform_int16 = np.int16(waveform * 32767)
    return waveform_int16


def write_tmp_file(wave_data: np.int16, sample_rate: int = 44100) -> str:
    # temp wav file
    _, tmp_file = tempfile.mkstemp(suffix=".wav")
    wavfile.write(tmp_file, sample_rate, wave_data)
    return tmp_file


def export_file(tmp_path: str, output_dir: str = ".", file_name: str = "sound",  file_format: Literal["wav", "ogg", "mp3"] = "wav"):
    if file_format not in ("wav", "ogg", "mp3"):
        raise ValueError("Invalid file format")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, f"{file_name}.{file_format}")
    if file_format == "wav":
        # move tmp file to output dir
        shutil.move(tmp_path, file_path)
        return file_path
    audio = AudioSegment.from_wav(tmp_path)
    audio.export(file_path, format=file_format)
    return file_path
