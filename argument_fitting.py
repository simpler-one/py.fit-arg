import inspect


def to_varargs(func):
    """
    Convert to a variable args function
    :param callable func: function
    """
    spec = inspect.getfullargspec(func)
    if spec.varargs is not None:
        return func

    arg_len = len(spec.args)
    if hasattr(func, "__self__"):
        arg_len -= 1

    return lambda *args, **kwargs: func(*args[:arg_len], **kwargs)


def to_varkw(func):
    """
    Convert to a variable keywords function
    :param callable func: function
    """
    spec = inspect.getfullargspec(func)
    if spec.varkw is not None:
        return func

    known = {arg for arg in spec.args + spec.kwonlyargs}
    return lambda *args, **kwargs: func(*args, **{k: v for k, v in kwargs.items() if k in known})
