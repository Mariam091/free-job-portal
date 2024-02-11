import hashlib

class ValidPassword:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if 8 <= len(value) <= 12 and any(sym in '._-/;' for sym in value) and any(sym.isupper() for sym in value) and any(sym.isdigit() for sym in value) and  any(sym.islower() for sym in value):
            pop = value.encode('utf-8')
            myhash = hashlib.sha256(pop)
            instance.__dict__[self.name] = myhash.hexdigest()
        else:
            raise ValueError('Invalid password. ')
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
