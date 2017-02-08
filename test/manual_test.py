import os
import sys
import logging

sys.path.append(os.path.split(os.path.split(__file__)[0])[0])

import image_search_colors

from api_keys import GoogleKeyLocker as Key

Key = Key()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s %(levelname)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info(image_search_colors.google_average('Death', 10, Key.api(), Key.cse()))
