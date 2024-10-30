def is_monster_bio_start(string, number_len):
    current = ''
    i = 0
    for char in string:
        current += char

        try:
            f = float(current)

            if i == number_len:
                return {'b': True, 'num': f, 'check_for_0': current.endswith('0 ')}
        
        except:
            continue
        
        i += 1
        
    return {'b': False, 'num': 0.0, 'check_for_0': False}

