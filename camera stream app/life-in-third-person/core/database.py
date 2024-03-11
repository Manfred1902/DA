import re
from datetime import datetime

import pyrebase  # pyrebase 4 is needed!
from kivy.logger import Logger
from kivymd.app import MDApp


class Firebase:
    def __init__(self) -> None:
        config = {
            "apiKey": "AIzaSyBowz9TW7OzskqlDV4OAecVofaOVq9OrO4",
            "authDomain": "life-in-third-person.firebaseapp.com",
            "databaseURL": "https://life-in-third-person-default-rtdb.europe-west1.firebasedatabase.app",
            "projectId": "life-in-third-person",
            "storageBucket": "life-in-third-person.appspot.com",
            "messagingSenderId": "403469711752",
            "appId": "1:403469711752:web:643d471e6c19cd869a223d",
            "measurementId": "G-MH9J5Q0QES"
        }
        self.user = None
        self.pb = pyrebase.initialize_app(config)
        Logger.info('Firebase: Initialized')

    def signup(self, email: str, password_1: str, password_2: str) -> None:
        if not re.match(password_1, password_2):
            Logger.error('Passwords do not match')
            return

        try:
            response = self.pb.auth().create_user_with_email_and_password(email, password_1)

            user = self.pb.auth().get_account_info(response["idToken"])

            if user["users"][0]["emailVerified"] is False:
                verify = self.pb.auth().send_email_verification(response["idToken"])
                MDApp.get_running_app().root.ids["signup_screen"].ids[
                    "signup_message"].text = "[b][color=#FF0000]An Email was sent to your account. [/color][/b]"
            else:
                MDApp.get_running_app().root.ids["signup_screen"].ids[
                    "signup_message"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"
                MDApp.get_running_app().change_screen("home_screen")

            Logger.debug(response)

        # https://code.whatever.social/questions/30442236/how-to-prevent-too-broad-exception-in-this-case
        except (Exception,) as e:
            Logger.error(e)

    def login(self, email: str, password: str) -> None:
        if email is None or password is None:
            Logger.error('Firebase: Email or Password is empty! ')
            return

        try:
            # response gets the user data
            response = self.pb.auth().sign_in_with_email_and_password(email, password)

            # user can only access some pages only if he is registered
            if response["registered"]:
                self.user = response

                MDApp.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                MDApp.get_running_app().change_screen("home_screen")
                MDApp.get_running_app().root.ids["home_screen"].ids[
                    "passing_email"].text = "[b]%s[/b]" % email

        except (Exception,) as e:
            MDApp.get_running_app().root.ids["login_screen"].ids[
                "login_message"].text = "[b]Invalid Email or Password[/b]"
            Logger.error(e)

    def logout(self) -> None:
        try:
            # auth().logout is not working!
            self.pb.auth().current_user = None
            self.user = None

            MDApp.get_running_app().change_screen("login_screen")

            Logger.debug('User: ' + str(self.user))

        except (Exception,) as e:
            Logger.error(e)

    def changePassword(self, email: str) -> None:
        if email is None:
            Logger.error('Email cannot be empty')
            return

        try:
            response = self.pb.auth().send_password_reset_email(email)

            MDApp.get_running_app().root.ids["forgot_password_screen"].ids[
                "forgot_message"].text = "[b]Thanks! Please check your email .[/b]"

            Logger.debug(response)

        except (Exception,) as e:
            MDApp.get_running_app().root.ids["forgot_password_screen"].ids[
                "forgot_message"].text = "[b][color=#FF0000]Please Enter Correct Email![/color][/b]"
            Logger.error(e)

    def getDroneData(self) -> None:
        try:
            response = self.pb.database().child("users").child(self.user["localId"]).get(self.user["idToken"])

            for user_data in response:
                Logger.info(user_data)

        except (Exception,) as e:
            Logger.error(e)

    def verifyEmail(self) -> None:
        try:
            response = self.pb.auth().send_verify_email(self.user["idToken"])

            Logger.debug(response)

        except (Exception,) as e:
            Logger.error(e)

    def refreshToken(self) -> None:
        try:
            response = self.pb.auth().refresh_token()

            Logger.debug(response)

        except (Exception,) as e:
            Logger.error(e)

    def send_data(self, battery, flight_time, avg_temp, barometer) -> None:
        try:
            self.pb.database().child("users").child(self.user["localId"]).push({
                "timestamp": datetime.now().timestamp(),
                "battery": battery,
                "flightTime": flight_time,
                "avgTemp": avg_temp,
                "barometer": barometer
            }, self.user["idToken"])

            Logger.debug("Firebase: Send drone data to firebase. ")

        except (Exception,) as e:
            Logger.error(e)

    def save_picture(self, filename) -> None:
        try:
            self.pb.storage().child("pictures").child(self.user["localId"]).put(filename, self.user["idToken"])

            Logger.info("Firebase: Picture")

        except (Exception,) as e:
            Logger.error(e)
