from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT * 
            FROM dojos;
        """
        results = connectToMySQL('ninjas_and_dojos_original').query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(name)s;"""
        
        return connectToMySQL('ninjas_and_dojos_original').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * 
            FROM dojos
            WHERE id = %(id)s;"""
            
        result = connectToMySQL('ninjas_and_dojos_original').query_db(query, data)
        if len(result) == 0:
            return False
        return cls(result[0])

    @classmethod
    def get_ninjas(cls, data):
        query = """
            SELECT * 
            FROM ninjas 
            WHERE dojo_id = %(id)s;
        """
        results = connectToMySQL('ninjas_and_dojos_original').query_db(query, data)
        ninjas = []
        for result in results:
            ninjas.append(Ninja(result))
        return ninjas


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s;
        """
        return connectToMySQL('ninjas_and_dojos_original').query_db(query, data)

