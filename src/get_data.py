import json
import config
import re
import requests


# TODO
# Get data from API through HTTP GET
# Example URL
# https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/biffkriminel%232107/profile/type/br
# Handle the Json data
# Examples
# https://documenter.getpostman.com/view/7896975/SW7aXSo5
# This is complicated as the API is not public

def get_csfr_token():
    url = 'https://profile.callofduty.com/cod/login'
    r = requests.get(url)
    # Pick out the XSFR-token from all other results in the Set-Cookie header
    csfr_result = re.findall('XSRF\-TOKEN=[\S]*;', r.headers['Set-Cookie'])
    # Dark magic!
    # Tidy the XSRF-token string up by removing the 11 first chars (XSRF-TOKEN=) and then remove the trailing ';'
    csfr = csfr_result[0][11:].strip(';')
    return csfr


def get_auth_tokens(token):
    url = 'https://profile.callofduty.com/do_login?new_SiteId=cod'
    json_data = {'username': config.cod_bot_activision_email, 'password': config.cod_bot_activision_password,
                 'remember_me': 'true', '_csrf': token}
    headers = {'Cookie': 'XSRF-TOKEN=' + token}

    r = requests.post(url, data=json_data, headers=headers)
    print(r)
    return r


def get_data():
    # For now we use a static json to have some data to play with
    with open('br.json') as json_file:
        data = json.load(json_file)
    return data['data']


xsrf_token = get_csfr_token()
print(xsrf_token)
auth_tokens = get_auth_tokens(xsrf_token)
