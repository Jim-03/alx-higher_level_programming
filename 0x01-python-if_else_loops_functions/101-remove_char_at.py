def remove_char_at(s, n):
    if 0 <= n < len(s):
        character = list(s)
        character.pop(n)
        result = ''.join(character)
        return result
    else:
        return s
