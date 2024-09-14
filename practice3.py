def workLeft(Ax,Ay,Bx,By):
    return min(Ax*Ax+Ay*Ay,Bx*Bx+By*By)

print(workLeft(12,5,12,9))