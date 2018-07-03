from flask import Flask, jsonify, request
from apiproject.model.property import Property, PropertySchema

app = Flask(__name__)

properties = []


@app.route('/properties')
def get_properties():
    return jsonify(properties)


@app.route('/properties', methods=['POST'])
def add_property():
    property = PropertySchema().load(request.get_json())
    properties.append(property.data)
    return '', 204
