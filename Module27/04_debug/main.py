def debug(function):
    def wrapper(*args, **kwargs):
        print("Вызывается {}({})".format(
            function.__name__,
            ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{k}=\"{v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )
        ))
        result = function(*args, **kwargs)
        print("'{}' вернула значение '{}'".format(
            function.__name__, result
        ))
        print(result)
        print()
        return result
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
