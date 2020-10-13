import json
import requests
import config

# TODO
# Get data from API through HTTP GET
# Example URL
# https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/biffkriminel%232107/profile/type/br
# Handle the Json data
# Examples
# https://documenter.getpostman.com/view/7896975/SW7aXSo5
# This is complicated as the API is not public

XSRF_TOKEN = 'token'
url = 'https://profile.callofduty.com/do_login?new_SiteId=cod'
payload = {'username': config.cod_bot_activision_email, 'password': config.cod_bot_activision_password,
           'remember_me': 'true', '_csrf': XSRF_TOKEN}
headers = {"XSRF-TOKEN": XSRF_TOKEN}
params = {"new_SiteId": "cod"}

# r = requests.get(url, params={payload}, headers={headers})

# For now we use a static json to have some data to play with
with open('br.json') as json_file:
    data = json.load(json_file)


def get_data():
    return data['data']
