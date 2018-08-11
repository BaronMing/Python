from threading import Thread
from types import FunctionType


class ThreadsManager:
    __error_message = {
        'TypeError_Arg_Message': '请检查是否给装饰器传入了多余的变量：参数_arg不能传值'
    }

    def __init__(self):
        self.threads = {}

    def __call__(self, _arg, multi_threads=False, name=None, daemon=None):
        def fn_wrapper(func):
            def args_wrapper(*args, **kwargs):
                thread = self.threads[func.__name__] = {}
                # 以下的字段名不是随便起的
                # 要与threading.Thread的参数名相同
                thread['target'] = func
                thread['args'] = args
                thread['kwargs'] = kwargs
                if name:
                    thread['name'] = name
                if daemon:
                    thread['daemon'] = daemon

                # 这个返回值贼关键！！！
                # 必须返回一个不可调用的对象
                # 我这里是返回了一个字符串
                if multi_threads:
                    ret = func.__name__
                else:
                    ret = self.__create_(thread)
                    ret.start()

                if not callable(ret):
                    return ret

            return args_wrapper

        if _arg and isinstance(_arg, FunctionType):
            return fn_wrapper(_arg)
        else:
            return fn_wrapper

    @staticmethod
    def __create_(thread):
        return Thread(**thread)

    def __create_threads(self):
        return [self.__create_(thread) for thread in self.threads.values()]

    def __start(self):
        [thread.start() for thread in self.__create_threads()]

    @property
    def start(self):
        if self.threads:
            def wrapper():
                self.__start()

            return wrapper
        else:
            raise Exception('必须先调用进程函数')

    @start.setter
    def start(self, _set):
        if _set.issubset(self.threads.keys()):
            self.__start()
        elif not _set:
            raise TypeError('必须传入有效参数')
        else:
            raise TypeError('类型为%s，要求参数类型为"集合"' % type(_set))

    # 经过再三思考后发现
    # catch_error不能装饰__call__，也不能在__call__中被调用
    # 因为这样做无法catch到__call__外面的进程函数
    @staticmethod
    def catch_error(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except TypeError as type_error:
                if "is not callable" in str(type_error):
                    raise Exception(ThreadsManager.__error_message['TypeError_Arg_Message'])
                else:
                    raise

        return wrapper
