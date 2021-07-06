math = int(input('數學成績?'))
english = int(input('英文成績?'))

if math >= 90 and english >= 90:
    print('有獎品')
elif math < 60 and english < 60:
    print('要處罰') 
elif math < 60 or english < 60:
    print('再加油')
elif 90 > math >=60 and 90 > english >=60:
    print('無獎懲')