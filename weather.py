import requests


def main():

    locations = ('London', 'SVO', 'Череповец')

    for location in locations:
        url = 'https://wttr.in/{}'.format(location)

        payload = {'Tqnm': '', 'lang': 'ru'}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    main()
