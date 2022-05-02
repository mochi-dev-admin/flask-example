from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
	return 'Hi Myra, wassup this is our web app.'
