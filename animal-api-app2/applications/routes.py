from applications import app
from flask import Response, request
import random 

@app.route('/getAnimal', methods=['GET'])
def getAnimal():
    animals=['Dog','Cat','Mouse','Horse','Cow','Sheep']
    animal=random.choice(animals)
    return Response(animal, mimetype="text/plain")

@app.route('getNoise', methods=['POST'])
def getNoise():
    animal = request.data.decode('utf-8')
    if animal == "Dog":
        noise = "Woof!"
    elif animal == "Cat":
        noise = "Meow!"
    elif animal == "Mouse":
        noise = "squeak"
    elif animal == "Horse":
        noise = "Neigh"
    elif animal == "Cow":
        noise = "Moo!"
    elif animal == "Sheep":
        noise = "Baa!"
    else:
        noise = "Unkown!"
    
    return Response(noise, mimetype='text/plain')

