def decorator(*decorator_args):
    def fn_wrapper(the_decorated_function):
        def args_wrapper(*args, **kwargs):

            # 在这里写一些必要的处理语句
            # 然后使用原函数调用装饰器中传入的参数
            if decorator_args:
                pass

            # 函数调用处使用 *args 与 **kwargs
            # args 是元组，kwargs是字典
            # *args 将元素解包到形参列表的位置参数处
            # **kwargs 将值解包到形参列表中与键名相同的命名参数处
            return the_decorated_function(*args, **kwargs)

        return args_wrapper

    return fn_wrapper


@decorator()
def decorated_function(*args, **kwargs):
    # 为什么要在"函数定义"中使用 *args 与 **kwargs 占位？
    # 答：不想让编辑器提示用户需要输入什么参数

    # 当在"函数定义"中使用 *args 与 **kwargs 占位时：

    # args 是一个元组，在函数体内，不能在"赋值"以外的位置解包
    arg, *_ = args

    # kwargs 是一个字典，在函数体内，不能在"赋值语句"中解包
    # 它就像是一个命名空间
    #
    # 可以在函数参数处解包：例如 print(*kwargs)
    # 但是 print 只支持*解包，不支持**解包，而且解出来的只有 key

    # for 循环是解包的万能大法
    # 使用 for element in args
    # 使用 for key, value in kwargs.items() 解包

    kwargs = kwargs

    return arg, kwargs
