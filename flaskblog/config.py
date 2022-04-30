import os
import json

with open('/etc/config.json') as config_file:
    config_data = json.load(config_file)


class Config():
    SECRET_KEY = config_data.get('BLOG_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config_data.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config_data.get('EMAIL_USER')
    MAIL_PASSWORD = config_data.get('EMAIL_PASS')
