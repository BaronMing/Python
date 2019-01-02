class Example:
    class __Decorator:
        # 承接装饰器参数
        def __init__(self, before=None, after=None, *args, **kwargs):
            self.dec_args = args
            self.dec_kwargs = kwargs

            self.before = before
            self.after = after

        # 接收被装饰函数
        def __call__(self, fn):
            # 接收被装饰函数的参数
            return lambda *fn_args, **fn_kwargs: {
                self.__fn_info(fn, *fn_args, **fn_kwargs),
                self.__exec()
            }

        def __fn_info(self, fn, *fn_args, **fn_kwargs):
            self.fn = fn
            self.fn_args = fn_args
            self.fn_kwargs = fn_kwargs

        # 在被装饰函数调用前调用的函数
        def __enter__(self):
            # self.before(*self.dec_args, **self.dec_kwargs)
            print("before")
            return self

        # 在被装饰函数调用后调用的函数
        def __exit__(self, exc_type, exc_val, exc_tb):
            # self.after(*self.dec_args, **self.dec_kwargs)
            print("after")
            pass

        # 执行
        def __exec(self):
            with self:
                return self.fn(*self.fn_args, **self.fn_kwargs)

    @__Decorator()
    def run(self):
        print("running")


if __name__ == "__main__":
    Example().run()
