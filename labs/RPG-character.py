def create_character(name, strength, intelligence, charisma):
    # Controlli sul parametro nome
    if not isinstance(name, str):
        return "The character name should be a string."
    elif len(name) == 0:
        return "The character should have a name."
    elif len(name) > 10:
        return "The character name is too long."
    elif ' ' in name:
        return "The character name should not contain spaces."

    # Controlli sulle statistiche
    if (not isinstance(strength, int) or isinstance(strength, bool)) or \
       (not isinstance(intelligence, int) or isinstance(intelligence, bool)) or \
       (not isinstance(charisma, int) or isinstance(charisma, bool)):
        return "All stats should be integers."
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1."
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4."
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points."

    # Stampa il personaggio creato
    return (
        f"{name}\n"
        f"STR {'●' * strength + '○' * (10 - strength)}\n"
        f"INT {'●' * intelligence + '○' * (10 - intelligence)}\n"
        f"CHA {'●' * charisma + '○' * (10 - charisma)}"
    )