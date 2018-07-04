from flask import Flask, jsonify, request
from apiproject.model.property import PropertySchema

app = Flask(__name__)

properties = []


@app.route('/properties', methods=['GET'])
def get_properties():
    schema = PropertySchema()
    result = schema.dump(properties)
    return jsonify(result)


@app.route('/properties', methods=['POST'])
def add_property():
    property = PropertySchema().load(request.get_json())
    properties.append(property)
    return '', 204
