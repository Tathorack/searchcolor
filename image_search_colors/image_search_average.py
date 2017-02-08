from io import BytesIO
import logging
from multiprocessing import Pool, cpu_count
import requests

import image_colors

from .web_image_search import GoogleImageSearch

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

def average_image_url(url, name):
    """Takes an image url and averages the image.
    Arguments
    url: str
        url for image to average
    name: str
        name to use
    return ["name",r,g,b] or None
    """
    try:
        response = requests.get(url, timeout=5)
        result = image_colors.average_single_image(BytesIO(response.content), name=name)
        return(result)
    except Exception:
        logger.exception('average_image_url Exception @ %s', url)
        logger.debug('average_image_url Traceback', exc_info=True)
        return(None)

def _image_search_average(url_list, max_threads=20):
    """Takes a list of image urls and averages the images to get the
    average color. Designed to be implimented with many methods of
    url sourcing.
    Arguments
    url_list: list
        list of strings with the image urls to average
    max_threads: int
        max number of processes to spawn
    return [r,g,b] or None
    """
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
        results = (p.starmap(average_image_url, zip(url_list, names)))
    for result in results:
        try:
            if result != None:
                r_total += result[1]
                b_total += result[2]
                g_total += result[3]
                imagecount += 1
        except TypeError:
            logger.debug('TypeError when iterating over results', exc_info=True)
    logger.debug('Image count %d', imagecount)
    if imagecount > 0:
        logger.debug('Image count greater then 0')
        r_avg = int(r_total / imagecount)
        g_avg = int(g_total / imagecount)
        b_avg = int(b_total / imagecount)
        return([r_avg, g_avg, b_avg])
    else:
        return(None)

def google_average(search_term, num_results, api_key, cse_id, max_threads=20):
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
    return ["search term",r,g,b] or None
    """
    url_list = []
    result = [search_term]
    GIS = GoogleImageSearch(api_key, cse_id)
    url_list = GIS.search(search_term, num_results)
    result.extend(_image_search_average(url_list, max_threads=max_threads))
    return(result)
