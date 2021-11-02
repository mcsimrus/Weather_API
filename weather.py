import requests


def main():

    locations = ('London', 'SVO', 'Череповец')

    for location in locations:
        
        url = 'https://wttr.in/{}?Tqnm&lang=ru'.format(location)

        responce = requests.get(url)
        responce.raise_for_status()
        print(responce.text)

if __name__ == '__main__':
    main()