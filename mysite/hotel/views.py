from django.shortcuts import render, redirect, HttpResponse
from .models import Admin, Customer, Order, Room, Staff
import pymysql
import time
from datetime import date
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'hotel/home.html')
    return render(request, 'hotel/home.html')

def adminLogin(request):
    '''
    管理员登录
    :param request:
    :return:
    '''
    print('lok')
    print(request.method)
    if request.method == 'GET':
        return render(request, 'hotel/login.html')
    #如果是post请求，获取用户提交的数据
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    if Admin.objects.filter(account = u, password = p):
        return redirect('../work')
    return render(request, 'hotel/login.html', {"error_msg": "用户名或密码错误"})
    

def staffLogin(request):
    '''
    员工登录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'hotel/StaffLogin.html')

    u = request.POST.get('user')
    p = request.POST.get('pwd')
    if Staff.objects.filter(account = u, password = p):
        sta = Staff.objects.filter(account = u, password = p).first()
        ty = sta.type
        print(ty)
        if ty == "前台":
            return redirect("../StaffWork")
        else:
            return redirect("../cleanWork")
    return render(request, "hotel/StaffLogin.html", {"error_msg": "用户名或密码错误"})



#管理员注册
def insertAdmin(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'hotel/register.html')
    
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    i = request.POST.get('id')

    Admin.objects.create(id = i, account = u, password = p)
    return render(request, "hotel/login.html")
#员工注册
def insertStaff(request):
    if request.method == 'GET':
        return render(request, 'hotel/StaffRegister.html')
    
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    i = request.POST.get('id')
    n = request.POST.get('name')
    t = request.POST.get('type')
    phone = request.POST.get('phone')
    s = request.POST.get('sex')

    Staff.objects.create(id = i, name = n, account = u, password = p, type = t, phone_number = phone, sex = s)
    return render(request, "hotel/StaffLogin.html")
#管理员管理员工
def getStaff(request):
    msg = 0
    if request.method == 'GET':
        staffList = Staff.objects.all()
        if staffList.count() != 0:
            i = {"ls":staffList, "msg":msg}
            print('yeee')
            for j in staffList:
                print(j.id)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/work.html",i)

def addStaff(request):
    if request.method == 'GET':
        return render(request, 'hotel/Addstaff.html')
    
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    i = request.POST.get('id')
    n = request.POST.get('name')
    t = request.POST.get('type')
    phone = request.POST.get('phone')
    s = request.POST.get('sex')

    Staff.objects.create(id = i, name = n, account = u, password = p, type = t, phone_number = phone, sex = s)
    return redirect('../work')

def deleStaff(request):
    print('delete')
    print(request.method)

    did = request.GET.get('dele_id')
    Staff.objects.filter(id=did).delete()
    return redirect('../work')

def editStaff(request):
    if request.method == 'GET':
        print('edit')
        print(request.method)
        print('1111111111')
        eid = request.GET.get('edit_id')
        print(eid)
        staf = Staff.objects.filter(id=eid).first()
        print(staf.id)
        return render(request,'hotel/editStaff.html',{'staf':staf})
    if request.method == 'POST':
        print('wtfffff')
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        i = request.POST.get('id')
        n = request.POST.get('name')
        t = request.POST.get('type')
        phone = request.POST.get('phone')
        s = request.POST.get('sex')
        flag = Staff.objects.filter(id=i).update(id = i, name = n, account = u, password = p, type = t, phone_number = phone, sex = s)
        if(flag == 1):
            return redirect('../work')
        else:
            return render(request, 'hotel/editStaff.html')

#管理员管理客户
def getClient(request):
    msg = 0
    print(request.method)
    if request.method == 'GET':
        clientList = Customer.objects.all()
        if clientList.count() != 0:
            i = {"ls":clientList, "msg":msg}
            print('yeee')
            for j in clientList:
                print(j.id)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/clientManage.html",i)

def addClient(request):
    if request.method == 'GET':
        return render(request, 'hotel/AddClient.html')
    
    n = request.POST.get('name')
    c = request.POST.get('id_card')
    phone = request.POST.get('phone')
    s = request.POST.get('sex')
    source = request.POST.get('source')
    Customer.objects.create(name = n, sex = s, id_card = c, phone_number = phone)
    if source == "0":
        return redirect('../clientManage')
    else:
        return redirect('../SclientManage')

def deleClient(request):
    print('delete')
    print(request.method)
    did = request.GET.get('id_card')
    Customer.objects.filter(id_card=did).delete()
    return redirect('../clientManage')

def editClient(request):
    if request.method == 'GET':
        print('edit')
        print(request.method)
        print('1111111111')
        eid = request.GET.get('id_card')
        source = request.GET.get('source')
        print(eid)
        cust = Customer.objects.filter(id_card=eid).first()
        print(cust.id_card)
        return render(request,'hotel/editClient.html',{'cust':cust,'source':source})
    if request.method == 'POST':
        print('wtfffff')
        n = request.POST.get('name')
        s = request.POST.get('sex')
        c = request.POST.get('id_card')
        source = request.POST.get('source')
        phone = request.POST.get('phone')
        
        flag = Customer.objects.filter(id_card=c).update(name = n, sex = s, id_card = c, phone_number = phone)
        print(flag)
        if(flag == 1):
            print('????')
            if source == "0":
                return redirect('../clientManage')
            else:
                return redirect('../SclientManage')
        else:
            print(n+s+c)
            return render(request, 'hotel/editClient.html')

#管理员管理房间
def getRoom(request):
    msg = 0
    if request.method == 'GET':
        rooomList = Room.objects.all()
        if rooomList.count() != 0:
            i = {"ls":rooomList, "msg":msg}
            print('yeee')
            for j in rooomList:
                print(j.room_number)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/RoomManage.html",i)

def addRoom(request):
    if request.method == 'GET':
        return render(request, 'hotel/AddRoom.html')
    
    r = request.POST.get('room_number')
    p = request.POST.get('price')
    t = request.POST.get('type')
    s = request.POST.get('state')

    Room.objects.create(room_number = r, type = t, price = p, state = s)
    return redirect('../RoomManage')

def deleRoom(request):
    print('delete')
    print(request.method)

    did = request.GET.get('room_number')
    Room.objects.filter(room_number=did).delete()
    return redirect('../RoomManage')

def editRoom(request):
    if request.method == 'GET':
        print('edit')
        print(request.method)
        print('1111111111')
        eid = request.GET.get('room_number')
        print(eid)
        room = Room.objects.filter(room_number=eid).first()
        print(room.room_number)
        return render(request,'hotel/editRoom.html',{'room':room})
    if request.method == 'POST':
        print('wtfffff')
        n = request.POST.get('room_number')
        p = request.POST.get('price')
        t = request.POST.get('type')
        print(n)
        flag = Room.objects.filter(room_number = n).update(type = t, price = p)
        if(flag == 1):
            print('success')
            return redirect('../RoomManage')
        else:
            print('77777')
            return render(request, 'hotel/editRoom.html')
#管理员管理订单
def getOrder(request):
    msg = 0
    if request.method == 'GET':
        orderList = Order.objects.all()
        if orderList.count() != 0:
            i = {"ls":orderList, "msg":msg}
            print('yeee')
        else:
            msg = "No order"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/OrderManage.html",i)

def addClientO(request):
    if request.method == 'GET':
        return render(request, 'hotel/AddClientO.html')
    
    n = request.POST.get('name')
    c = request.POST.get('id_card')
    phone = request.POST.get('phone')
    s = request.POST.get('sex')

    Customer.objects.create(name = n, sex = s, id_card = c, phone_number = phone)
    return redirect('../AddOrder')

def addOrder(request):
    if request.method == 'GET':
        return render(request, 'hotel/AddOrder.html')
    s = request.POST.get('state')
    r = request.POST.get('room_id')
    sa = request.POST.get('staff_id')
    t = request.POST.get('starttime')
    d = date.today()
    i = request.POST.get('id')
    source = request.POST.get('source')

    cust = Customer.objects.filter(id_card = i)
    client = Customer.objects.filter(id_card = i).first()
    #没有该客户
    if cust.count() ==0:
        print('no cclient')
        return render(request,"hotel/AddClientO.html",{"id":i})

    else:
        msg = 0
        print('client')
        print(client.id)
        exist_order = Order.objects.filter(room_id = r, state = '进行中')
        room = Room.objects.filter(room_number = r).first()
        print(room.state)
        if room.state == '使用中' or room.state == '待清洁':
            print('该房间不可订，请重新输入房号')
            msg = "该房间不可订，请重新输入房号"
            return render(request, 'hotel/AddOrder.html', {"msg":msg})
        Order.objects.create(state = s, room_id = r, cust_id = client.id, staff_id = sa, start_time = d)
        if source == '0':
            return redirect('../OrderManage')
        else:
            return redirect('../SOrderManage')

def deleOrder(request):
    print('delete')
    print(request.method)

    did = request.GET.get('id')
    Order.objects.filter(id=did).delete()
    return redirect('../OrderManage')

def editOrder(request):
    if request.method == 'GET':
        print('edit')
        print(request.method)
        print('1111111111')
        eid = request.GET.get('id')
        print(eid)
        order = Order.objects.filter(id=eid).first()
        print(order.id)
        return render(request,'hotel/editOrder.html',{'order':order})
    if request.method == 'POST':
        print('wtfffff')
        s = request.POST.get('state')
        t = request.POST.get('end_time')
        id = request.POST.get('id')
        print(s)
        flag = Order.objects.filter(id = id).update(state = s, end_time = t)
        if(flag == 1):
            print('success')
            return redirect('../OrderManage')
        else:
            print('77777')
            return render(request, 'hotel/editOrder.html')

#前台管理客户
def SgetClient(request):
    msg = 0
    if request.method == 'GET':
        clientList = Customer.objects.all()
        if clientList.count() != 0:
            i = {"ls":clientList, "msg":msg}
            print('yeee')
            for j in clientList:
                print(j.id)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/SclientManage.html",i)

def SaddClient(request):
    if request.method == 'GET':
        return render(request, 'hotel/AddClient.html')
    
    n = request.POST.get('name')
    c = request.POST.get('id_card')
    phone = request.POST.get('phone')
    s = request.POST.get('sex')

    Customer.objects.create(name = n, sex = s, id_card = c, phone_number = phone)
    return redirect('../clientManage')

def SdeleClient(request):
    print('delete')
    print(request.method)
    did = request.GET.get('id_card')
    Customer.objects.filter(id_card=did).delete()
    return redirect('../SclientManage')
#前台管理房间
def SgetRoom(request):
    msg = 0
    if request.method == 'GET':
        rooomList = Room.objects.all()
        if rooomList.count() != 0:
            i = {"ls":rooomList, "msg":msg}
            print('yeee')
            for j in rooomList:
                print(j.room_number)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/SRoomManage.html",i)

def checkOut(request):
    print('checkout')
    rid = request.GET.get('room_number')
    d = date.today()
    print(rid, d)
    flag = Order.objects.filter(room_id = rid, state = '进行中').update(state = '已结束', end_time = d)
    return redirect('../SRoomManage')

#前台管理订单
def SgetOrder(request):
    msg = 0
    if request.method == 'GET':
        orderList = Order.objects.all()
        if orderList.count() != 0:
            i = {"ls":orderList, "msg":msg}
            print('yeee')
        else:
            msg = "No order"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/SOrderManage.html",i)

def SdeleOrder(request):
    print('delete')
    print(request.method)

    did = request.GET.get('id')
    Order.objects.filter(id=did).delete()
    return redirect('../SOrderManage')

#清洁工清洁房间
def cleanWork(request):
    msg = 0
    if request.method == 'GET':
        rooomList = Room.objects.filter(state = '待清洁')
        if rooomList.count() != 0:
            i = {"ls":rooomList, "msg":msg}
            print('yeee')
            for j in rooomList:
                print(j.room_number)
        else:
            msg = "fffffalse"
            i = {"msg":msg}
        print(msg)
        return render(request,"hotel/cleanWork.html",i)
    
def cleanOut(request):
    print('cleanOut')
    rid = request.GET.get('room_number')
    print(rid)
    flag = Room.objects.filter(room_number = rid, state = '待清洁').update(state = '可入住')
    return redirect('../cleanWork')