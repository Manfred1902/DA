import pyrebase  # pyrebase 4 is needed!
import re
from kivy.logger import Logger
from kivymd.app import MDApp


class Firebase:
    def __init__(self) -> None:
        self.config = {
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
        self.pb = pyrebase.initialize_app(self.config)
        Logger.info('Firebase: Initialized')

    def signup(self, email: str, password_1: str, password_2: str) -> None:
        if not re.match(password_1, password_2):
            Logger.error('Passwords do not match')
            return

        try:
            response = self.pb.auth().create_user(email, password_1)

            MDApp.get_running_app().root.ids["signup_screen"].ids[
                "signup_screen"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"

            Logger.debug(response)

        # https://code.whatever.social/questions/30442236/how-to-prevent-too-broad-exception-in-this-case
        # TLDR: is used to prevent PEP8
        except (Exception,) as e:
            Logger.warning(e)

    def login(self, email: str, password: str) -> None:
        if email is None or password is None:
            Logger.error('Email or Password is empty! ')
            return

        try:
            # response gets the user data
            response = self.pb.auth().sign_in_with_email_and_password(email, password)

            # user can only access some pages only if he is registered
            if response["registered"]:
                self.user = response

                Logger.debug(self.user)

                MDApp.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                MDApp.get_running_app().change_screen("home_screen")
                MDApp.get_running_app().root.ids["home_screen"].ids[
                    "passing_email"].text = "[b]%s[/b]" % email

        except (Exception,) as e:
            MDApp.get_running_app().root.ids["login_screen"].ids[
                "login_message"].text = "[b]Invalid Email or Password[/b]"
            Logger.warning(e)

    def logout(self) -> None:
        try:
            # auth().logout is not working!
            self.pb.auth().current_user = None
            self.user = None

            MDApp.get_running_app().change_screen("login_screen")

            Logger.debug('User: ' + str(self.user))

        except (Exception,) as e:
            return Logger.warning(e)

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
            return Logger.warning(e)

    def getDroneData(self) -> None:
        try:
            response = self.pb.database().child("users").child(self.user["localId"])

            Logger.debug(response)

        except (Exception,) as e:
            return Logger.warning(e)

    def verifyEmail(self) -> None:
        try:
            response = self.pb.auth().send_verify_email(self.user["idToken"])

            Logger.debug(response)

        except (Exception,) as e:
            return Logger.warning(e)

    def getUserInfo(self) -> None:
        try:
            response = self.pb.auth().get_user()

            Logger.debug(response)

        except (Exception,) as e:
            return Logger.warning(e)

    def refreshToken(self) -> None:
        try:
            response = self.pb.auth().refresh_token()

            Logger.debug(response)

        except (Exception,) as e:
            return Logger.warning(e)
