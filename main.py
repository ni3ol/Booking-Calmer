import requests
from bs4 import BeautifulSoup


URL = 'https://booking.com/'


def fetch_source():
    response = requests.get(URL)
    return response.text


def parse_deals(source):
    soup = BeautifulSoup(source, 'html.parser')
    deals = soup.find_all('div', class_='new_product_block')

    for deal in deals:
        name = deal.find(class_='shortname').text
        retail_price = int(deal.find(class_='retail').text.lstrip('Retail: R').replace(',', ''))
        selling_price = int(deal.find(class_='selling').text.lstrip('R').replace(',', ''))
        yield {'name': name, 'retail_price': retail_price, 'selling_price': selling_price}


def build_index(deals):
    return {}


def load_searches():
    return [{'email': 'nvojacek@gmail.com', 'name': 'fitness watches', 'query': 'brand:Garmin description:watch'}]


def search_deals(index, searches):
    return [{
        'email': 'nvojacek@gmail.com', 'name': 'fitness watches', 'query': 'brand:Garmin description:watch',
        'results': [{'name': 'a', 'description': 'b', 'retail_price': 0, 'sale_price': 0 }]
    }]


def send_emails(matches):
    pass


def main():
    source = fetch_source()
    deals = parse_deals(source)
    index = build_index(deals)
    searches = load_searches()
    matches = search_deals(index, searches)
    send_emails(matches)


if __name__ == '__main__':
    main()
