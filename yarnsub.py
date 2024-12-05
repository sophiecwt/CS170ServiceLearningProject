#This is where we will write the function to substitute yarns 

# h: number of balls / skeins of the yarn that is recommended in pattern
# i: length of 1 ball / skein of the yarn that is recommended in pattern in meters
# j: length of 1 ball / skein of the desired yarn in meters
# k: number of balls / skeins of the desired yarn required for the pattern

# formula:
# (i * h) / j = k


def yarnSub (h,i,j,k):
    sub = 0
    k = (i * h) / j
    sub = k
    return(sub)
