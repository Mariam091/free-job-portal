import hashlib

from validname import Validname
from validsurname import ValidSurname
from validmail import ValidMail
from validpassword import ValidPassword
from getpass import getpass


class Login:
    set_name = Validname()
    set_surname = ValidSurname()
    set_mail = ValidMail()
    set_password = ValidPassword()

    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
        self.transfer()

    def transfer(self):
        with open('password.txt', 'r') as file:
            text = file.read()
            self.foo(text, self.mail, self.password)

    def foo(self, datas, mail, password):
        ls = datas.splitlines()
        for line in ls:
            if mail in line:
                res = line.split(',')
                if password == res[-1]:
                    print('Successfully logged in. ')
                    self.menu()

    def menu(self):
        update_line = []
        print('1. Set name. ')
        print('2. Set surname. ')
        print('3. Set mail. ')
        print('4. Set password. ')
        print('5. Back menu. ')
        while True:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                new_value = input(f'Enter new {"Name " if choice == 1 else "Surname " if choice == 2 else "Mail "}: ')
                if choice == 1:
                    self.set_name = new_value
                elif choice == 2:
                    self.set_surname = new_value
                elif choice == 3:
                    self.set_mail = new_value
            elif choice == 4:
                value = getpass('Enter new password. ')
                self.set_password = value
                pop = value.encode('utf-8')
                myvalue = hashlib.sha256(pop)
                new_value = myvalue.hexdigest()
            elif choice == 5:
                break

            with open("password.txt", "r") as f:
                for line in f:
                    part = line.strip().split(",")
                    if self.mail in part:
                        part[choice - 1] = new_value
                        print('Changing. ')
                        update_line.append(",".join(part))
                    else:
                        update_line.append(line.strip())

                with open("password.txt", "w") as f:
                    f.writelines("\n".join(update_line)+"\n")
                break
