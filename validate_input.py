def validate_input(field_name, inp, mini, maxi):
    is_valid = False
    text = ''
    try:
        inp = float(inp)
        if mini <= inp <= maxi:
            is_valid = True
        else:
            raise ValueError('')
    except ValueError:
        text += f'{field_name} should be a number between {mini} and {maxi}. \n'
    return is_valid, text, inp

