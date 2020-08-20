from applications import app
from flask import render_template
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get/animal', methods=['GET', 'POST'])
def animal():
    animal = requests.get('http://app2:5001/getAnimal')
    noise = requests.post('http://app2:5001/getNoise', data=animal.text)
    return render_template('result.html', animal=animal.text, noise=noise.text)


