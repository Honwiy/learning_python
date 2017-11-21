# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight/(height * height)
if bmi<18.5:
    print(bmi,"过轻")
elif bmi>=18.5 and bmi<25:
    print(bmi,"正常")
elif bmi>=25 and bmi<28:
    print(bmi,"过重")
elif bmi>=28 and bmi<32:
    print(bmi,"肥胖")
elif bmi>=32:
    print(bmi,"严重肥胖")