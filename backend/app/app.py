from flask import Flask, jsonify, request 
# Flask initializes app and runs server
# jsonify converts Python data structures into JSON
# request holds details of incoming HTTP requests

app = Flask(__name__) #instantiates Flask app

allDevilFruits = []

#root endpoint
@app.route('/') #decorator
def home(): 
    return "Welcome to the DevilDex"

#retrieves all the devil fruit
@app.route('/api/alldevilfruits', methods=['GET'])
def get_allDevilFruits():
    return jsonify(allDevilFruits)

#retrieves single devil fruit using id
@app.route('/api/alldevilfruits/<int:id>', methods=['GET'])
def get_devilFruit(id):
    devilFruit = next((f for f in allDevilFruits if f["id"] == id), None) #returns devilFruit w/ matching the id or None if nothing matches
    
    if devilFruit:
        return jsonify(devilFruit)
    else:
        return jsonify({"error": "Devil Fruit not found"}), 404

#adds a devil fruit to master list of devil fruits
@app.route('/api/alldevilFruits', methods=['POST']) 
def add_devilFruit():
    new_devilFruit = request.get_json() #changes incoming request data into JSON format
    
    if not new_devilFruit or 'name' not in new_devilFruit: 
        return jsonify({'error': 'Invalid data'}), 400 #returns error if new_devilFruit isn't in JSON or missing its name
    
    new_devilFruit["id"] = len(allDevilFruits) + 1 #adds id based on list length by adding 1 to current length
    allDevilFruits.append(new_devilFruit) #adds new devil fruit to allDevilFruits list
    return jsonify(new_devilFruit), 201

#deletes a single devil fruit based on id
@app.route('/api/alldevilFruits/<int:id>', methods=['DELETE'])
def delete_devilFruit(id):
    global allDevilFruits
    allDevilFruits = [f for f in allDevilFruits if f["id"] != id] #filter out the devil fruit based on its id
    return jsonify({"message": "Fruit deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True) #checks if app is being being executed directly or imported as a module into another script


#Decorators wrap another function to extend the behaviour of the wrapped function w/o permanently changing it.
#def indicate function definition
#global keyword declares that variable inside a function is defined outside the function; allows functions to be modified directly and enables management of shared state across functions--should be used sparingly
#generator expressions iterator over each item in a collection and returns 1s item w/ matching specification or None if not
# None is a special keyword in Python that represents the absence of a value or a null value, and it’s always spelled with a capital N. Using lowercase (none) would result in an error because Python would treat it as an undefined variable or name.