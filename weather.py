import requests


locations = ('London', 'SVO', 'Череповец')

def main():
    for location in locations:
        
        url = 'https://wttr.in/{}?qnm&lang=ru'.format(location)

        responce = requests.get(url)
        responce.raise_for_status()
        print(responce.text)

if __name__ == '__main__':
    main()