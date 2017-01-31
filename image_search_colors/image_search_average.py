import requests
from io import BytesIO
from multiprocessing import Pool, cpu_count

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

def average_image_url(url, name):
    try:
        response = requests.get(url, timeout=5)
        result = image_colors.average_single_image(BytesIO(response.content), name=name)
        return(result)
    except Exception as e:
        print("Exception")
        return(['failed', 0, 0, 0])

def _image_search_average(search_term, results, num_results):
    r_total = 0
    b_total = 0
    g_total = 0
    imgcount = 0
    names = ['{0}{1}'.format(search_term, count) for count in range(len(results))]
    if num_results <= 20:
        threads = num_results
    else:
        threads = 20

    with Pool(threads) as p:
        results = (p.starmap(average_image_url, zip(results, names)))
    for result in results:
        try:
            if result != None or result[0] != 'failed':
                r_total += result[1]
                b_total += result[2]
                g_total += result[3]
                imgcount += 1
        except TypeError as e:
            pass
        except Exception as e:
            print(e)
    if imgcount > 0:
        r_avg = int(r_total/imgcount)
        g_avg = int(g_total/imgcount)
        b_avg = int(b_total/imgcount)
        return([search_term, r_avg, g_avg, b_avg])
    else:
        return(None)

def google_average(search_term, num_results, api_key, cse_id):
    results = []
    GIS = GoogleImageSearch(api_key, cse_id)
    results = GIS.search(search_term, num_results)
    return(_image_search_average(search_term, results, num_results))
