

import dao
import domain

def get_database():
    connection = dao.get_connection()
    database = connection.mydb
    return database

def get_collection():
    collection = get_database().mycoll
    return collection

def save(obj):
    men = {"name": obj.name, "surname": obj.surname}
    get_collection().save(men)

def getAll():
    List = []
    for element in get_collection().find():
        men = domain.Men(element['_id'], element['name'], element['surname'])
        List.append(men)
    return List




