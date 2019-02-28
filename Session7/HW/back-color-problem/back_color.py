#Homework đây:
from random import choice,randint
import check_inside
shapes = [
    {
        'text': 'BLUE',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'RED',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'YELLOW',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'GREEN',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
def get_shapes():
    return shapes

#Viết 2 hàm này:
#Hàm 1: Tọa lựa chọn trên dưới meaing or color:
def generate_quiz():
    i = randint(0,3)
    j = randint(0,3)
    choice_text = shapes[i]["text"]
    choice_color = shapes[j]["color"]
    return [
                choice_text,
                choice_color,
                randint(0, 1) # 0 : meaning, 1: color
            ]
                
#Hàm 2: Kick chuột chọn vùng
def mouse_press(x, y, text, color, quiz_type):
    # Ở trên : chọn theo màu
    if(quiz_type==1):
        for i in range(len(shapes)):
            if(color==shapes[i]['color']):
                x1 = shapes[i]['rect'][0]
                y1 = shapes[i]['rect'][1]
                width = shapes[i]['rect'][2]
                height = shapes[i]['rect'][3]
                if(check_inside.is_inside(x,y,x1,y1,width,height) == True):
                    return True
                else:
                    return False  
    else: #Ở dưới chọn theo nghĩa
        for i in range(len(shapes)):
            if(text==shapes[i]['text']):
                x1 = shapes[i]['rect'][0]
                y1 = shapes[i]['rect'][1]
                width = shapes[i]['rect'][2]
                height = shapes[i]['rect'][3]
                if(check_inside.is_inside(x,y,x1,y1,width,height) == True):
                    return True
                else:
                    return False  


        



