#This is where we will write the function to substitute yarns 

# h: number of balls / skeins of the yarn that is recommended in pattern
# i: length of 1 ball / skein of the yarn that is recommended in pattern in meters
# j: length of 1 ball / skein of the desired yarn in meters
# k: number of balls / skeins of the desired yarn required for the pattern

# formula:
# (i * h) / j = k
def yarnSub (h,i,j,k):
    sub = 0
    (i * h) / j = k
    sub = g
    return(sub)

def main():
    h = input("number of balls / skeins of the yarn that is recommended in pattern: ")
    h = float(h)
    i = input("length of 1 ball / skein of the yarn that is recommended in pattern in meters: ")
    i = float(i)
    j = input("length of 1 ball / skein of the desired yarn in meters: ")
    j = float(j)
    k = input("number of balls / skeins of the desired yarn required for the pattern: ")
    k = float(k)

    sub = yarnSub(h,i,j,k)
    print(sub)


# call main when you click run or load this file
if __name__ == "__main__":
    main()
