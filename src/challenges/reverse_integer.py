def reverse_integer(x: int) -> int:
    is_negative: bool = True if x < 0 else False
    x_to_str_rev: str = str(x).replace("-","")[::-1]

    x_to_int_rev: int = int(x_to_str_rev)

    if is_negative:
        x_to_int_rev *= -1

    if x_to_int_rev > (2**31 - 1) or x_to_int_rev < (-2**31):
        return 0

    return x_to_int_rev
