from threading import Thread


class ThreadManager:
    def __init__(self, immediately=True):
        self.immediately = immediately
        self.threads = set()

    def __call__(self, name=None, daemon=None):
        def fn_wrapper(fn):
            def args_wrapper(*args, **kwargs):
                new_thread = Thread(target=fn, name=None, args=args, kwargs=kwargs, daemon=None)
                if self.immediately:
                    new_thread.start()
                else:
                    self.threads.add(new_thread)

                return new_thread

            return args_wrapper

        return fn_wrapper

    def __start(self):
        [thread.start() for thread in self.threads]

    @property
    def start(self):
        if self.threads:
            return lambda: self.__start()
        else:
            raise Exception('必须先调用进程函数')

    @start.setter
    def start(self, _set):
        if not _set:
            raise TypeError('集合不能为空，必须赋有效值')
        elif _set.issubset(self.threads):
            self.__start()
        else:
            raise TypeError('类型为%s，要求参数类型为"集合"' % type(_set))
