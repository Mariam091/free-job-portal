import hashlib

from register import *
from login import *
from getpass import getpass
import hashlib


def menu():
    print('1. Register. ')
    print('2. Log in. ')
    print('3. Exit. ')


def main():
    while True:
        menu()
        choice = int(input('Choice: '))
        if choice == 1:
            name = input('Enter your name: ')
            surname = input('Enter your surname: ')
            mail = input('Enter your mail: ')
            with open('password.txt','r') as f:
                text = f.read()
                text2 = text.splitlines()
                for i in text2:
                    if mail in i:
                        print('Already exists. Try again. ')
                        mail = input('Enter your mail: ')
            password = getpass("Please enter your password. It should include at least one uppercase letter, four lowercase letters, one digit, and one of the following symbols: ._-/;")
            user = Register(name, surname, mail, password)
            user.datasaveing()
            print('You are registered. ')

        elif choice == 2:
            mail = input('Enter your mail: ')
            password = getpass('Enter your password: ')
            pop = password.encode('utf-8')
            mypassword = hashlib.sha256(pop)
            login_attempt = Login(mail, mypassword.hexdigest())

        elif choice == 3:
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter a valid option.')


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
        again = input('You want try again? : y/n ')
        if again != 'y':
            break
