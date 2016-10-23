from flask import render_template
from flask_ecommerce.modules import admin_module


@admin_module.route('')
def index():
    return render_template('default/index.html')