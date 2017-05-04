import os
from flask import Flask, flash, request, redirect, render_template, url_for

from model.product import Product

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/", methods=["GET", "POST"])
def index():
    products = Product.get_all()   
    return render_template("index.html", products=products)

@app.route("/product/new", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["describtion"]
        price = request.form["price"]
        product = Product("", name, description, price)
        product.add_product()
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)