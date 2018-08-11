from threading import Thread


def thread_decorator(_fn, name=None, daemon=None):
    def fn_wrapper(fn):
        def args_wrapper(*args, **kwargs):
            new_thread = Thread(target=fn, name=name, args=args, kwargs=kwargs, daemon=daemon)
            new_thread.start()

            # 这个返回值贼关键！！！
            # 必须返回一个不可调用的对象
            if not callable(new_thread):
                return new_thread

        return args_wrapper

    if _fn and callable(_fn):
        return fn_wrapper(_fn)
    else:
        return fn_wrapper
