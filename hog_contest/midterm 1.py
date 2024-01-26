def splash(klay,curry):
    while curry==3:
        steph = klay
        klay = lambda klay: steph(curry+1)
        curry=curry+2
        return klay
    return curry//5

steph = lambda klay: splash(11,curry)-3
steph, curry=splash(steph,3),30
steph(4)