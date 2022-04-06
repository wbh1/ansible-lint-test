def sysexit_no_wrapping():
    try:
        open("file_doesnt_exist.txt")
    except Exception as e:
        raise SystemExit from e


def sysexit_wrapped():
    try:
        open("file_doesnt_exist.txt")
    except Exception as e:
        # Adding 'from e' here does not change the output
        raise SystemExit(e)


def regular_chaining():
    try:
        open("file_doesnt_exist.txt")
    except Exception as e:
        raise ValueError("Couldn't open specified file!") from e


if __name__ == "__main__":
    import sys

    func = sys.argv[1] + "()"
    print(f"Running {func}")
    eval(func)
