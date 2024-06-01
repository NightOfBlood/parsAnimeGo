from bs4 import BeautifulSoup
import requests
import codecs

# #адресс сайта
# url = "https://animego.org/manga"
# #пишем хэдер, чтобы сайт не принял нас за бота
# HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
# fp = requests.get(url, headers=HEADER)

# #производим запись тегов в файл
# with open('text.html', 'w', encoding="utf_8") as file:
#     file.write(fp.text)

fileObj = codecs.open("text.html", "r", "utf_8_sig")
soup = BeautifulSoup(fileObj, 'html.parser')
fileObj.close()

main_div_tag = soup.find('div', 'mangas-grid2 position-relative')
body_all_tag = main_div_tag.find_all('div', 'animes-list-item media')
count = 0
with open('result.txt', 'w', encoding="utf-8") as file:

    for div in body_all_tag:
        #image
        image = div.find('div', 'anime-grid2-lazy lazy').get('data-original')

        # Наименование
        name = div.find('div', 'h5 font-weight-normal mb-1').text

        # count += 1
        # try:
        #     with open(f'image/{count}.jpg', 'wb') as target:
        #         a = requests.get(image)
        #         target.write(a.content)
        # except:
        #     pass

        # Жанр
        genre = div.find('span', 'anime-genre d-none d-sm-inline').find_all('a')
        genre = ', '.join([j.text for j in genre])

        # Год
        year = div.find('span', 'anime-year mb-2').text

        #Класс произведения
        for value in div.find_all('div', 'mb-2'):
            class_anime = div.find('a', 'text-link-gray text-underline').text

        # image, class, year, genre
        file.write(f' {image}, {name}, {class_anime}, {year}, {genre}  \n')