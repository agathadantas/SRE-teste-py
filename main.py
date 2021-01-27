# coding: utf-8
import requests


def main():
    print('####################')
    print('### The Cat API ####')
    print('####################\n')

    request = requests.get(
        'https://api.thecatapi.com/v1/breeds')

    breeds = request.json()

    print('==> Raças Encontradas <==\n')
    x = 0
    numero = len(breeds)

    breed = str
    origin = str
    temperament = str
    description = str

    while (x < numero):

        breed = breeds[x]['name']
        origin = breeds[x]['origin']
        temperament = breeds[x]['temperament']
        description = breeds[x]['description']

        print('RAÇA: ' + breed)
        print('ORIGEM: ' + origin)
        print('TEMPERAMENTO: ' + temperament)
        print('DESCRIÇÃO: ' + description)

        print('\n')
        x += 1
       # print(x)

    print('---------------------------------')


if __name__ == '__main__':
    main()
