# Python 3.6.5
# Checks a URL against the PhishTank database.
# !! NOTE !! Still a work in progress.

import requests
import base64


def check_phishtank(search):
    api_key = 'bb7da612a507679bb53ef5c918e67b35d547b35cf8ca1e2e738b11dd078a992c'
    api_url = 'http://checkurl.phishtank.com/checkurl/'
    post_data = {
        'url': base64.b64encode(search.encode("utf-8")),
        'format': 'json',
        'app_key': api_key,
    }

    response = requests.post(api_url, data=post_data)

    in_database = response.get('in_database', None)
    verified = response.get('verified', None)
    valid = response.get('valid', None)

    result = f'{in_database} {verified} {valid}'
    return result


if __name__ == "__main__":
    check_phishtank(input())
