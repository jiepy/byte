def cmp(x, y):
    return x >= y

def sort(*args):
    ret = []
    for item in args:
        for i, v in enumerate(ret):
           if cmp(item, v):
                ret.insert(i, item)
                break
        else:
            ret.append(item)
    return ret


s=sort( 3, 1, 2, 5)
print(s)