#!/usr/bin/env python3
#coding=UTF-8
import os
import sys
#installed
import pytest
#local
sys.path.append(os.path.split(os.path.split(__file__)[0])[0])
import searchcolor

from api_keys import GoogleKeyLocker
from api_keys import BingKeyLocker
from api_keys import MSCSKeyLocker

GKL = GoogleKeyLocker()
BKL = BingKeyLocker()
MSCSKL = MSCSKeyLocker()

def test_google_average():
    result = searchcolor.google_average('Death', 10, GKL.api(), GKL.cse(), max_threads=8)
    assert result.get('name') == 'Death'
    assert result.get('red') >= 0 and result.get('red') <= 255
    assert result.get('green') >= 0 and result.get('green') <= 255
    assert result.get('blue') >= 0 and result.get('blue') <= 255

def test_bing_average():
    result = searchcolor.bing_average('Death', 10, BKL.api(), max_threads=8)
    assert result.get('name') == 'Death'
    assert result.get('red') >= 0 and result.get('red') <= 255
    assert result.get('green') >= 0 and result.get('green') <= 255
    assert result.get('blue') >= 0 and result.get('blue') <= 255

def test_mscs_average():
    result = searchcolor.mscs_average('Death', 10, MSCSKL.api(), max_threads=8)
    assert result.get('name') == 'Death'
    assert result.get('red') >= 0 and result.get('red') <= 255
    assert result.get('green') >= 0 and result.get('green') <= 255
    assert result.get('blue') >= 0 and result.get('blue') <= 255
