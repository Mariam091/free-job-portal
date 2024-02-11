class ValidSurname:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not 4 <= len(value) <= 30:
            raise ValueError('Surname lenght must be between 4 anc 30 characters. ')
        for char in value:
            if not char.isalpha():
                raise ValueError('Surname must contain only alphabetic characters.  ')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
