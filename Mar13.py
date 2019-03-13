def ordinal(num):
    var = str(num)
    if var[-1] == '1':
        print('{}st'.format(var))
    elif var[-1] == '2':
        print('{}nd'.format(var))
    elif var[-1] == '3':
        print('{}rd'.format(var))
    else:
        print('{}th'.format(var))

ordinal(21)
ordinal(22)
ordinal(23)
ordinal(24)
ordinal(20)
