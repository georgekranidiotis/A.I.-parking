dic={}
def find_more(joe):
    for i in joe:
        dic[joe[i-1]] = 0
    for i in joe:
        for j in joe:
            if joe[i-1]== joe[j-1]:
                wtf = int(dic[joe[i-1]])
                dic[joe[i-1]] = wtf +1
    for item in dic:
        b = list(dic.values())
    joe = len(b)
    for j in range(joe):
        i = j-1
        if(b[i]>b[j]):
            save= b[i]
            b[i] = b[j]
            b[j]=save
    val = b[-1]
    for key,value in dic.items():
        if val == value:
            plate=key
            return plate