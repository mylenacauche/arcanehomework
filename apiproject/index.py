from flask import jsonify, request, url_for
from flask_api import FlaskAPI, status, exceptions

# from apiproject.model.property import PropertySchema
from apiproject.model.property import property_repr, properties

app = FlaskAPI(__name__)

@app.route('/properties', methods=['GET', 'POST'])
def properties_list():
    if request.method == 'POST':
        property = str(request.json)
        max(properties.keys()) + 1 if id else 0
        properties[id] = property
        return property_repr(id), status.HTTP_201_CREATED
    return [property_repr(id) for id in sorted(properties.keys())]



