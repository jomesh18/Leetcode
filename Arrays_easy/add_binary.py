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

<<<<<<< Updated upstream
# from leetcode
def add_binary(a:str, b:str)->str:
    a = list(a)
    b = list(b)
    c = 0
    res = ''
    while a or b or c:
        if a:
            c += int(a.pop())
        if b:
            c += int(b.pop())
        res += str(c%2)
        c //= 2
    return result[::-1]

# from leetcode
def add_binary(a: str, b:str)->str:
    if len(a) == 0: return b
    if len(b) == 0: return a
    if a[-1] =='1' and b[-1] =='1':
        return add_binary(add_binary(a[:-1],b[:-1]),'1')+'0'
    else:
        return add_binary(a[:-1],b[:-1])+str(int(a[-1])|int(b[-1]))

=======
#from leetcode
def addBinary(a: str, b: str) -> str:
    c, d, i = 0, "", -1
    j = -len(a) if len(a)<len(b) else -len(b)
    while i>=j:
        d=str((int(a[i])+int(b[i])+c)%2)+d
        c=int((int(a[i])+int(b[i])+c)/2)
        i-=1
    rem_str = a if len(a)>len(b) else b
    while i>=-len(rem_str):
        d=str((int(rem_str[i])+c)%2)+d
        c=int((int(rem_str[i])+c)/2)
        i-=1
    if(c==1):
        d="1"+d
    return d
>>>>>>> Stashed changes
