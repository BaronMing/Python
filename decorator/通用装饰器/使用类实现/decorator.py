from types import GeneratorType

class Decorator:
    # 承接装饰器参数
    def __init__(self, before=None, after=None):
        # before 与 after 都必须是无参函数
        self.before = before
        self.after = after

    # 接收被装饰函数
    def __call__(self, fn):
        # 收集被装饰函数的参数
        def collection(*args, **kwargs):
            with self:
                return fn(*args, **kwargs)

        return collection

    # 在被装饰函数调用前调用的函数
    def __enter__(self):
        # self.before()
        print("before")
        return self

    # 在被装饰函数调用后调用的函数
    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.after()
        print("after")
        return self
    


@Decorator()
def test_function():
    print("*" * 10)
    return "final"


if __name__ == "__main__":
    t = test_function()
    print(t)
