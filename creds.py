import getpass
from json import loads

from requests import post

url = 'https://api.studi.se/oauth/access_token'
headers = {
    'Content-Type': "application/json",
}


def authorize():
    while True:
        username = input('Namn: ')
        password = getpass.getpass('Lösenord: ')

        print('\nLoggar in...')

        payload = "{\"grant_type\":\"password\",\"username\":\"" + username + "\",\"password\":\"" + password + "\",\"client_id\":\"studi_ember\",\"client_secret\":\"ED1DA59DFCB83A43616CE714189CE\",\"scope\":\"view_lessons\"}\r\n"

        response = post(url=url, data=payload, headers=headers)
        data = loads(response.text)

        if 'error_message' in data:
            print('Fel lösenord eller namn')
            continue
        break

    return {
        'token': data['access_token'],
        'user_id': str(data['user_id'])
    }
