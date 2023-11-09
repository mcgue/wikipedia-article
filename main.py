# Obtains a random wikipedia article and prints it out

from bs4 import BeautifulSoup
import requests




def print_article(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_article('PyCharm')
