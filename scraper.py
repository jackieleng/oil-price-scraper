import requests
import bs4
from bs4 import BeautifulSoup


PRICES_URL = "https://oilprice.com/oil-price-charts"


def get_rows(table: bs4.element.Tag):
    thead, tbody = table.children
    rows = tbody.find_all('tr')
    return rows


def parse_row(row: bs4.element.Tag) -> dict:
    cells = row.find_all('td')
    name = cells[1]
    last_price = cells[2]
    return {
        "name": name.text,
        "price": last_price.text,
    }


def main():
    response = requests.get(PRICES_URL)

    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all("table")
    rows = get_rows(tables[0])
    for row in rows:
        data = parse_row(row)
        print(data)


if __name__ == '__main__':
    main()
