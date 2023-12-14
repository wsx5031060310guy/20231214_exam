#!/usr/bin/env python3
import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

print(sys.argv)

if str(sys.argv[1]) == "--metadata":
    url = str(sys.argv[2])

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(response.text, "html.parser")

    print("site: {0}".format(url.replace("https://", "").replace("http://", "")))

    print("num_links: {0}".format(len(soup.find_all('a'))))
    print("images: {0}".format(len(soup.find_all('img'))))
    now = datetime.now(timezone.utc)
    print("last_fetch: {0}".format(now.strftime('%a %b %d %Y %H:%M %Z')))


else:
    for i in range(len(sys.argv)-1):
        # print(sys.argv[i+1])
        url = str(sys.argv[i+1])
        if uri_validator(url):
            
            r = requests.get(url)

            filename = url.replace("https://", "").replace("http://", "")

            modify_html = str(r.text).replace('src="/', 'src="' + url + "/")

            with open(filename + '.html', 'w') as file:
                file.write(modify_html)