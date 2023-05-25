def main():
    han = open('mbox-short.txt')
    for line in han:
        line = line.rstrip()
        #print('Line: ',line)
        wds = line.split()
        
        if len(wds) < 3 or wds[0] != 'From' :   
            continue
        print(wds[2])

if __name__ == "__main__":
    main()