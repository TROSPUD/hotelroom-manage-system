# hotelroom-manage-system

## 部署与应用

```python
#本项目主要模块设计
/mysite/hotel/views.py
#html页面
/mysite/hotel/templates/hotel
#css及javascript
/mysite/static
```

1. 数据库生成

使用mysql, 在数据库软件中运行hotel.sql文件，生成hotel数据库。

2. 修改代码数据库设置

在/mysite/mysite/settings.py中修改连接的数据库为本地的数据库。数据库名为hotel, 用户和密码为自身mysql数据库设定

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          'ENGINE':'django.db.backends.mysql',
          'NAME':'hotel',
          'USER':'root',
          'PASSWORD':'hz2225910',
          'HOST':'localhost',
          'PORT':'3306',
    }
}
```

3. 运行服务器

在项目mysite文件夹下运行服务器（当前python环境中必须安装django包）

```
python manage.py inspectdb > hotel/models.py

python manage.py runserver

```

![https://docimg9.docs.qq.com/image/AgAACIbvZD3Z432tWPZLUrDyqdqdILsr.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1](https://docimg9.docs.qq.com/image/AgAACIbvZD3Z432tWPZLUrDyqdqdILsr.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1)

5. 浏览器打开

访问[http://127.0.0.1:8000](http://127.0.0.1:8000/)

## 效果展示

### HomePage

HotelManagement主页面,点击按钮可以进行管理员和员工的登录操作

![https://docimg2.docs.qq.com/image/AgAACIbvZD3ENZVpaB5NJaxMHJ5V1ToJ.png?w=2090&h=1274](https://docimg2.docs.qq.com/image/AgAACIbvZD3ENZVpaB5NJaxMHJ5V1ToJ.png?w=2090&h=1274)

### 员工

员工登录

登陆失败时登录界面会提示密码或用户名错误

![https://docimg5.docs.qq.com/image/AgAACIbvZD1_Y99F7MVEP7WbRa-3K-CE.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1](https://docimg5.docs.qq.com/image/AgAACIbvZD1_Y99F7MVEP7WbRa-3K-CE.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1)

![https://docimg4.docs.qq.com/image/AgAACIbvZD0BuvP7c2FGmI23-FQ8f7dY.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1](https://docimg4.docs.qq.com/image/AgAACIbvZD0BuvP7c2FGmI23-FQ8f7dY.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1)

员工登录成功后根据员工注册时的职位，进入前台员工使用界面或清洁员工使用界面。

### 前台员工

**顾客管理**

可以添加/编辑/删除顾客

![https://docimg2.docs.qq.com/image/AgAACIbvZD3wJTKiPPRJrbXvOYHADcFV.png?w=2090&h=1274](https://docimg2.docs.qq.com/image/AgAACIbvZD3wJTKiPPRJrbXvOYHADcFV.png?w=2090&h=1274)

**房间管理**

可以办理入住或退房业务

![https://docimg6.docs.qq.com/image/AgAACIbvZD0neiO32FlKdYDCltjb2mAR.png?w=2090&h=1274](https://docimg6.docs.qq.com/image/AgAACIbvZD0neiO32FlKdYDCltjb2mAR.png?w=2090&h=1274)

点击退房，房间状态改为待清洁

![https://docimg3.docs.qq.com/image/AgAACIbvZD0IcEeMWH1CWrJfc3SNOT7x.png?w=2090&h=1274](https://docimg3.docs.qq.com/image/AgAACIbvZD0IcEeMWH1CWrJfc3SNOT7x.png?w=2090&h=1274)

订单中，该项变为状态变为已结束，并自动输入结束时间

![https://docimg8.docs.qq.com/image/AgAACIbvZD24iDiLmKVCTrSIh9JZYqfB.png?w=2090&h=1274](https://docimg8.docs.qq.com/image/AgAACIbvZD24iDiLmKVCTrSIh9JZYqfB.png?w=2090&h=1274)

**订单管理**

可新建订单办理入住

![https://docimg9.docs.qq.com/image/AgAACIbvZD26JDUHzsZALYQiXKagRpyO.png?w=2090&h=1274](https://docimg9.docs.qq.com/image/AgAACIbvZD26JDUHzsZALYQiXKagRpyO.png?w=2090&h=1274)

注意，新建订单要选择状态为可入住的房间。

![https://docimg1.docs.qq.com/image/AgAACIbvZD3HmOPGWORK84SSzhC7MypG.png?w=2090&h=1274](https://docimg1.docs.qq.com/image/AgAACIbvZD3HmOPGWORK84SSzhC7MypG.png?w=2090&h=1274)

输入客户身份证号，若发现客户不在客户列表里面，则跳转至添加顾客页面

![https://docimg4.docs.qq.com/image/AgAACIbvZD2ueiLHhDpCxaRcTKvpl2j9.png?w=2090&h=1274](https://docimg4.docs.qq.com/image/AgAACIbvZD2ueiLHhDpCxaRcTKvpl2j9.png?w=2090&h=1274)

然后在订单页面能看到添加的订单

![https://docimg10.docs.qq.com/image/AgAACIbvZD31-4719qxAHbJilWrGWrBo.png?w=2090&h=1274](https://docimg10.docs.qq.com/image/AgAACIbvZD31-4719qxAHbJilWrGWrBo.png?w=2090&h=1274)

同时，在客房页面能看到对应入住的房间状态更新为使用中

![https://docimg2.docs.qq.com/image/AgAACIbvZD3QpmrCXllCbZl800znbWGR.png?w=2090&h=1274](https://docimg2.docs.qq.com/image/AgAACIbvZD3QpmrCXllCbZl800znbWGR.png?w=2090&h=1274)

### 清洁员工

清洁员工仅能看到待清洁的房间，点击按钮标识清洁完成，房间状态更改为可入住。

![https://docimg5.docs.qq.com/image/AgAACIbvZD1DjCHRKF1IKqSKObicimrJ.png?w=2090&h=1274](https://docimg5.docs.qq.com/image/AgAACIbvZD1DjCHRKF1IKqSKObicimrJ.png?w=2090&h=1274)

### 管理员

**管理员登录**

登陆失败时登录界面会提示密码或用户名错误

![https://docimg6.docs.qq.com/image/AgAACIbvZD11VjOggCtMsq55s0fFZvHP.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1](https://docimg6.docs.qq.com/image/AgAACIbvZD11VjOggCtMsq55s0fFZvHP.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1)

![https://docimg2.docs.qq.com/image/AgAACIbvZD2MR5ESUsFB6aiSr31T6w3r.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1](https://docimg2.docs.qq.com/image/AgAACIbvZD2MR5ESUsFB6aiSr31T6w3r.png?imageMogr2/thumbnail/1600x%3E/ignore-error/1)

管理员登陆成功后进入管理界面，可以对整个系统的数据进行管理，也可以点击登出。

**管理员工**

可以修改员工信息以及添加员工

![https://docimg6.docs.qq.com/image/AgAACIbvZD1n8l4VLq1GN6XTLNLBb7_5.png?w=2090&h=1274](https://docimg6.docs.qq.com/image/AgAACIbvZD1n8l4VLq1GN6XTLNLBb7_5.png?w=2090&h=1274)

**添加员工**

![https://docimg7.docs.qq.com/image/AgAACIbvZD3DCV63de5GwZytzrz15ohx.png?w=2090&h=1274](https://docimg7.docs.qq.com/image/AgAACIbvZD3DCV63de5GwZytzrz15ohx.png?w=2090&h=1274)

输入信息正确后成功添加

![https://docimg5.docs.qq.com/image/AgAACIbvZD3bSWFlEFNNzaQWgMieX6ZR.png?w=2090&h=1274](https://docimg5.docs.qq.com/image/AgAACIbvZD3bSWFlEFNNzaQWgMieX6ZR.png?w=2090&h=1274)

**修改员工信息**

![https://docimg2.docs.qq.com/image/AgAACIbvZD0e2RGSv19Nq4kGmswWTiRS.png?w=2090&h=1274](https://docimg2.docs.qq.com/image/AgAACIbvZD0e2RGSv19Nq4kGmswWTiRS.png?w=2090&h=1274)

**管理顾客**

可以添加/编辑/删除客人，具体和上述管理员工相似

![https://docimg6.docs.qq.com/image/AgAACIbvZD2mRn-y19dO5oD5CMBjT9VS.png?w=2090&h=1274](https://docimg6.docs.qq.com/image/AgAACIbvZD2mRn-y19dO5oD5CMBjT9VS.png?w=2090&h=1274)

**管理订单**

管理员可以添加/编辑/删除订单

![https://docimg1.docs.qq.com/image/AgAACIbvZD2dVIDjMU9K8arLyMiIVc7D.png?w=2090&h=1274](https://docimg1.docs.qq.com/image/AgAACIbvZD2dVIDjMU9K8arLyMiIVc7D.png?w=2090&h=1274)

**管理房间**

管理员可以添加房间、编辑或删除房间的信息

![https://docimg8.docs.qq.com/image/AgAACIbvZD3hWJnQI-NJUYzHTrgsjY62.png?w=2090&h=1274](https://docimg8.docs.qq.com/image/AgAACIbvZD3hWJnQI-NJUYzHTrgsjY62.png?w=2090&h=1274)

例：编辑房间信息

![https://docimg7.docs.qq.com/image/AgAACIbvZD2r1bJAW6pMNZFXYARl1ccV.png?w=2090&h=1274](https://docimg7.docs.qq.com/image/AgAACIbvZD2r1bJAW6pMNZFXYARl1ccV.png?w=2090&h=1274)

添加房间

![https://docimg2.docs.qq.com/image/AgAACIbvZD3b1V9mkUJIV4AWyXPjPdPB.png?w=2090&h=1274](https://docimg2.docs.qq.com/image/AgAACIbvZD3b1V9mkUJIV4AWyXPjPdPB.png?w=2090&h=1274)

房间添加成功

![https://docimg9.docs.qq.com/image/AgAACIbvZD0XHB-QvodPqLoFf3kuGiWS.png?w=2090&h=1274](https://docimg9.docs.qq.com/image/AgAACIbvZD0XHB-QvodPqLoFf3kuGiWS.png?w=2090&h=1274)

## 一、需求分析

### 1.1 系统需求

本酒店管理系统的目标是让酒店员工快速筛选并掌握酒店的房间信息，有利于提高顾客的订房效率，有效地减轻酒店员工的工作负担。

本系统主要面向三种用户角色：管理员、前台员工和清洁工。

- **管理员：**

管理员具有该系统的最高权限，可以对系统进行管理，可对数据库进行系统所提供的所有操作：

1. 房间管理：包括房间各种属性的增加、查询、修改和删除。
2. 员工信息管理：添加、查询、修改、删除所有员工的信息。
3. 客户管理：包括客户信息的添加、查询、修改、删除等。
- **前台员工：**
1. 房间查询：查询房间，查询房间的各种属性（房型、楼层等）
2. 客户管理：包括客户信息的添加、查询、修改、删除等。
3. 入住登记：输入顾客信息以及房间信息。先查询顾客信息，若不在数据库中则要输入顾客详细信息为顾客在客户信息表中添加该顾客的信息。查询房间信息，若房间可以入住则成功进行入住登记。
4. 退房登记：输入房间信息进行查询，提示是否超时的信息。成功退房后房间变回待清洁状态，等待被清洁，相应的信息插入到历史订单并且入住订单中删除该订单。
- **清洁员工：**
1. 房间查询：查询处于情节状态的房间，返回房间的各种属性（状态、房型、楼层等）
2. 清洁登记：清洁结束后，将房间状态从待清洁房间修改为可入住。

管理员、酒店前台员工和酒店清洁员工这三种用户的功能需求各不相同，其用户组织架构图如图

![用户组织架构.png](hotelroom-manage-system%20c89885c34d1d497c9384b47dd8063902/%25E7%2594%25A8%25E6%2588%25B7%25E7%25BB%2584%25E7%25BB%2587%25E6%259E%25B6%25E6%259E%2584.png)

### 1.2 系统用例图

![系统用例.png](hotelroom-manage-system%20c89885c34d1d497c9384b47dd8063902/%25E7%25B3%25BB%25E7%25BB%259F%25E7%2594%25A8%25E4%25BE%258B.png)

### 1.3 系统核心用例

本系统涉及到的用例主要是以下三个，它们分别是：入住登记、退房登记和清洁登记。

**1.3.1 入住登记**

**用例：**入住登记

**主要参与者：**前台员工

**涉众及其关注点：**

1. 前台员工：查询到该顾客是否在数据库中，选择可以入住的房间，记录入住信息
2. 顾客：顾客信息准确录入，尽快找到合适的空房间进行入住

**前置条件：**前台员工的账号必须已经添加到系统中。

**成功保证：**

1. 房间的信息显示为已入住。
2. 入住信息表记录该入住信息，包括房号、入住时间、顾客等。
3. 入住信息表的状态栏改为进行中。

**主成功场景：**

1. 前台员工登录系统
2. 前台员工查询并获得当前空闲房间信息
3. 前台员工根据顾客要求进一步查询筛选房间
4. 前台员工输入顾客信息进行入住

**扩展：**
1a. 前台员工的帐号或密码不正确：

1. 系统提示帐号或密码错误，要求用户重新输入。

4a. 顾客信息不在顾客信息表中

1. 系统提示顾客信息不全，须完善顾客信息表

**特殊需求：**系统的设计保障系统的健壮性。

**发生频率：**经常发生。

**1.3.2 退房登记**

**用例：**退房登记

**主要参与者：**前台员工

**涉众及其关注点：**

1. 前台员工：退房的房间必须是已入住的房间

**前置条件：**前台员工的账号必须已经添加到系统中，顾客必须已入住。

**成功保证：**

1. 房间的信息显示为待清洁。
2. 入住信息表记录更新该入住信息的退房时间。
3. 入住信息表的状态栏改为已结束。

**主成功场景：**

1. 前台员工登录系统
2. 前台员工查询并获得相关顾客或房间的入住信息
3. 系统提示该退房是否已超时
4. 前台员工确认退房，房间状态从已入住变为待清洁

**扩展：**

1a.前台员工的帐号或密码不正确：

1. 系统提示帐号或密码错误，要求用户重新输入。

**1.3.3 清洁登记**

**用例：**清洁登记

**主要参与者：**清洁员工

**涉众及其关注点：**

1. 清洁员工：对待清洁的房间进行清洁后及时更新房间状态

**前置条件：**清洁员工的账号必须已经添加到系统中。

**成功保证：**

1. 房间的状态显示为可入住。

**主成功场景：**

1. 清洁登录系统
2. 清洁员工查询并获得待清洁房间信息
3. 清洁员工对房间进行清洁
4. 清洁员工输入已完成清洁的房间号，进行已清洁确认，相应房间的状态从房间状态从待清洁房间修改为可入住

**扩展：**
1a. 员工的帐号或密码不正确：
1.系统提示帐号或密码错误，要求用户重新输入。

### 1.4领域模型

本系统一共有6个角色：管理员、前台员工、清洁员工、入住信息、房间、顾客。它们的关系如下：

一个管理员可以管理0或多个前台员工、清洁员工、顾客和房间，因此管理员对前台员工的关系数量是1：0..n，管理员对清洁员工的关系数量是1：0..n，管理员对顾客的关系数量是1：0..n，管理员对房间的关系数量也同样是1：0..n。

一条入住信息对应一个房间和一位顾客，因此入住信息对房间的关系数量是1：1，入住信息对顾客的关系数量是1：1.

一个清洁员工可以清洁0或多个房间，所以清洁员工对房间的关系数量是1：0..n。
据此，可以画出系统的领域模型

![DomainModel.png](hotelroom-manage-system%20c89885c34d1d497c9384b47dd8063902/DomainModel.png)

### 二、 架构设计

### 2.1业务用例的实现

使用Django框架进行网页软件开发。

### 2.2数据库设计

**2.2.1 ER图**

![https://docimg7.docs.qq.com/image/AgAACIbvZD0LTdfZWnVLyboRJ-T6n_YP.png?w=831&h=561](https://docimg7.docs.qq.com/image/AgAACIbvZD0LTdfZWnVLyboRJ-T6n_YP.png?w=831&h=561)

**2.2.2 数据库表设计**

本系统一共有5张数据库表，分别是：Admin、staff、customer、room、order

| 表名 | 说明 |
| --- | --- |
| Admin | 存放管理员信息的管理员表 |
| Staff | 存放员工信息的员工表 |
| Customer | 存放顾客信息的顾客表 |
| Room | 存放房间信息的房间表 |
| Order | 存放入住信息的入住信息表 |

下表描述了Admin表的详细信息

| 字段 | 数据类型 | 主键、外键 | 允许空 | 说明 |
| --- | --- | --- | --- | --- |
| id | integer | 主键 | 否 | 管理员编号 |
| account | string |  | 否 | 管理员帐号 |
| password | string |  | 否 | 管理员密码 |

添加约束unique，使得：account唯一

Staff表

| 字段 | 数据类型 | 主键、外键 | 允许空 | 说明 |
| --- | --- | --- | --- | --- |
| id | integer | 主键 | 否 | 员工编号 |
| name | string |  | 否 | 员工姓名 |
| account | string |  | 否 | 员工帐号 |
| password | string |  | 否 | 员工密码 |
| type | string |  | 否 | 员工类型（前台/清洁） |
| phone_number | string |  | 否 | 手机号码 |
| sex | string |  | 否 | 性别 |

添加约束unique，使得：account唯一

添加约束check，使得：sex只能为男或女

Room表

| 字段 | 数据类型 | 主键、外键 | 允许空 | 说明 |
| --- | --- | --- | --- | --- |
| room_number | integer | 主键 | 否 | 房间号 |
| type | string |  | 否 | 房间类型 |
| price | float |  | 否 | 房间价格 |
| state | string |  | 否 | 房间状态（使用中/可入住/待清洁） |

添加约束check，使得：

类型type只能为标准单人房/标准双人房/豪华大床房/顶级总统套房

状态state只能为使用中/可入住/待清洁

Order表

| 字段 | 数据类型 | 主键、外键 | 允许空 | 说明 |
| --- | --- | --- | --- | --- |
| id | integer | 主键 | 否 | 入住信息编号 |
| state | string |  | 否 | 入住状态（进行中/已结束） |
| room_id | integer | 外键，引用Room表room_number | 否 | 入住房间号 |
| cust_id | integer | 外键，引用Customer表id | 否 | 入住顾客编号 |
| staff_id | integer | 外键，引用
Staff表id | 否 | 负责人员工编号 |
| start_time | date |  | 否 | 入住时间 |
| end_time | date |  | 是 | 退房时间 |

添加约束check，使得：状态state只能为进行中/已结束

添加外键约束：room_id，cust_id，staff_id

使用Navicat数据库设计工具进行数据库的设计：

![https://docimg1.docs.qq.com/image/AgAACIbvZD1sUX_qiC1FxKHWf8XHe2Qm.png?w=862&h=811](https://docimg1.docs.qq.com/image/AgAACIbvZD1sUX_qiC1FxKHWf8XHe2Qm.png?w=862&h=811)