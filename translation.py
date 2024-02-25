
# [start : End : Step]
# [::-1] ----> for reversing

firstLine = input()
seconLine = input()

# now i reverse the firstline value , then compare with secondline
firstLinePrime = firstLine[::-1]

# now i throw condition
if firstLinePrime == seconLine:
    print("YES")
else:
    print("NO")