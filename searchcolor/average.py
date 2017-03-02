#!/usr/bin/env python3
#coding=UTF-8
from functools import partial
from io import BytesIO
import logging
import math
from multiprocessing import Pool, cpu_count
import requests

import imagecolor

from .web_image import GoogleImageSearch

"""Copyright © 2017 Rhys Hansen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

logger = logging.getLogger(__name__)

class OversizeException(Exception):
    pass

class SearchAveragingError(Exception):
    pass

def average_image_url(url, name, timeout=5, max_size=5):
    """Takes an image url and averages the image.
    Arguments
    url: str
        url for image to average
    name: str
        name to use
    timeout: int
        request timeout in seconds
    max_size: int
        max size of request in MB
    return {red':r_avg, 'green':g_avg, 'blue':b_avg} or None
    """
    try:
        shorturl = url.rsplit('/', 1)[-1]
        logger.debug('Full URL,           %s', url)
        response = requests.get(url, timeout=timeout, stream=True)
        length = int(response.headers.get('Content-Length', 0))
        logger.debug('Request size,       %s - %.2fKB', shorturl, length/1024)
        if length > (1024 * 1024 * max_size):
            raise OversizeException('Response size {2}MB, larger than {0}MB, discarding: {1}'.format(max_size, url, math.ceil(length/1024/1024)))
        logger.debug('Finished request,   %s', shorturl)
        result = imagecolor.average(BytesIO(response.content), name=name)
        logger.debug('Averaging complete, %s', shorturl)
        return(result)
    except OversizeException as e:
        logger.warning('Exception: %s', e)
        return(None)
    except Exception as e:
        logger.warning('Exception: %s @ %s', e, url)
        logger.debug('Traceback:', exc_info=True)
        return(None)

def _image_search_average(url_list, max_threads=2, **kwargs):
    """Takes a list of image urls and averages the images to get the
    average color. Designed to be implimented with many methods of
    url sourcing.
    Arguments
    url_list: list
        list of strings with the image urls to average
    max_threads: int
        max number of processes to spawn
    return {red':r_avg, 'green':g_avg, 'blue':b_avg} or None
    """
    if len(url_list) < 1:
        raise SearchAveragingError('No urls to average')
    r_total = 0
    b_total = 0
    g_total = 0
    imagecount = 0
    num_results = len(url_list)
    names = [n for n in range(num_results)]
    if num_results <= max_threads:
        threads = num_results
    else:
        threads = max_threads
    with Pool(threads) as p:
        results = p.starmap(partial(average_image_url, **kwargs), zip(url_list, names))
    logger.debug('All results averaged')
    for result in results:
        try:
            if result != None:
                r_total += result.get('red')
                b_total += result.get('green')
                g_total += result.get('blue')
                imagecount += 1
        except TypeError:
            logger.debug('TypeError when iterating over results', exc_info=True)
    logger.debug('Image count %d', imagecount)
    if imagecount > 0:
        logger.debug('Image count greater then 0')
        r_avg = int(r_total / imagecount)
        g_avg = int(g_total / imagecount)
        b_avg = int(b_total / imagecount)
        return({'red':r_avg, 'green':g_avg, 'blue':b_avg})
    else:
        raise SearchAveragingError('Nothing averaged successfully')

def google_average(search_term, num_results, api_key, cse_id, **kwargs):
    """Does a Google image search to get the average color of the
    top x results.
    Arguments
    search_term: str
        tearm to search for
    num_results: int
        number of results to average
    api_key: str
        Google API key
    cse_id: str
        Google CSE ID
    max_threads: int
        max number of processes to spawn

    return {'name':search_term, 'red':r_avg, 'green':g_avg, 'blue':b_avg} or None
    """
    url_list = []
    result = {'name':search_term}
    GIS = GoogleImageSearch(api_key, cse_id)
    url_list = GIS.search(search_term, num_results)
    result.update(_image_search_average(url_list, **kwargs))
    return(result)
