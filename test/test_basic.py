#!/usr/bin/env python3
# coding=UTF-8
import os
import sys
# installed
import pytest
# local
sys.path.append(os.path.split(os.path.split(__file__)[0])[0])
import searchcolor

google_api = os.environ["GOOGLE_SEARCH_API"]
cse = os.environ["GOOGLE_SEARCH_CSE"]


def test_api_keys():
    assert google_api is not None
    assert cse is not None


def test_google_average_red():
    result = searchcolor.google_average(
        'red', 10, google_api, cse, max_threads=8)
    assert result['name'] == 'red'
    assert result['red'] >= 0 and result['red'] <= 255
    assert result['green'] >= 0 and result['green'] <= 255
    assert result['blue'] >= 0 and result['blue'] <= 255
    assert result['red'] > result['green']
    assert result['red'] > result['blue']


def test_google_average_green():
    result = searchcolor.google_average(
        'green', 10, google_api, cse, max_threads=8)
    assert result['name'] == 'green'
    assert result['red'] >= 0 and result['red'] <= 255
    assert result['green'] >= 0 and result['green'] <= 255
    assert result['red'] >= 0 and result['blue'] <= 255
    assert result['green'] > result['red']
    assert result['green'] > result['blue']


def test_google_average_blue():
    result = searchcolor.google_average(
        'blue', 10, google_api, cse, max_threads=8)
    assert result['name'] == 'blue'
    assert result['red'] >= 0 and result['red'] <= 255
    assert result['green'] >= 0 and result['green'] <= 255
    assert result['blue'] >= 0 and result['blue'] <= 255
    assert result['blue'] > result['red']
    assert result['blue'] > result['green']
