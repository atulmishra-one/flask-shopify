from flask_ecommerce.modules import admin_module


@admin_module.route('')
def index():
    return 'Pp'