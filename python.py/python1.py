
nam = input('Wer bist du?')
print('Willkommen', nam)

efl = input('Press european floor number: ')
usf = int(efl) + 1
print('US Floor number', usf)


if usf != 17:
    print('sehr gute Wahl')
else:
    print('Is not accessible, please choose different level')

    newefl = input('Please choose different floor that is not 16 in Europe nor 17 in US:')
    newusf = int(newefl) + 1
    print(newusf)

    if newusf == 17:
        print('WTF dude')
    elif newusf < 5:
        print('Lower floors will be entered, you could have aken the stairs')
    elif newusf <= 10:
        print('everything below level 10')   
    elif newusf < 15:
        print('floor before level 15 will be entered')
    else :
        print('Understandable you took the elevater')

    if newusf < 5:
        print('Lower floors will be entered, you could have aken the stairs')
    elif newusf <= 10:
        print('everything below level 10')   
    elif newusf < 15:
        print('floor before level 15 will be entered')
    else :
        print('Understandable you took the elevater')
newusf = usf        
print('Have a great ride to level',newusf)
