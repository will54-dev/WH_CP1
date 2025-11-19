def multequl(var,*check):
    out = False
    for check in check:
        if var == check:
            out = True
    return out