def addBinary(a: str, b: str) -> str:
    if a == "0" and b == "0":
        return "0"
    min_len, max_len = min(len(a), len(b)), max(len(a), len(b))
    c = 0
    res = []
    for i in range(-1, -min_len-1, -1):
        digit_res = int(a[i])+int(b[i])+c
        if digit_res == 2:
            c = 1
            digit_res = 0
        elif digit_res == 3:
            c = 1
            digit_res = 1
        else:
            c = 0
        res.append(str(digit_res))
    rem_str = a if len(a)>len(b) else b
    for i in range(-min_len-1, -max_len-1, -1):
        digit_res = int(rem_str[i])+c
        if digit_res == 2:
            c = 1
            digit_res = 0
        else:
            c = 0
        res.append(str(digit_res))
        if c == 0:
            break
    if c == 1:
        res.append(str(c))
    else:
        if len(res)<max_len:
            res.extend(rem_str[:(max_len-len(res))][::-1])
    res.reverse()
    return "".join(res)
