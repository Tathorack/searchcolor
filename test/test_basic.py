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

class TestGoogleProcess(object):
    def test_google_average_process_red(self):
        result = searchcolor.google_average_process('red', 10, (google_api, cse))
        assert result['name'] == 'red'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['blue'] >= 0 and result['blue'] <= 255
        assert result['red'] > result['green']
        assert result['red'] > result['blue']


    def test_google_average_process_green(self):
        result = searchcolor.google_average_process('green', 10, (google_api, cse))
        assert result['name'] == 'green'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['red'] >= 0 and result['blue'] <= 255
        assert result['green'] > result['red']
        assert result['green'] > result['blue']


    def test_google_average_process_blue(self):
        result = searchcolor.google_average_process('blue', 10, (google_api, cse))
        assert result['name'] == 'blue'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['blue'] >= 0 and result['blue'] <= 255
        assert result['blue'] > result['red']
        assert result['blue'] > result['green']

class TestGoogleThreads(object):
    def test_google_average_threads_red(self):
        result = searchcolor.google_average_threads('red', 10, (google_api, cse))
        assert result['name'] == 'red'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['blue'] >= 0 and result['blue'] <= 255
        assert result['red'] > result['green']
        assert result['red'] > result['blue']


    def test_google_average_threads_green(self):
        result = searchcolor.google_average_threads('green', 10, (google_api, cse))
        assert result['name'] == 'green'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['red'] >= 0 and result['blue'] <= 255
        assert result['green'] > result['red']
        assert result['green'] > result['blue']


    def test_google_average_threads_blue(self):
        result = searchcolor.google_average_threads('blue', 10, (google_api, cse))
        assert result['name'] == 'blue'
        assert result['red'] >= 0 and result['red'] <= 255
        assert result['green'] >= 0 and result['green'] <= 255
        assert result['blue'] >= 0 and result['blue'] <= 255
        assert result['blue'] > result['red']
        assert result['blue'] > result['green']
