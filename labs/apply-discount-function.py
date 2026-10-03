def apply_discount(price, discount):
    if not isinstance(price, (int, float)) or isinstance(price, bool):              # Controllo esteso ai bool, interpretati anche come interi
        return "The price should be a number"
    elif not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        return price - (price * (discount / 100))                                   # Se tutti i controlli sono superati, la funzione restituisce il prezzo scontato 