#stdlib
#from io import BytesIO
import os
import sys
#installed
#from PIL import Image
import pytest
#local
sys.path.append(os.path.split(os.path.split(__file__)[0])[0])
import searchcolor

from api_keys import GoogleKeyLocker as Key

Key = Key()

def test_google_average():
    result = searchcolor.google_average('Death', 10, Key.api(), Key.cse())
    assert result.get('name') == 'Death'
    assert result.get('red') >= 0 and result.get('red') <= 255
    assert result.get('green') >= 0 and result.get('green') <= 255
    assert result.get('blue') >= 0 and result.get('blue') <= 255
