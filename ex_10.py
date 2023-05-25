def main():
    fname= input('Ingrese el archivo: \n(Da enter)')
    if len (fname) < 1 : fname = "clown.txt"
    hand = open(fname)

    di = dict()
    for lin in hand:
        lin = lin.rstrip()
        wds = lin.split()
        for w in wds:   #Counter
            di[w] = di.get(w,0) + 1
            
        #print(di)
        #x = di.items(5)
    tmp = list()
    for k,v in di.items():
        newt = (k,v)
        tmp.append(newt)
    
    tmp = sorted(tmp, reverse=True)
    #print('Sorteado',tmp)
    for v,k in tmp[:5]:
        print(k,v)
if __name__ == "__main__":
    main()