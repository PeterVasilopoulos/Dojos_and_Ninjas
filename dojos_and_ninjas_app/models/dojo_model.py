from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    # Retrieving all the dojos
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

    # Adding a new dojo
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO dojos(name) 
            VALUES(%(name)s)
        """

        connectToMySQL(DATABASE).query_db(query, data)