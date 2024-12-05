import gauge
import gaugepattern
import yarnsub

calc = input("Which calculator would you like to use? : yarnsub, gauge from scratch, gauge from pattern, none ")


if calc == "gauge from scratch":
    a = input("Enter rows/stitches per 10cm: ")
    a = float(a)
    b = input("Enter Desired width/length in centimeters: ")
    b = float(b)
    c = 0
    c = float(c)

    answergauge = gauge.gauge(a,b,c)

    print(answergauge)


if calc == "gauge from pattern":
    d = input("Rows/stitches per 10cm in original pattern gauge: ")
    d = float(d)
    e = input("Rows/stitches in original pattern: ")
    e = float(e)
    f = input("Rows/stitches per 10cm inches in desired gauge: ")
    f = float(f)
    g = 0
    g = float(g)

    result = gaugepattern.gaugePattern(d,e,f,g)

    print(result)


if calc == "yarnsub":
    h = input("number of balls / skeins of the yarn that is recommended in pattern: ")
    h = float(h)
    i = input("length of 1 ball / skein of the yarn that is recommended in pattern in meters: ")
    i = float(i)
    j = input("length of 1 ball / skein of the desired yarn in meters: ")
    j = float(j)
    k = 0
    k = float(k)

    sub = yarnsub.yarnSub(h,i,j,k)
    print(sub)

if calc == "none":
    print("")
    

