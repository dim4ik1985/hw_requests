import requests
from pprint import pprint


def get_request_question(url, params):
    res = requests.get(url, params=params)
    return res.json()


url_quest = 'https://api.stackexchange.com/2.3/questions'
params_quest = {'tagged': 'python', 'site': 'stackoverflow', 'order': 'desc', 'sort': 'creation', 'fromdate': 1651536000,
          'todate': 1651708800}
pprint(get_request_question(url_quest, params_quest))
