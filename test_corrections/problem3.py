def euc(n, m):
    print(n,m)
    if n== m:
        return
    elif n > m:
        return euc(n - m, m)
    else:
        return euc(n, m - n)

def main():
    print(euc(14, 10))

if __name__ == '__main__':
    main()