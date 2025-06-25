hour = 21.59
if hour > 23:
    hour = 23
elif hour < 0:
    hour = 0
if 7 > hour >= 22:
    print('доброй ночи')
elif hour < 12:
    print('доброе утро')
elif hour < 17:
    print('добрый день')
else:
    print('добрый вечер')
