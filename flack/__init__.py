import os
from flask import Flask
app = Flask(__name__)



app.config['SECRET_KEY'] = 'iioioiiojioi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_ADDRESS')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

from flack import routes