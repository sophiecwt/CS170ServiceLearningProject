import gauge
import gaugepattern
import yarnsub

a = input("Enter rows/stitches per 10cm: ")
a = float(a)
b = input("Enter Desired width/length: ")
b = float(b)
c = input("Number of stitches to cast on or rows to knit: ")
c = float(c)

answergauge = gauge.gauge(a,b,c)

print(answergauge)