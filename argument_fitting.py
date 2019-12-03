import inspect


def ignore_longer(func):
    spec = inspect.getfullargspec(func)
    if spec.varargs is not None:
        return func

    arg_len = len(spec.args)
    if hasattr(func, "__self__"):
        arg_len -= 1

    return lambda *args, **kwargs: func(*args[:arg_len], **kwargs)


def ignore_unknown(func):
    spec = inspect.getfullargspec(func)
    if spec.varkw is not None:
        return func

    known = {arg for arg in spec.args + spec.kwonlyargs}
    return lambda *args, **kwargs: func(*args, **{k: v for k, v in kwargs.items() if k in known})
