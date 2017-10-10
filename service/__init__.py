import dao

def get_database():
    connection = dao.get_connection()
    database = connection.mydb
    return database

def get_collection():
    collection = get_database().mycoll
    return collection

def save(obj):
    get_collection().save(obj)

def getAll():
    List = []
    for men in get_collection().find():
        List.append(men)
        return List





