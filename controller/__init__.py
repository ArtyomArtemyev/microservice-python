from json import JSONDecoder
from http import HTTPStatus
from flask import Flask, jsonify, request, abort
from flasgger import Swagger

import service
from domain import Men
from service import getAll
import jsonpickle

app = Flask(__name__)
swaggger = Swagger(app)

@app.route('/api/v1.0/mens', methods=['GET'])
def get_mens():
    """
      Get a list of mens
      ---
      tags:
        - mens
      definitions:
        Men:
          type: object
          properties:
            _id:
              type: string
            title:
              type: string
            description:
              type: string
            done:
              type: bool
    """
    response = jsonpickle.encode(getAll())
    return response

@app.route('/api/v1.0/mens', methods=['POST'])
def add_men():
    """
      Create a new man
      ---
      tags:
        - mens
      parameters:
        - in: body
          name: body
      definitions:
        Men:
          type: object
          properties:
            _id:
              type: string
            title:
              type: string
            description:
              type: string
            done:
              type: bool
    """
    men = Men('19', request.json['name'], request.json['surname'])
    service.save(men)
    response = jsonpickle.encode(men)
    return response



if __name__ == '__main__':
    app.run(debug=True)