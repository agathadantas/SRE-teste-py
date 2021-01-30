# coding: utf-8
import requests


def main():
    print('####################')
    print('### The Cat API ####')
    print('####################\n')

    request = requests.get(
        'https://api.thecatapi.com/v1/breeds')

    breeds = request.json()
    id_User = str
    img = str

    print('==> Raças Encontradas <==\n')
    x = 0
    numero = len(breeds)

    breed = str
    origin = str
    temperament = str
    description = str
    pic_one = str
    pic_two = str
    pic_three = str
    num = 0
    while (x < numero):
        id_User = breeds[x]['id']
        breed = breeds[x]['name']
        origin = breeds[x]['origin']
        temperament = breeds[x]['temperament']
        description = breeds[x]['description']

        x += 1

        requestImg = requests.get(
            'https://api.thecatapi.com/v1/images/search?breed_ids={0}&include_breeds=true?format=json'.format(id_User))
        img = requestImg.json()

        print('RAÇA: ' + breed)
        #print('id: ' + id_User)
        print('ORIGEM: ' + origin)
        print('TEMPERAMENTO: ' + temperament)
        print('DESCRIÇÃO: ' + description)
        if (num < 3):

            pic_one = img[0]['url']
            num += 1

            requestImg = requests.get(
                'https://api.thecatapi.com/v1/images/search?breed_ids={0}&include_breeds=true?format=json'.format(id_User))
            img = requestImg.json()

            pic_two = img[0]['url']
            num += 1

            requestImg = requests.get(
                'https://api.thecatapi.com/v1/images/search?breed_ids={0}&include_breeds=true?format=json'.format(id_User))
            img = requestImg.json()
            pic_three = img[0]['url']
            num = 0

        print('IMAGENS: ' + pic_one)
        print('IMAGENS: ' + pic_two)
        print('IMAGENS: ' + pic_three)
        print('\n')

    # print(x)

    print('---------------------------------')


if __name__ == '__main__':
    main()