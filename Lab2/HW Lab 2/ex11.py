#Check điểm P xem có năm trong hcn ABCD không ?
def area(x1, y1, x2, y2, x3, y3): 
      return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 
def is_inside(x, y, x1, y1, width_h, height_t): 
    #rectangle ABCD: A(x1,y1),B(x2,y2),C(x3,y3),D(x4,y4) and point check P(x,y)
    x3 = x1
    x2 = x4 = x1 + width_h
    y2 = y1
    y3 = y4 = y1 - height_t
    #Area of rectangle ABCD  
    A = width_h*height_t
    # print(A)
    #Area of triangle PAB  
    A1 = area(x, y, x1, y1, x2, y2) 
    # print(A1)
    #Area of triangle PBD
    A2 = area(x, y, x2, y2, x4, y4) 
    # print(A2)
    #Area of triangle PCD  
    A3 = area(x, y, x3, y3, x4, y4) 
    # print(A3)
    #Area of triangle PAC  
    A4 = area(x, y, x1, y1, x3, y3) 
    # print(A4)
    if(A == A1 + A2 + A3 + A4):
        print("Given point lies inside the rectangle") 
        return True
    else:
        print("Given point does not lie on the rectangle")
        return False
is_inside(200,-120,140,-60,100,200)
# # Anh Đức ơi em không hiểu nếu để đoạn code dưới thì lại ra dòng
# # "Given point does not lie on the rectangle."
# if(is_inside==True):
#     print("Given point lies inside the rectangle") 
# else:
#     print("Given point does not lie on the rectangle")   