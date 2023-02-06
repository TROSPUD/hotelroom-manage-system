from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.adminLogin, name='adminLogin'),
    path('register/', views.insertAdmin, name='insertAdmin'),
    path('work/', views.getStaff, name='getStaff'),
    path('AddStaff/', views.addStaff, name='addStaff'),
    path('deleteStaff/', views.deleStaff, name='deleStaff'),
    path('editStaff/', views.editStaff, name='editStaff'),
    path('clientManage/', views.getClient, name='getClient'),
    path('AddClient/', views.addClient, name='addClient'),
    path('editClient/', views.editClient, name='editClient'),
    path('deleteClient/', views.deleClient, name='deleClient'),
    path('RoomManage/', views.getRoom, name='getRoom'),
    path('AddRoom/', views.addRoom, name='addRoom'),
    path('editRoom/', views.editRoom, name='editRoom'),
    path('deleteRoom/', views.deleRoom, name='deleRoom'),
    path('OrderManage/', views.getOrder, name='getOrder'),
    path('AddOrder/', views.addOrder, name='addOrder'),
    path('AddClientO/', views.addClientO, name='addClientO'),
    path('editOrder/', views.editOrder, name='editOrder'),
    path('deleteOrder/', views.deleOrder, name='deleOrder'),
    path('StaffLogin/', views.staffLogin, name='staffLogin'),
    path('StaffRegister/', views.insertStaff, name='insertStaff'),
    path('StaffWork/', views.SgetRoom, name='SgetRoom'),
    path('SRoomManage/', views.SgetRoom, name='SgetRoom'),
    path('checkout/', views.checkOut, name='checkOut'),
    path('SclientManage/', views.SgetClient, name='SgetClient'),
    path('SdeleteClient/', views.SdeleClient, name='SdeleClient'),
    path('SOrderManage/', views.SgetOrder, name='SgetOrder'),
    path('SdeleteOrder/', views.SdeleOrder, name='SdeleOrder'),
    path('cleanWork/', views.cleanWork, name='cleanWork'),
    path('cleanOut/', views.cleanOut, name='cleanOut'),

]