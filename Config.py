import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ca_file = os.getenv('MYSQL_SSL_CA', 'ca.pem')
ca_path = ca_file if os.path.isabs(ca_file) else os.path.join(BASE_DIR, ca_file)

class Config:

    MYSQL_HOST      = os.getenv('MYSQL_HOST')
    MYSQL_USER      = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD  = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB        = os.getenv('MYSQL_DB')
    MYSQL_PORT      = int(os.getenv('MYSQL_PORT', 3306))

    # Opciones SSL para Aiven / bases de datos remotas
    MYSQL_CUSTOM_OPTIONS = {}
    if os.path.exists(ca_path) and os.getenv('MYSQL_HOST', '') not in ('localhost', '127.0.0.1'):
        MYSQL_CUSTOM_OPTIONS['ssl'] = {'ca': ca_path}