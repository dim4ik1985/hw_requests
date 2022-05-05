import requests
from pprint import pprint

url = 'http://httpbin.org/get'
resp = requests.get(url)
print(resp)
pprint(resp.json())