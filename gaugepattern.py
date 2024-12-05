#This Is where we will write a gauge function for modifying gauge from a written pattern

#d: Rows/stitches per 10cm in original pattern
#e: Rows/stitches in original pattern
#f: Rows/stitches per 10cm inches in desired gauge
#g: Equivalent rows/stitches in your desired gauge

# formula:
# g = (e / d) * f


def gaugePattern (d,e,f,g):
    result = 0
    g = (e / d) * f
    result = g
    return(result)
