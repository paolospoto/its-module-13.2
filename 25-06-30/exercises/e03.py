# Age checker
age = int(input('Inserire età:'))
has_license = input('Hai la patente? y/n:')

is_adult = age >= 18
can_drive = is_adult and has_license == 'y'
is_old = age > 70
print('Is adult? ', is_adult)
print('Can drive? ', can_drive)
print('Is old and can drive?', can_drive and is_old)
