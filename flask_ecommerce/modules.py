from flask import Blueprint


def _factory(module_name, url_prefix):

    name = module_name
    import_name = 'flask_ecommerce.{}'.format(module_name)
    template_folder = 'templates'
    module = Blueprint(name, import_name, template_folder=template_folder, static_folder='static', url_prefix=url_prefix)
    return module

default_module = _factory('default.controllers', '/')

all_modules = (
    default_module,
)
