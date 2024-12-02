#This Is where we will write a gauge function for gauge from scratch

# a: Rows/stitches per 10cm
# b: Desired width/length
# c: number of stitches to cast on or rows to knit

def gauge(a,b,c):
    answer = 0
    c = (a / 10) * b
    answer = c
    return(answer)

def main():
    a = input("Enter rows/stitches per 10cm: ")
    a = float(a)
    b = input("Enter Desired width/length: ")
    b = float(b)
    c = input("Number of stitches to cast on or rows to knit: ")
    c = float(c)

    answer = gauge(a,b,c)
    print(answer)


# call main when you click run or load this file
if __name__ == "__main__":
    main()