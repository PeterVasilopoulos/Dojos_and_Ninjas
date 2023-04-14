from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = ['name']

    