from flask import Flask, Blueprint, render_template, request, redirect, url_for
from forms import generate_rand_int
import random
import os
import cv2

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/rangen', methods=['GET', 'POST'])
def random_gen():
	random_int = 0
	form = generate_rand_int()
	if form.is_submitted():
		random_int = random.randint(int(form.a.data), int(form.b.data))
	return render_template('rangen.html', random_int=random_int, form=form)

@app.route('/upload_image')
def upload_form():
	return render_template('upload_image.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
	if request.method == 'POST':
		if request.files:
			image = request.files['file']
			filename = image.filename
			image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print("TESTSETTESTSETASDFASET")
			img = cv2.imread(f'static/uploads/{filename}')
			print(img)
			img = cv2.circle(img, (500, 500), 200, (150, 150, 150))
			cv2.imwrite(f'static/uploads/{filename}_test', img)
			return render_template('upload_image.html', filename=filename+'_test')

if __name__ == '__main__':
	app.run()