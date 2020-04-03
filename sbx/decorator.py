
def decorator(func, *outer_args, **outer_kwargs):
    def wrapper(*args, **kwargs):
        print(f"decorator args={outer_args} kwargs={outer_kwargs}")
        
        print(f"before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after {func.__name__}")
        return result

    return wrapper


@decorator
@decorator
@decorator
def main():
    pass


def test_main():
    main()
    assert False