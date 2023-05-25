def main():
    count = 0
    sum = 0
    print('Antes: ', count, sum)
    for value in [9, 41, 12, 3, 74, 15]:
        count = count +1
        sum = sum + value
        print(count, sum, value)
    print('Después', count, sum, sum/count)
if __name__ == "__main__":
    main()