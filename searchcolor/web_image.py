#!/usr/bin/env python3
#coding=UTF-8
from googleapiclient.discovery import build
from py_bing_search import PyBingImageSearch
from py_ms_cognitive import PyMsCognitiveImageSearch

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

class GoogleImageSearch(object):
    """Class for conducting Google Image Searches
    """
    def __init__(self, api_key, cse_id, file_type='jpg'):
        """Set up search object with your API key and CSE ID
        api_key: str
            Google API key
        cse_id: str
            Google CSE ID
        file_type: str
            file type restriction
        """
        self.api_key = api_key
        self.cse_id = cse_id
        self.file_type = file_type
        self.service = build("customsearch", "v1", developerKey=api_key)

    def search(self, search_term, num_results, **kwargs):
        """Gets x number of Google image result urls for
        a given search term.
        Arguments
        search_term: str
            tearm to search for
        num_results: int
            number of url results to return
        return ['url','url']
        """
        results = []
        count = 1
        while len(results) <= num_results:
            search_results = self.service.cse().list(q=search_term,
                        cx=self.cse_id, searchType="image",
                        fileType=self.file_type, start=count,
                        **kwargs).execute()
            results.extend([r['link'] for r in search_results['items']])
            count += len(search_results)
        results = results[:num_results]
        return(results)

class BingImageSearch(object):
    """docstring for ."""
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, search_term, num_results, **kwargs):
        if num_results > 50:
            raise ValueError('Number of results requested greater than 50!')
        bing_image = PyBingImageSearch(self.api_key, search_term, custom_params="&Adult='off'", **kwargs)
        results = bing_image.search(limit=num_results, format='json')
        return([r.media_url for r in results])

class MicrosoftCognitiveImageSearch(object):
    """docstring for ."""
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, search_term, num_results, thumbnail=True, **kwargs):
        if num_results > 50:
            raise ValueError('Number of results requested greater than 50!')
        search_service = PyMsCognitiveImageSearch(self.api_key, search_term, **kwargs) #custom_params="&safesearch=Off"
        search_results = search_service.search(limit=num_results, format='json')
        if thumbnail == True:
            return([r.thumbnail_url for r in search_results])
        else:
            return([r.content_url for r in search_results])
