from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Create a simple dictionary for storing data
items = []

# Define the resource class for working with the API
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return jsonify(item)
        return {'message': 'Item not found'}, 404

    def post(self):
        global items
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        items.append(new_item)
        return jsonify(new_item)

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}

# Routing for the resource
api.add_resource(Item, '/item/<string:name>', '/item')

if __name__ == '__main__':
    app.run(debug=True)