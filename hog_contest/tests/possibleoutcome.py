

def outcome_calculator():
    x=range(2,9)
    dict={}
    for a in x:
        for b in x:
            for c in x:
                for d in x:
                    for e in x:
                        for f in x:
                            for h in x:
                                for g in x:
                                    value=(a+b+c+d+e+f+g+h)
                                    if value in dict:
                                        dict[value]+=1
                                    else:
                                        dict[value]=1
    return dict
sum=0
dict=outcome_calculator()
for item in dict.keys():
    dict[item]=dict[item]/(8**8)
    sum+=dict[item]
print(sum)
print(dict)