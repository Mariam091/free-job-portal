class Validname:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not 4 <= len(value) <= 20:
            raise ValueError('Name length must be between 4 and 20 characters. ')
        if not value[0].isalpha():
            raise ValueError('Name must start with an alphabetic character. ')
        if ' ' in value:
            raise ValueError('Name cannot contain spaces. ')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
