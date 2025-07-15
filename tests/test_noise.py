#!.venv/bin/python
import os
import pytest
import numpy as np
from noise import generate_random_wave, write_tmp_file, export_file


def test_generate_random_wave():
    wave_data = generate_random_wave()
    assert isinstance(wave_data, np.ndarray)
    assert wave_data.dtype == np.int16
    assert len(wave_data) > 0


def test_generate_random_wave_params():
    wave_data = generate_random_wave(duration_seconds=5, sample_rate=22050)
    assert isinstance(wave_data, np.ndarray)
    assert wave_data.dtype == np.int16
    assert len(wave_data) > 0


def test_write_tmp_file():
    wave_data = generate_random_wave()
    tmp_path = write_tmp_file(wave_data)
    assert os.path.exists(tmp_path)
    assert tmp_path.endswith('.wav')


def test_export_file_wav():
    wave_data = generate_random_wave()
    tmp_path = write_tmp_file(wave_data)
    file_name = 'test_sound'
    file_path = export_file(tmp_path, file_name=file_name, file_format='wav')
    assert os.path.exists(file_path)
    assert file_path.endswith('.wav')


def test_export_file_mp3():
    wave_data = generate_random_wave()
    tmp_path = write_tmp_file(wave_data)
    file_name = 'test_sound'
    file_path = export_file(tmp_path, file_name=file_name, file_format='mp3')
    assert os.path.exists(file_path)
    assert file_path.endswith('.mp3')


def test_export_file_ogg():
    wave_data = generate_random_wave()
    tmp_path = write_tmp_file(wave_data)
    file_name = 'test_sound'
    file_path = export_file(tmp_path, file_name=file_name, file_format='ogg')
    assert os.path.exists(file_path)
    assert file_path.endswith('.ogg')


def test_export_file_invalid_format():
    wave_data = generate_random_wave()
    tmp_path = write_tmp_file(wave_data)
    file_name = 'test_sound'
    with pytest.raises(ValueError):
        export_file(tmp_path, file_name=file_name, file_format='invalid')
