from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app.models.ninja_model import Ninja

from dojos_and_ninjas_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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

    # Get dojo info
    @classmethod 
    def get_dojo_info(cls, id):
        data = {
            'id' : id
        }

        query = """
            SELECT * FROM dojos WHERE id = %(id)s
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        return results

    # Getting all ninjas from a single dojo
    @classmethod
    def get_all_ninjas_from_dojo(cls, id):
        # Run query and get results
        data = {
            'id' : id
        }

        query = """
            SELECT * FROM dojos JOIN ninjas ON 
            dojos.id = ninjas.dojo_id 
            WHERE ninjas.dojo_id = %(id)s;
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        # Separate out the data and create classes
        ninjas = []

        if results:
            for row in results:
                dojo = cls(row)

                ninja_data = {
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'dojo_id' : row['dojo_id'],
                    'created_at' : row['ninjas.created_at'],
                    'updated_at' : row['ninjas.updated_at']
                }

                ninja = Ninja(ninja_data)

                ninja.dojo = dojo

                ninjas.append(ninja)

        return ninjas