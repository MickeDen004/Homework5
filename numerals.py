from operator import itemgetter
numerals = {1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X'
            }
list(numerals.values())
for i in sorted(numerals.items(), key=itemgetter(1, 0))[::-1]:
    print(i)
numerals[1]
numerals[4]
numerals[8]
