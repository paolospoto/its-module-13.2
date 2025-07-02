# Shipping fee based on weight and destination
# RULES:
# Use if-else statements
# - Domestic shipping:
#   - Up to 1 kg: $5.00
#   - Up to 5 kg: $10.00
#   - Over 5 kg: $20.00
# - International shipping:
#   - Up to 1 kg: $15.00
#   - Up to 5 kg: $30.00
#   - Over 5 kg: $60.00

destination = input('Insert destination: domestic/international ')
weight = float(input('Insert weight: '))
fee = 0

if destination == 'domestic':
    if weight <= 1:
        fee = 5
    elif weight <= 5:
        fee = 10
    else:
        fee = 20
elif destination == 'international':
    if weight <= 1:
        fee = 15
    elif weight <= 5:
        fee = 30
    else:
        fee = 60
else:
    print('Destination not valid')

print('Fee: ', fee)
