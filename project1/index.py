from flask import Flask, Blueprint, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/rangen')
def random_gen():
	return render_template('rangen.html')

if __name__ == '__main__':
	app.run()