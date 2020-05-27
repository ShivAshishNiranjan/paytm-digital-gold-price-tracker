__author__ = 'shiv_ashish_niranjan'

import requests


def test_paytm_digital_gold_price():
    querystring = {"channel": "WEB", "version": 2, "child_site_id": 1, "site_id": 1}
    response = requests.get("https://paytm.com/papi/v2/gold/product-portfolio", params=querystring)

    print("Status Code is {}".format(response.status_code))
    print("Response Content is {}".format(response.content))

    sell_price_per_gm = response.json()["portfolio"]["product_level"][0]["sell_price_per_gm"]
    buy_price_per_gm = response.json()["portfolio"]["product_level"][0]["price_per_gm"]

    print("Buying Price is {}".format(buy_price_per_gm))
    print("Selling Price is {}".format(sell_price_per_gm))


if __name__ == '__main__':
    test_paytm_digital_gold_price()
