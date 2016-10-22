from flask_ecommerce.application import initialize_app
from flask_ecommerce.config import local


flask_ecommerce = initialize_app(local)

flask_ecommerce.run(threaded=True, port=80)
