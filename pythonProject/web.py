from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World!'


@app.route('/app')
def index2():
	return 'Hello app!'


@app.route('/app2')
def index3():
	return 'Hello app!'

@app.route('/app3')
def index4():
	return 'Hello app!'



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)