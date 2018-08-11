def decorator_params(fn):
    # wrapper接收的是实参而不是形参
    def wrapper(*args, **kwargs):
        # 计算形参中必传参数的数量（非零则执行if）
        if fn.__code__.co_argcount - len(fn.__default__):
            return fn(*args, **kwargs)
        else:
            arg0 = args[0] if args else None
            arg_s = args[1:] if args else ()

            if callable(arg0) and not arg_s and not kwargs:
                return fn(*arg_s, **kwargs)(arg0)
            else:
                return fn(*args, **kwargs)

    return wrapper
