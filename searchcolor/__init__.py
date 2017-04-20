#!/usr/bin/env python3
#coding=UTF-8
from .average import average_image_url
from .average import google_average, bing_average, mscs_average
from .average import SearchColorException, OversizeException, ZeroResultsException

major_version = 1
minor_version = 4
build_version = 1

__author__ = 'Rhys Hansen'
__copyright__ = "Copyright 2017, Rhys Hansen"
__license__ = "MIT"
__version__ = '{0}.{1}.{2}'.format(major_version, minor_version, build_version)
