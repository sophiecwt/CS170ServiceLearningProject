#This Is where we will write a gauge function for gauge from scratch

# a: Rows/stitches per 10cm
# b: Desired width/length
# c: number of stitches to cast on or rows to knit

def gauge(a,b,c):
    answer = 0
    c = (a / 10) * b
    answer = c
    return(answer)
