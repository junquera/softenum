class Softenummeta(type):

    def __new__(metacls, cls, bases, classdict, **kwargs):       
        
        # Finding base __new__
        __new__ = classdict.get('__new__')
        
        if __new__ is None:
            for base in bases:
                __new__ = getattr(base, "__new__")
                if __new__:
                    break

        if __new__ is None:
            __new__ = object.__new__

        # 
        target_bases = bases + (object,)
        forbidden = set(("__module__", "__qualname__",))
        for base in target_bases:
            for key in base.__dict__:
                forbidden.add(key)

        # Creating response
        enumerated = dict(classdict)
        for key in forbidden:
            if key in enumerated:
                del enumerated[key]

        enum_class = super().__new__(metacls, cls, bases, classdict, **kwargs)
        
        keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return','try', 'while', 'with', 'yield', '_', 'case', 'match']

        for element in enumerated:

            # if not re.match(r"^[a-z][a-z0-9_]*", element):
            if not element.isidentifier():
                raise Exception(f"Invalid enumerated value {element}: not identifier")
            if element in keywords:
                raise Exception(f"Invalid enumerated value {element}: kwlist")
                
            value = enumerated[element]
            if not isinstance(value, tuple):
                args = (value, )
            else:
                args = value

            enum_member = __new__(enum_class, *args)
            enum_member._name_ = element
            enum_member._value_ = args
            enum_member.__objclass__ = enum_class
            enum_member.__init__(*args)

            setattr(enum_class, element, enum_member)

        return enum_class # super().__new__(metacls, cls, bases, classdict, **kwargs)

    def __repr__(cls):
        return "<softenum %r>" % cls.__name__


class Softenum(metaclass=Softenummeta):

    def __new__(cls, value):
        
        if type(value) is cls:
            return value
        else:
            return cls(value)

    def __repr__(self):
        return "<%s.%s: %r>" % (
                self.__class__.__name__, self._name_, self._value_)

    def __str__(self):
        return "%s.%s" % (self.__class__.__name__, self._name_)
