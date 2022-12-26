if __name__ == "__main__":
    import time
    print("CALCULATOR")
    a = int(input("A: "))
    b = int(input("B: "))
    c = input("(+/-/X/:/%): ")
    if c == "+":
        print(a, "+", b, "=", a+b)
    if c == "-":
        print(a, "-", b, "=", a-b)
    if c == "X":
        print(a, "X", b, "=", a*b)
    if c == ":":
        print(a, ":", b, "=", a/b)
    if c == "%":
        print(a, "%", b, "=", a%b)
    time.sleep(5)