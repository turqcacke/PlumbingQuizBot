from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
USE_WEBHOOK = env.bool('USE_WEBHOOK')
USE_REDIS = env.bool('USE_REDIS')
BASE_URL = env.str('BASE_URL')
WEBHOOK_PATH = env.str('WEBHOOK_PATH')
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')

ADMINS = env.list('ADMINS')

ip = {
    'db': '',
    'redis': '',
}

database_info = {
    'host': ip['db'],
    'drivername': '',
    'user': '',
    'password': '',
    'db': '',
    'port': '5432',
}

redis = {
    'host': ip['redis'],
    'password': ''
}
