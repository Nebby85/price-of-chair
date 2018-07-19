import os

__author__ = 'nebby85'


DEBUG = True
ADMINS = frozenset([os.environ.get('ADMIN_EMAIL')])
SITE_URL = "https://pricing-service-nebby85.herokuapp.com/"
