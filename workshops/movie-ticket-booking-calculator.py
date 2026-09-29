base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
is_member = False
is_weekend = False

# Controllo della maggiore età per l'acquisto generale
if age > 17:
    print('User is eligible to book a ticket')

# Controllo dell'età specifica per gli spettacoli serali
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Sconto applicato solo ai membri con almeno 21 anni
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Supplemento applicato se serale o se weekend
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Verifica requisiti complessivi per la prenotazione
if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
    print('Ticket booking condition satisfied')

    # Calcolo dei costi in base al tipo di posto scelto
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    # Calcolo finale: Base + Extra + Servizio - Sconto
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
else:
    print('Ticket booking failed due to restrictions')