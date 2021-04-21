from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
USE_WEBHOOK = env.bool('USE_WEBHOOK')
USE_MONGO = env.bool('USE_MONGO')
BASE_URL = env.str('BASE_URL')
WEBHOOK_PATH = env.str('WEBHOOK_PATH')
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')
I18_DOMAIN = 'locale'
LOCALES_DIR = Path(__file__).parent.parent / 'locales'

ADMINS = env.list('ADMINS')
ALLOWED_GROUPS = env.list('ALLOWED_GROUPS')
TABLES_FOLDER = env.str('TABLES_FOLDER')

ip = {
    'db': '',
    'mongo': 'localhost',
}

database_info = {
    'host': ip['db'],
    'drivername': '',
    'user': '',
    'password': '',
    'db': '',
    'port': '5432',
}

mongo = {
    'host': ip['mongo'],
    'db_name': 'bot',
    'port': 27017
}
