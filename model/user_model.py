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
            return {"users": result}
        else:
            return {"message": "No data found"}

    def user_addone_model(self, data):
        # self.cur.execute("SELECT * FROM users")
        self.cur.execute(
            f"INSERT INTO users(name, email, phone ,role ,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data)
        return {"message": "User created successfully"}

    def user_update_model(self, data):
        self.cur.execute(
            f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id='{data['id']}'")
        print(data)
        if self.cur.rowcount > 0:
            return {"message": "Data updated successfully"}
        else:
            return {"message": "Nothing to update"}

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        print(id)
        if self.cur.rowcount > 0:
            return {"message": "User deleted successfully"}
        else:
            return {"message": "Nothing to delete"}
