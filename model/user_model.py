import json

import mysql.connector


class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="admin", password="Password@123",
                                               database="flask_demo")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Succesfully established")
        except:
            print("Some error")

    def user_signup_model(self):
        return "This is user signup model1"

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            return json.dumps(result)
        else:
            return "No data found"

    def user_addone_model(self, data):
        # self.cur.execute("SELECT * FROM users")
        self.cur.execute(
            f"INSERT INTO users(name, email, phone ,role ,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data)
        return "User created successfully"
