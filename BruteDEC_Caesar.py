suratcinta = 'zowkxkckx_vctaez_qmek_qnuhyh' #encrypted message
hurup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(hurup)):
    translated = ''
    for symbol in suratcinta:
        if symbol in hurup:
            num = hurup.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(hurup)
            translated = translated + hurup[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))