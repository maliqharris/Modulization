# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
       
    # Now we use class methods to query our database


    # CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        return  connectToMySQL('userscd').query_db(query, data)
    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('userscd').query_db(query)

        # result is list of dictionarys
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    #read one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('userscd').query_db(query, data)
        users = cls(results[0])
        return users



     #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s,email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('userscd').query_db(query, data)
    # DELETE
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s; "
        data = {'id': id}
        return connectToMySQL('userscd').query_db(query, data)
