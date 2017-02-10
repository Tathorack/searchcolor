# searchcolor - Extract colors from web searches
This module uses imagecolor with PIL(Pillow) to extract colors from web image searches.
### Available functions
#### average_image_url(url, name)
Averages a single image from a url into RGB color values. Returns a dictionary with the following keys: name, red, green, blue
* **url** - image url.
* **name** - name to return. Generally passed from the function that generates the url.

#### \_image_search_average(url_list, max_threads=20)
Averages all urls in a list into a singular RGB average.
* **url_list** - path to directory
* **max_threads** - max processes to spawn.

#### google_average(search_term, num_results, api_key, cse_id, max_threads=20)
Does a Google image search and averages all the images into a singular RGB search average. Returns a dictionary with the following keys: name, red, green, blue
* **search_term** - Google image search term.
* **num_results** - Number of results to include.
* **api_key** - Google API key.
* **cse_id** - Google CSE ID.
* **max_threads** - max processes to spawn. This gets passed to *\_image_search_average(max_threads)*

### Future work
* add more information to readme
* build offline tests
