import re
from unicodedata import category
from unittest import result
from flask import Flask
import json
from config import me, hello
from mock_data import catalog

app = Flask("Server")


@app.get("/")
def home():
    return "Hello world!"


@app.get("/test")
def test():
    return "This is the final test!"


@app.get("/about")
def about():
    return "It's me, Matthew!"


#######################################
# API ENDPOINTS
# JSON
#######################################


@app.get("/api/version")
def version():
    v = {
        "version": "1.0.0",
        "build": 35,
        "name": "chocolate",
        "developer": me
    }

    hello()

    return json.dumps(v)


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


@app.get("/api/products/count")
def total_count():
    return json.dumps(len(catalog))


# get /apt/products/total
# return the sum of all the prices
@app.get("/api/products/total")
def total_price():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)


@app.get("/api/catalog/lower/<ammount>")
def lower_than(ammount):
    results = []
    for prod in catalog:
        if prod["price"] < float(ammount):
            results.append(prod)

    return json.dumps(results)


@app.get("/api/category/unique")
def unique_cats():
    results = []
    for prod in catalog:
        category = prod["category"]
        if not category in results:
            results.append(prod["category"])

    return json.dumps(results)


@app.get("/api/test/colors")
def unique_colors():
    colors = ["red", 'blue', "Pink", "yelloW", "Red",
              "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    results = []
    for color in colors:
        color = color.lower()
        if not color in results:
            results.append(color)

    return json.dumps(results)


@app.get("/api/test/count/<color>")
def count_color(color):
    color = color.lower()
    colors = ["red", 'blue', "Pink", "yelloW", "Red",
              "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    count = 0
    for item in colors:
        if color == item.lower():
            count += 1

    return json.dumps(count)


app.run(port=5001, debug=True)
