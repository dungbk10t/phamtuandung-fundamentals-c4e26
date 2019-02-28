#Check điểm P xem có năm trong hcn ABCD không ?
def area(x1, y1, x2, y2, x3, y3): 
      return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 
def is_inside(x, y, x1, y1, width_h, height_t): 
    #rectangle ABCD: A(x1,y1),B(x2,y2),C(x3,y3),D(x4,y4) and point check P(x,y)
    x3 = x1
    x2 = x4 = x1 + width_h
    y2 = y1
    y3 = y4 = y1 + height_t
    #Area of rectangle ABCD  
    S = width_h*height_t
    # print(A)
    #Area of triangle PAB  
    S1 = area(x, y, x1, y1, x2, y2) 
    # print(S1)
    #Area of triangle PBD
    S2 = area(x, y, x2, y2, x4, y4) 
    # print(S2)
    #Area of triangle PCD  
    S3 = area(x, y, x3, y3, x4, y4) 
    # print(S3)
    #Area of triangle PAC  
    S4 = area(x, y, x1, y1, x3, y3) 
    # print(S4)
    if(S == S1 + S2 + S3 + S4):
        return True
    else:
        return False
x = is_inside(30,50,20,30,100,100)
print(x)
