
from dotenv import load_dotenv

load_dotenv()
import os

# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


#Fauna
FAUNA_ADMIN_SECRET=os.getenv("FAUNA_ADMIN_SECRET")
FAUNA_SERVER_SECRET=os.getenv("FAUNA_SERVER_SECRET")
