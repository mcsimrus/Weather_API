import requests


def main():

    locations = ('London', 'SVO', 'Череповец')

    for location in locations:
        
        url = 'https://wttr.in/{}?Tqnm&lang=ru'.format(location)

        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    main()