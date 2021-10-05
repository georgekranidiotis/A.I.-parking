def is_plate(plate):
    pin = list(plate)
    pin_num = len(pin)
    wtf = 0
    ftw = 0
    w=pin_num+1
    if pin_num==7 or pin_num==6:
        for i in range(0,3):
            if pin[i].isalpha:
                wtf= wtf +1
        if wtf==3:
            for i in range(3,pin_num):
                if pin[i].isnumeric:
                   ftw= ftw +1
            if ftw== pin_num-3:
               return True
            else :
                return False


