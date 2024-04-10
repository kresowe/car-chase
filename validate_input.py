def valid_input(inp, mini, maxi):
    is_valid = False
    try:
        inp = float(inp)
        if mini <= inp <= maxi:
            is_valid = True
        else:
            raise ValueError('')
    except ValueError:
        pass
    return is_valid
