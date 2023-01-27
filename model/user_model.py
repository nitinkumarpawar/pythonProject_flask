import mysql.connector


class user_model():
    def __init__(self):
        try:
            con = mysql.connector.connect(host="localhost", user="admin", password="Password@123",
                                          database="flask_demo")
            print("Connection Succesfully established")
        except:
            print("Some error")

    def user_signup_model(self):
        return "This is user signup model1"

    def user_getall_model(self):
        return "This is user getall model1"
