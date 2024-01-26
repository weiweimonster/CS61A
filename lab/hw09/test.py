while True:
    Flag = False
    while not Flag:
        Flag = True
        formula = input('enter formula:')
        for i in formula:
            if not (formula[0] in ['C','O','H'] and i in ['C','H','O','0','1','2','3','4','5','6','7','8','9']):
                Flag = False
                print('wrong formula reenter:')
                break

    # C12H3OOH
    dict = {'C':0, 'H':0, 'O':0}
    i = 0
    while i < len(formula):
        if i == len(formula)-1:
            dict[formula[i]]+=1
            break
        index = i
        if formula[i] == 'C':
            while not index==len(formula)-1 and not formula[index+1] in ['C','H','O'] :
                index += 1
            if index == i:
                dict['C'] += 1
            else:
                dict['C'] += int(formula[i+1:index+1])
            i = index+1
        elif formula[i] == 'H':
            while not index == len(formula)-1 and not formula[index+1] in ['C','H','O']:
                index += 1
            if index==i:
                dict['H'] += 1
            else:
                dict['H'] += int(formula[i+1:index+1])
            i = index+1
        elif formula[i] == 'O':
            while not index==len(formula)-1 and not formula[index+1] in ['C','H','O'] :
                index += 1
            if index==i:
                dict['O'] += 1
            else:
                dict['O'] += int(formula[i+1:index+1])
            i = index+1
    weight = dict['C']*12.011+dict['H']*1.0079+dict["O"]*15.9994
    print(round(weight,4))








