import requests
import logging

success_logger = logging.getLogger('successful_connections')
success_logger.setLevel(level=logging.INFO)
success_handler = logging.FileHandler('successful_connections.log', mode='w')
success_formatter = logging.Formatter('%(levelname)s: %(message)s')
success_handler.setFormatter(success_formatter)
success_logger.addHandler(success_handler)


bad_logger = logging.getLogger('bad_connections')
bad_logger.setLevel(level=logging.INFO)
bad_handler = logging.FileHandler('bad_connections.log', mode='w')
bad_formatter = logging.Formatter('%(levelname)s: %(message)s')
bad_handler.setFormatter(bad_formatter)
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('blocked_connections')
blocked_logger.setLevel(level=logging.INFO)
blocked_handler = logging.FileHandler('blocked_connections.log', mode='w')
blocked_formatter = logging.Formatter('%(levelname)s: %(message)s')
blocked_handler.setFormatter(blocked_formatter)
blocked_logger.addHandler(blocked_handler)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = requests.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f'{site}, response - {response.status_code}')
        elif response.status_code > 200:
            bad_logger.warning(f'{site}, response - {response.status_code}')
    except requests.exceptions.ConnectTimeout:
        blocked_logger.error(f'{site}, NO CONNECTION')
    except requests.exceptions.ReadTimeout:
        blocked_logger.error(f'{site}, NO CONNECTION')

