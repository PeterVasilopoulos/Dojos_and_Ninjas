from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app import DATABASE

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
    
    # Createing a new ninja
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO ninjas(first_name, last_name, age, dojo_id) 
            VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        """

        connectToMySQL(DATABASE).query_db(query, data)