class Example:
    def decorator(*dec_args, **dec_kwargs):
        print(*dec_args, *dec_kwargs)

        def fn_wrapper(fn):
            def args_wrapper(self, *fn_args, **fn_kwargs):
                return fn(self, *fn_args, **fn_kwargs)
            return args_wrapper
        return fn_wrapper

    @decorator()
    def run(self):
        print("running")


if __name__ == "__main__":
    Example().run()
