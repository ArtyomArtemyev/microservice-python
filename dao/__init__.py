import pymongo

def get_connection():
    connection = pymongo.Connection('localhost', 27017)
    return connection


