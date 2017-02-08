#stdlib
#from io import BytesIO
import os
import sys
#installed
#from PIL import Image
import pytest
#local
sys.path.append(os.path.split(os.path.split(__file__)[0])[0])
import image_search_colors

from api_keys import GoogleKeyLocker as Key

Key = Key()

def test_cwd():
    location = __file__
    test_dir = os.path.split(location)[0]
    project_dir = os.path.split(test_dir)[0]
    assert location == '/Users/rhyshansen/programming/source/Python/imagesearchcolors/test/test_basic.py'
    assert test_dir == '/Users/rhyshansen/programming/source/Python/imagesearchcolors/test'
    assert project_dir == '/Users/rhyshansen/programming/source/Python/imagesearchcolors'

def test_google_average():
    result = image_search_colors.google_average('Death', 10, Key.api(), Key.cse())
    assert result[0] == 'Death'
    assert result[1] >= 0 and result[1] <= 255
    assert result[2] >= 0 and result[2] <= 255
    assert result[3] >= 0 and result[3] <= 255
