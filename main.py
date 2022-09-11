import names
import random


f = open('netflix.txt', 'w')
q=0

while True:
    first=names.get_first_name()
    last =names.get_last_name()
    birthday1=random.choice('1')
    birthday2=random.choice('012')
    birthday3=random.choice('12')
    birthday4=random.choice('0123456789')
    domain   =random.choice(['gmail.com','outlook.com','yahoo.com','protonmail.com'])
    country  =random.choice(['CN','BR','UK','US'])
    max      =random.choice('1234')
    pay      =random.choice(['CC','DC'])
    dot      =random.choice(['.',''])
    #emmanuelsouza53@gmail.com:eusoudos3 | SUBSCRIBED | Country: BR | Free trial: false | Current plan: Padr u00E3o | Has UHD: false | Max streams: 2 | Payment method: CC
    f.write(f'{first}{dot}{last}{birthday1}{birthday2}{birthday3}{birthday4}@{domain} | SUBSCRIBED | Country:{country} | Free trial: false | Current plan: Padr u00E3o | Has UHD: false | Max streams: {max} | Payment method: {pay}\n')
    q+=1
