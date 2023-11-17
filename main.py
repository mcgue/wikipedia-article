# Obtains a random wikipedia article and prints it out

# import necessary modules
from bs4 import BeautifulSoup
import requests




def print_article(title, url):
    print(f'The article is called: {title}')
    print(f'The url is: {url}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )

    # verify getting valid response back and proceed if yes
    if (response.status_code) == 200:

        # get title
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="firstHeading")

        # Print title and url
        print_article(title.string, response.url)

    # try later if not working
    else:
        print('Try again later')
