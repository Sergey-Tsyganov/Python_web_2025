# подбор оп росту 150-180
#число
#кандидатов
#число
#прошедших
#среди
#прошедших:
#мин
#рост
#макс
#прост

count = 0
count_cand = 0
max_h = -float('inf')
min_h = float('inf')

while True:

    height = int(input('введите рост'))
    if height == -1:
        break
    count += 1
    if 150 < height < 180:
        count_cand += 1
        if height > max_h:
            max_h = height
        if height < min_h:
            min_h = height

print(f'всего {count} кандидатов, прошли отбор {count_cand}, мин рост {min_h}, макс рост {max_h}')
