import re


class ValidMail:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Invalid mail.  ')

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]




