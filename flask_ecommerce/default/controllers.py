from flask import render_template

from flask_ecommerce.modules import default_module


@default_module.route('')
def index():
    return render_template('index.html')