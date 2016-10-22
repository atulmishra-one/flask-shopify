from flask import render_template

from flask_ecommerce.modules import product_module


@product_module.route('')
def index():
    return render_template('index.html')


@product_module.route('/<product_id>')
def detail(product_id=None):
    return render_template('detail.html')