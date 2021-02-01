# coding: utf-8
import requests


def main():
    # print('#####################################')
    # print('############ The Cat API ############')
    # print('#####################################\n')

    request = requests.get(
        'https://api.thecatapi.com/v1/breeds')

    breeds = request.json()
    id_User = str
    img = str

    print('Criando e escrevendo em arquivos de texto (modo w)')
    arquivo = open('db-cats.txt', 'w')
    arquivo.write('############ The Cat API ############\n\n')

    #print('==> Raças Encontradas <==\n')
    print('Salvando 67 raças')
    arquivo.write('==> Raças Encontradas <==\n\n')
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
        print(x)
        requestImg = requests.get(
            'https://api.thecatapi.com/v1/images/search?breed_ids={0}&include_breeds=true?format=json'.format(id_User))
        img = requestImg.json()

        arquivo.write('RAÇA: ' + breed + "\n")
        arquivo.write('ORIGEM: ' + origin + "\n")
        arquivo.write('TEMPERAMENTO: ' + temperament + "\n")
        arquivo.write('DESCRIÇÃO: ' + description + "\n")

        #print('RAÇA: ' + breed)
        # print('id: ' + id_User)
        #print('ORIGEM: ' + origin)
        #print('TEMPERAMENTO: ' + temperament)
        #print('DESCRIÇÃO: ' + description)
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

        arquivo.write('IMAGEM 1: ' + pic_one + "\n")
        arquivo.write('IMAGEM 2: ' + pic_two + "\n")
        arquivo.write('IMAGEM 3: ' + pic_three + "\n")
        arquivo.write("\n")

        #print('IMAGEM 1: ' + pic_one)
        #print('IMAGEM 2: ' + pic_two)
        #print('IMAGEM 3: ' + pic_three)
        # print('\n')

    # print('-----------------------------------------------')

    #print('==> Gatos com Chapéu <==\n')
    arquivo.write('==> Gatos com Chapéu <==\n')
    hats = str
    catHats = str

    hatsRequest = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=1')
    hats = hatsRequest.json()

    catHats = hats[0]['url']
    arquivo.write('Gato de chapéu 1: ' + catHats + "\n")

    #print('Gato de chapéu 1: ' + catHats)

    hatsRequest = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=1')
    hats = hatsRequest.json()

    catHats = hats[0]['url']
    arquivo.write('Gato de chapéu 2: ' + catHats + "\n")

    #print('Gato de chapéu 2: ' + catHats)

    hatsRequest = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=1')
    hats = hatsRequest.json()

    catHats = hats[0]['url']

    arquivo.write('Gato de chapéu 3: ' + catHats + "\n")
    arquivo.write("\n")

    #print('Gato de chapéu 3: ' + catHats)

    # print('-----------------------------------------------')

    #print('==> Gatos com Óculos <==\n')
    arquivo.write('==> Gatos com Óculos <==\n')

    sunglass = str
    catSunglasses = str

    requestSunglass = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=4')
    sunglass = requestSunglass.json()

    catSunglasses = sunglass[0]['url']
    arquivo.write('Gato de óculos 1: ' + catSunglasses + "\n")
    #print('Gato de óculos 1: ' + catSunglasses)

    requestSunglass = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=4')
    sunglass = requestSunglass.json()

    catSunglasses = sunglass[0]['url']
    arquivo.write('Gato de óculos 2: ' + catSunglasses + "\n")

    #print('Gato de óculos 2: ' + catSunglasses)

    requestSunglass = requests.get(
        'https://api.thecatapi.com/v1/images/search?category_ids=4')
    sunglass = requestSunglass.json()

    catSunglasses = sunglass[0]['url']
    arquivo.write('Gato de óculos 3: ' + catSunglasses + "\n")

    #print('Gato de óculos 3: ' + catSunglasses)

    arquivo.close()

    print('Abrindo arquivo txt')

    # Lendo o arquivo criado:
    arquivo = open('db-cats.txt', 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()


if __name__ == '__main__':
    main()
