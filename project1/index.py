from flask import Flask, Blueprint, render_template
from forms import generate_rand_int
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/rangen', methods=['GET', 'POST'])
def random_gen():
	random_int = 0
	form = generate_rand_int()
	print("test1")
	if form.is_submitted():
		print("test")
		random_int = random.randint(int(form.a.data), int(form.b.data))
	return render_template('rangen.html', random_int=random_int, form=form)


if __name__ == '__main__':
	app.run()