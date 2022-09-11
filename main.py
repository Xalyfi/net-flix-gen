import names
import random

first=names.get_first_name()
last =names.get_last_name()
birthday1=random.choice('1')
birthday2=random.choice('012')
birthday3=random.choice('12')
birthday4=random.choice('0123456789')

print(f'{first}.{last}{birthday1}{birthday2}{birthday3}{birthday4}@gmail.com')