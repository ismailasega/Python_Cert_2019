# Create a python script called googlesearch that provides a command line utility to
# perform google search. It gives you the top links (search results) of whatever you want to
# search on google

import urllib.request
import json

url = 'https://serpapi.com/playground?engine=google&q='
search = input("Enter Search:")
search = urllib.parse.urlencode({'q': search})
response = urllib.request.urlopen(url + search).read()
data = json.loads(response.decode('utf-8'), strict=False)
results = data['responseData']['results']


for result in results:
    title = result['title']
    url = result['url']
    print(title + '; ' + url)