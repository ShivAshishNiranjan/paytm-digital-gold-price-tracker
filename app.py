__author__ = 'shiv_ashish_niranjan'
from datetime import date

import requests
import csv
import os.path


def test_paytm_digital_gold_price():
    querystring = {"channel": "WEB", "version": 2, "child_site_id": 1, "site_id": 1}
    response = requests.get("https://paytm.com/papi/v2/gold/product-portfolio", params=querystring)

    print("Status Code is {}".format(response.status_code))
    print("Response Content is {}".format(response.content))

    sell_price_per_gm = response.json()["portfolio"]["product_level"][0]["sell_price_per_gm"]
    buy_price_per_gm = response.json()["portfolio"]["product_level"][0]["price_per_gm"]

    print("Buying Price is {}".format(buy_price_per_gm))
    print("Selling Price is {}".format(sell_price_per_gm))

    csv_columns = ['Date', 'Buy_Price', 'Sell_Price']
    csv_file = "paytm_digital_gold_price.csv"

    dict_data = {'Date': date.today(), 'Buy_Price': buy_price_per_gm, 'Sell_Price': sell_price_per_gm}

    file_exists = os.path.isfile(csv_file)

    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not file_exists:
                writer.writeheader()
            writer.writerow(dict_data)
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    test_paytm_digital_gold_price()
