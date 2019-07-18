korean, english, math, science = map(int, input().split())
score_sum = korean + english + math + science
score_average = score_sum / 4
if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100 and 0 <= science  <= 100:
    if score_average >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
