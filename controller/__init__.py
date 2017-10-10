import service

# For inishialize database
import pymongo

from flask import Flask, jsonify
from flasgger import Swagger
from http import HTTPStatus

app = Flask(__name__)
swaggger = Swagger(app)

@app.route('/mens')
def getAll():
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
         name:
           type: string
         surname:
           type: string
   responses:
     200:
       description: Returns a list of mens
       schema:
         id: Mens
         type: object
         properties:
           users:
             type: array
             items:
               $ref: '#/definitions/Men'
       examples:
         users: [{'_id': '1', 'name': 'Russel', 'surname': 'Allen'}]
           """
    return jsonify(service.getAll()), HTTPStatus.OK

if __name__ == '__main__':

    # Inishialize database
    # conn = pymongo.Connection('localhost', 27017)
    # db = conn.mydb
    # coll = db.mycoll
    # doc = {"name": "Петр", "surname": "Иванов"}
    # coll.save(doc)

    app.run()
