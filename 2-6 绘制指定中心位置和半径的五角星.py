import turtle as t
import math as m

star_pos={'x1':0,'y1':0,'x2':0,'y2':0,'x3':0,'y3':0,'x4':0,'y4':0,'x5':0,'y5':0}

def calc_pos(ori_x,ori_y,r):
    global star_pos
    star_pos['x1'] = ori_x+r*m.cos(m.radians(162))
    star_pos['y1'] = ori_y+r*m.sin(m.radians(162))

    star_pos['x2'] = ori_x+r*m.cos(m.radians(90))
    star_pos['y2'] = ori_y+r*m.sin(m.radians(90))

    star_pos['x3'] = ori_x+r*m.cos(m.radians(18))
    star_pos['y3'] = ori_y+r*m.sin(m.radians(18))

    star_pos['x4'] = ori_x+r*m.cos(m.radians(306))
    star_pos['y4'] = ori_y+r*m.sin(m.radians(306))

    star_pos['x5'] = ori_x+r*m.cos(m.radians(234))
    star_pos['y5'] = ori_y+r*m.sin(m.radians(234))
    print(star_pos)
    print("(x1,y1)和(x4,y4)的距离L为"+str(m.sqrt((star_pos['x4'] - star_pos['x1'])**2 + (star_pos['y4'] - star_pos['y1'])**2)))
    return m.sqrt((star_pos['x4'] - star_pos['x1'])**2 + (star_pos['y4'] - star_pos['y1'])**2)

def draw_fiveanglestar(ori_x,ori_y,r):
    global star_pos
    t.Screen();t.speed(1000)
    # 先画外接圆
    t.penup();t.goto(ori_x, ori_y-r);t.pendown()
    t.circle(r)
    # 回到中心位置，画x1，y1
    t.penup();t.goto(ori_x, ori_y);t.pendown()
    t.color('red');t.begin_fill()
    t.goto(star_pos['x1'],star_pos['y1'])
    t.goto(star_pos['x3'],star_pos['y3'])
    t.goto(star_pos['x5'],star_pos['y5'])
    t.goto(star_pos['x2'],star_pos['y2'])
    t.goto(star_pos['x4'],star_pos['y4'])
    t.goto(star_pos['x1'],star_pos['y1'])
    t.end_fill()

    t.penup()
    t.goto(50,-170)
    t.pendown()
    t.write("2306020123 韩镒名",font=("Arial",20,"normal"))
    t.hideturtle();

def draw_using_L(ori_x,ori_y,r,L):
    # 先画外接圆
    t.penup();t.goto(ori_x, ori_y-r);t.pendown()
    t.circle(r)
    # 回到中心位置
    t.penup();t.goto(ori_x, ori_y);t.pendown()
    t.begin_fill()
    t.setheading(180);t.right(18)
    t.forward(r)
    t.setheading(0)
    t.right(18*2)
    t.forward(L)
    for a in range(4):
        t.left(180);t.right(36)
        t.forward(L)
    t.end_fill()
    t.done()

if __name__=='__main__':
    r=100
    ori_x=30
    ori_y=40
    L=calc_pos(ori_x,ori_y,r)
    draw_fiveanglestar(ori_x,ori_y,r)
    draw_using_L(-60,-80,r,L)