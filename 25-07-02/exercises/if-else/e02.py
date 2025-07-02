# Grading system
# RULES:
# Use if-else statements
# score from 0-100
# >= 90 => 'Excellent'
# >= 80 => 'Very Good'
# >= 70 => 'Good'
# >= 60 => 'Sufficient'
# < 60  => 'Fail'

x = int(input('Insert score: '))

if x >= 90:
    print('Excellent')
elif x >= 80:
    print('Very Good')
# ....
else:
    print('Fail')
