import functools
from bs4 import BeautifulSoup as BSoup
import requests as req


def console_out(link):
    print(link)


def file_out(file, link):
    file.write(link + '\n')


def main():
    output_type = input(
        'Вывод в файл - введите 1\n'
        'Вывод в консоль - введите 2\n'
    )
    if output_type == '1':
        out = file_out
        file = open('output.txt', 'w')
        out = functools.partial(out, file=file)
    elif output_type == '2':
        out = console_out
    else:
        print('Неверный ввод!\n'
              'Будет использован вывод в консоль')
        out = console_out

    # link = input()
    link = 'https://natasha.github.io/'
    get_links(link, out, True)


def get_links(link, out, first=None):
    response = req.get(link)
    soup = BSoup(response.text, 'lxml')
    for el in soup.findAll('a'):
        try:
            href = el['href']
        except KeyError:
            continue
        if href.startswith('http') or href.startswith('https'):
            out(link=href)
            if first:
                get_links(href, out)


if __name__ == '__main__':
    main()
