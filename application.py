from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
	return 'Hi Myra, wassup this is our web app.'

personal_access_token = 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
