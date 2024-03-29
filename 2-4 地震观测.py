#用户输入P波和S波从震中A到达地震观测点B的时间间隔(秒)，分别输入2、10、22
#计算并输出震中A与观测点B间的距离(公里)
#如果城市C(ABC位于同一直线上)与观测点B的距离为100km，观测点接收到S波后立即向城市C发出地震警报(忽略警报利用网络传输所需的时间)，那么P波还有几秒到达城市C? 破坏力较强的面波L波还有几秒到达?
#说明：L波到达的时间就是S波到达的时间(它们同时到达)，S波到达前的时间就是城市C中人员的逃生应对时间
#城市D和AB不在一条直线上，AD距离为200km，观测点向城市D发出地震警报后，P波还有几秒到达? S波几秒后到达?

def motion():
    t=float(input("从震源A到观测点B，接收到纵波和横波的时间差为(秒)："))
    Dab=t/(1/3.6-1/6.2) #A和B之间的距离
    print("震源A距离观测点B大约为{:.2f}公里。".format(Dab))

    Pbc=100/6.2-t
    Sbc=100/3.6
    print("城市C在{:.1f}秒后可以感觉到地震波，{:.1f}秒后强震到达。".format(Pbc,Sbc))
    Pd=(200-Dab)/6.2-t
    Sd=(200-Dab)/3.6
    print("城市D在{:.1f}秒后可以感觉到地震波，{:.1f}秒后强震到达。".format(Pd,Sd))

if __name__=='__main__':
    motion()