from flask_ecommerce.application import initialize_app
from flask_ecommerce.config.local import LocalConfig


flask_ecommerce = initialize_app(LocalConfig)

flask_ecommerce.run(threaded=True, port=80)
