def main():
    print("hello world")
    a=[1,21,'hello']
    a.append(10)
    a.pop(1)
    for i in range(len(a)):
        print(a[i])
    print("len of list:",len(a))
    b={'a':'2','b':3}
    print(b['a'])
    for key in b:
        print(b[key])
if __name__=='__main__':
    main()