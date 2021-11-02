import requests


def main():

    locations = ('London', 'SVO', 'Череповец')

    for location in locations:
        
        #url = 'https://wttr.in/{}?Tqnm&lang=ru'.format(location)
        url = 'https://wttr.in/{}'.format(location)

        payload = {'key':'Tqnm','lang':'ru'}
                
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
        #print(response.url)

if __name__ == '__main__':
    main()