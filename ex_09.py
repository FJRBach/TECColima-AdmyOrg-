def main():
    fname= input('Ingrese el archivo: ')
    if len (fname) < 1 : fname = "clown.txt"
    hand = open(fname)

    di = dict()
    for lin in hand:
        lin = lin.rstrip()
        wds = lin.split()
        for w in wds:   #Counter
            di[w] = di.get(w,0) + 1
            
    #print(di)
    largest = -1    #FindWord
    theword = None
    for k,v in di.items():
        if v > largest: 
            largest = v
            theword = k #RecordarLlave
    print(theword,largest)  

if __name__ == "__main__":
    main()