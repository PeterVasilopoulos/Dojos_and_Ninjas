from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = ['name']

    @classmethod 
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL(DATABASE).query_db(query)

        dojos = []

        if results:
            for dojo in results:
                new_dojo = cls(dojo)
                dojos.append(new_dojo)

        return dojos