На основі Pandas побудовано програму визначення ймовірностей сум двох гральних кубіків за методом Монте-Карло.
Проведено якісний аналіз методу при різній кількості спостережень
Важливо! Колонка dictionary вказує значення з нормального розподілу (довідкова інформація), які є еталоном для визначення якості методу Монте-Карло.

1.  Кількість спостережень = 100

                  count       predict  dictionary

    Sum of dice
    2 3.0 3.0 2.78
    3 13.0 13.0 5.56
    4 3.0 3.0 8.33
    5 10.0 10.0 11.11
    6 16.0 16.0 13.89
    7 15.0 15.0 16.67
    8 9.0 9.0 13.89
    9 9.0 9.0 11.11
    10 9.0 9.0 8.33
    11 8.0 8.0 5.56
    12 5.0 5.0 2.78

Ми бачимо суттєві розбіжності отриманної верогідності ('predict') та еталону ('dictionary') -якість незадовільна!

2.  Кількість спостережень = 1000

                 count  predict  dictionary

    Sum of dice
    2 35.0 3.5 2.78
    3 57.0 5.7 5.56
    4 69.0 6.9 8.33
    5 122.0 12.2 11.11
    6 139.0 13.9 13.89
    7 168.0 16.8 16.67
    8 142.0 14.2 13.89
    9 120.0 12.0 11.11
    10 78.0 7.8 8.33
    11 47.0 4.7 5.56
    12 23.0 2.3 2.78

Тут якість методу суттєво покращилась, але йще є значні прогалини!

3. Кількість спостережень = 10000

Sum of dice count predict dictionary
2 284.0 2.84 2.78
3 542.0 5.42 5.56
4 869.0 8.69 8.33
5 1117.0 11.17 11.11
6 1342.0 13.42 13.89
7 1702.0 17.02 16.67
8 1313.0 13.13 13.89
9 1132.0 11.32 11.11
10 855.0 8.55 8.33
11 549.0 5.49 5.56
12 295.0 2.95 2.78

Тут якість методу майже відповідає ідеальній, вже нема таких значних прогалин!

3. Кількість спостережень = 100000

Sum of dice count predict dictionary
2 2801.0 2.801 2.78
3 5425.0 5.425 5.56
4 8200.0 8.200 8.33
5 11113.0 11.113 11.11
6 13901.0 13.901 13.89
7 16604.0 16.604 16.67
8 13979.0 13.979 13.89
9 11343.0 11.343 11.11
10 8446.0 8.446 8.33
11 5422.0 5.422 5.56
12 2766.0 2.766 2.78

Тут якість методу майже ідеальна.

Висновок: Якість методу Монте-Карло значно залежить від квлькості спостережень, чим більше - тим точніше результат.
Метод має дуже простий код реалізації та інтуїтивно зрозумілий, але зновж таки його якість залежить від кількості спостережень.
На експеременті ми бачимо, що 10 000 спостережень вже дають достатньо високу якість результату.