# Obtains a random wikipedia article and prints it out

from bs4 import BeautifulSoup
import requests




def print_article(article):
    print(f'Hi, {article}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Web_scraping",
    )
    # should print 200
    print(response.status_code)

    # Print link to article
    print_article('here it is')
