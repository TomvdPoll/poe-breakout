def add_some_numbers(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
