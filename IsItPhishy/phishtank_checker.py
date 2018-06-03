# Python 3.6.5
# Checks a URL against the PhishTank database.
# Still a work in progress.
import requests
import base64
import configparser


def check_phishtank(search):
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config.get('IsItPhishy', 'api_key')
    api_url = config.get('IsItPhishy', 'api_url')
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
