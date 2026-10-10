def pin_extractor(poems):
    secret_codes = []  # Lista con tutti i PIN
    for poem in poems:
        lines = poem.split('\n')  # Divide la poesia in righe
        secret_code = ''
        for line_index, line in enumerate(lines):  # Itera riga per riga con relativo indice
            words = line.split()  #Divide la riga in parole
            if len(words) > line_index:
                # Aggiunge la lunghezza dell'n-esima parola
                secret_code += str(len(words[line_index]))
            else:
                #Se mancano parole sufficienti, usa '0'
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))