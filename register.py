from validname import Validname
from validsurname import ValidSurname
from validmail import ValidMail
from validpassword import ValidPassword

import os


class Register:
    name = Validname()
    surname = ValidSurname()
    mail = ValidMail()
    password = ValidPassword()

    def __init__(self, name, surname, mail, password):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password

    def datasaveing(self):
        path = "password.txt"
        check = os.path.isfile(path)
        if check:
            with open('password.txt', 'a') as f:
                f.write(f'{self.name},{self.surname},{self.mail},{self.password}\n')



