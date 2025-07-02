# Access with time and age restrictions
# RULES:
# Use if-else statements
# - Minors (under 18) can enter only if accompanied by a parent or guardian
# - Minors cannot enter after 10 PM (even if with a parent)
# - Adults (18 and older) can enter at any time

age = int(input('Insert age: '))


if age >= 18:
    print('Pass')
else:
    time = int(input('Insert time (PM): '))
    if time > 10:
        print('You shall not pass!')
    else:
        is_with_parent = input('With parent? y/n: ')

        if is_with_parent == 'y':
            print('Pass')
        else:
            print('You shall not pass!')
