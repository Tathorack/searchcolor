#!/usr/bin/env python3
# coding=UTF-8
from .average import average_image_url

from .average import google_average_process, google_average_threads
from .average import mscs_average_process, mscs_average_threads
from .exceptions import SearchColorException, OversizeException, ZeroResultsException

major_version = 2
minor_version = 1
build_version = 3

__author__ = 'Rhys Hansen'
__copyright__ = "Copyright 2017, Rhys Hansen"
__license__ = "MIT"
__version__ = '{0}.{1}.{2}'.format(major_version, minor_version, build_version)
