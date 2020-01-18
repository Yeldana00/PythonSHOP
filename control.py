## THIS IS THE CCONTROLLER FILE< IT IS TH SUPERSET SUPER FATHER OF THE MODULE AND VIEW IT THIS PROJECT
import time
import settings
import platform
import subprocess
import view
import module
import getpass
from pyzt import inputs, inputi, inputf

def logger(message):
        time_format  = "%Y-%m-%d %X %A %B %p %r"
        time_current = time.strftime(time_format)
        with open('data/log.txt','a') as f:
            f.write(f"{time_current}:{message}")
            f.write('\n')
class Control():
    fr = settings.FIRST_RUN
    current_user = 'Azat' #Current user in this session
    current_user_role = 'admin'

    def prepare_file(self,log='data/log.txt',users='data/users.txt',products='data/products.txt',orders='data/orders.txt'):
        path_list = [log,orders,products,users]
        for each in path_list:
            with open(each,'w') as f:
                f.write('')

    def system_check(self):
        # check python version
        print(f"Step 1: Checking Python Version : {platform.python_version()}")
        if platform.python_version()[0] == '3':
            print('PYTHON VERSION OK!')
        else:
            exit('Sorry, The program dose not support your python version, please update to python3.x')
        # check required packages installed
        print(f"Step 2: Checking Python packages")
        required_pkgs = ['azt','pyzt']
        installed_pkgs = subprocess.check_output(['pip3','list']).decode("utf-8")
        for pkg in required_pkgs:
            if pkg not in installed_pkgs:
                exit("requirements not installed! Please install all of required packages.")
            print("PYTHON PACKAGE REQUIREMENTS OK!")
        print(f"Step 3: Checking data resources")
        data_resources = ['data/log.txt','data/users.txt','data/products.txt','data/orders.txt']
        for each in data_resources:
            try:
                with open(each) as f:
                    pass
            except FileNotFoundError:
                exit("Data Source NOt Found!")

    def run(self):
        print("Running the AzatAI Python Shop system self checking")
        self.system_check()
        self.prepare_file()
        if self.fr is False: # super admin already exist
            print("In the case super admin already exist")
        else:
            home = view.Home()
            home.superadmin()
            while True:
                user_name = input('Please input a username for SUPERADMIN:\n')
                user_pw = input(f'Please input a password for SUPERADMIN {user_name}:\n')
                if  user_name != '' and user_pw != '' and  user_name != ' ' and user_pw != ' ':
                    user = module.User()
                    user.is_admin = True
                    user.add(user_name, user_pw)
                    settings.SUPER_ADMIN = user_name
                    settings.SUPER_ADMIN_PW = user_pw
                    settings.CURRENT_USER = user_name
                    settings.CURRENT_USER_ROLE = "ADMIN"
                    self.log(user_name, user_pw, settings.CURRENT_USER_ROLE, 'кірді')
                    self.admin()
                else:
                    print('Again')
    def admin(self):
        home_admin = view.Home()
        home_admin.welcome()
        while True:
            admin_choice = inputi("Please select your choice 1-Logout, 2 - kirdi,shykty , 3 - List users ,4 - Profile \n")
            if admin_choice==1:  
                with open('data/log.txt','r') as f:
                    data=f.read().split('\n')
                    data.pop()
                self.log(data[len(data)-1][0],data[len(data)-1][2],settings.CURRENT_USER_ROLE,'шықты')
                self.logout()
            elif admin_choice==2:
                with open ('data/log.txt','r') as f:
                    d=f.read()
                    print(d)
                    while True:
                        en = inputs('Таңдаңыз: 1- logout , 2- profile , 3- artka:')
                        if en == '1':
                            with open('data/log.txt', 'r') as f:
                                data = f.read().split('\n')
                                data.pop()
                            self.log(data[len(data) - 1][0], data[len(data) - 1][2], settings.CURRENT_USER_ROLE,
                                     'шықты')
                            self.logout()
                        if en == '2':
                            self.admin()
                        if en == '3':
                            break
            elif admin_choice==3:
                l = []
                with open('data/users.txt', 'r') as f:
                    e = f.read().split('\n')
                    for i in e:
                        a = i.split(',')
                        l.append(a)
                    l.pop()
                    print('  usr, pwd,   Date created     ,                                    admin,manager,staff,client')
                    for index, item in enumerate(l):
                        print(index, item)
                while True:
                    s= inputi("Таңдаңыз:1-logout , 2 - Profile , 3 - Edit logs ")
                    if s==1:
                        with open('data/log.txt', 'r') as f:
                            data = f.read().split('\n')
                            data.pop()
                        self.log(data[len(data) - 1][0], data[len(data) - 1][2], settings.CURRENT_USER_ROLE, 'шықты')
                        self.logout()
                    elif s==2:
                        self.admin()
                    elif s==3:
                        l=[]
                        with open ('data/users.txt','r') as f:
                            e=f.read().split('\n')
                            for i in e:
                                a=i.split(',')
                                l.append(a)
                            l.pop()
                            print('  usr, pwd,   Date created     ,                                    admin,manager,staff,client')
                            for index,item in enumerate(l):
                                print(index,item)
                            while True:
                                tandau=inputs('Статусты озгерту ушін индексін танданыз,q-logout, q1-profile,q2-artka kaitu: ')
                                if tandau=='q':
                                    with open('data/log.txt', 'r') as f:
                                        data = f.read().split('\n')
                                        data.pop()
                                    self.log(data[len(data) - 1][0], data[len(data) - 1][2], settings.CURRENT_USER_ROLE,'шықты')
                                    self.logout()
                                elif tandau=='q1':
                                    self.admin()
                                elif tandau=='q2':
                                    break
                                else:
                                    try:
                                        if int(tandau)==0 or int(tandau)>=len(l):
                                            print('ozgerte almaisyz!!!')
                                        elif len(l)>1 :
                                            print( '  usr, pwd,   Date created                                                  ,admin,manager,staff,client')
                                            while True:
                                                for i in l:
                                                    print(i)
                                                while True:
                                                    engiz=input('Client>Staff -1, Client>Manager-2, Staff>Manager-3: , 4-logout , 5 - profile ,6 - back')
                                                    if engiz=='1':
                                                        if l[int(tandau)][6]=='True' and l[int(tandau)][5]=='False' and l[int(tandau)][4]=='False' and l[int(tandau)][3]=='False':
                                                            l[int(tandau)][6]='False'
                                                            l[int(tandau)][5]='True'
                                                            with open('data/users.txt','w+') as d1:
                                                                for i in l:
                                                                    for item in i:
                                                                        d1.write(item+',')
                                                                    d1.write('\n')
                                                                print('  usr, pwd,   Date created     ,                                    admin,manager,staff,client')
                                                                for index, item in enumerate(l):
                                                                    print(index, item)
                                                    elif engiz=='2':
                                                        if l[int(tandau)][6]=='True' and l[int(tandau)][5]=='False' and l[int(tandau)][4]=='False' and l[int(tandau)][3]=='False':
                                                            l[int(tandau)][6]='False'
                                                            l[int(tandau)][4]='True'
                                                            with open('data/users.txt','w+') as d1:
                                                                for i in l:
                                                                    for item in i:
                                                                        d1.write(item+',')
                                                                    d1.write('\n')
                                                                print('  usr, pwd,   Date created     ,                                    admin,manager,staff,client')
                                                                for index, item in enumerate(l):
                                                                    print(index, item)
                                                    elif engiz=='3':
                                                        if l[int(tandau)][6]=='False' and l[int(tandau)][5]=='True' and l[int(tandau)][4]=='False' and l[int(tandau)][3]=='False':
                                                            l[int(tandau)][5]='True'
                                                            l[int(tandau)][4]='True'
                                                            with open('data/users.txt','w+') as d1:
                                                                for i in l:
                                                                    for item in i:
                                                                        d1.write(item+',')
                                                                    d1.write('\n')
                                                                print( '  usr, pwd,   Date created     ,                                    admin,manager,staff,client')
                                                    elif engiz=='6':
                                                        break
                                                    elif engiz=='5':
                                                        self.admin()
                                                    elif engiz=='4':
                                                        with open('data/log.txt', 'r') as f:
                                                            data = f.read().split('\n')
                                                            data.pop()
                                                        self.log(data[len(data) - 1][0], data[len(data) - 1][2],settings.CURRENT_USER_ROLE, 'шықты')
                                                        self.logout()
                                                    else:
                                                        print('Again')
                                        else:
                                            print('kaita engiz!!!')
                                    except (ValueError):
                                        print('kaita')



            elif admin_choice == 4:
                self.admin()
        
    def logout(self):
        settings.CURRENT_USER_ROLE='GUEST'
        home_guest = view.Home()
        home_guest.welcome()
        while True:
            a= inputi('REGISTER-1 /LOGIN TO CONTINUE - 2 : ')
            if a==1:
                user_name = inputs('Please input a username :\n')
                # with open ('vip.txt','w') as dos:
                #     sert=dos.write(user_name+',')
                user_pw = inputs(f'Please input a password  {user_name}:\n')
                if user_name != '' and user_pw != '' and user_name != ' ' and user_pw != ' ':
                    lis = []
                    with open('data/users.txt', 'r') as f:
                        data = f.read().split('\n')
                        data.pop()
                        for i in data:
                            d = i.split(',')
                            lis.append(d)
                        for i in range(len(lis)):
                            if lis[i][0] == user_name and lis[i][1] == user_pw and lis[i][3] == 'True':
                                print('bul account saitka tirkelgen')
                                self.logout()
                            elif lis[i][0] == user_name and lis[i][1] == user_pw and lis[i][4] == 'True':
                                print('bul account saitka tirkelgen')
                                self.logout()
                            elif lis[i][0] == user_name and lis[i][1] == user_pw and lis[i][5] == 'True':
                                print('bul account saitka tirkelgen')
                                self.logout()
                            elif lis[i][0] == user_name and lis[i][1] == user_pw and lis[i][6] == 'True':
                                print('bul account saitka tirkelgen')
                                self.logout()
                    user = module.User()
                    user.is_client = True
                    user.add(user_name,user_pw)
                    settings.CURRENT_USER = user_name
                    settings.CURRENT_USER_ROLE = "CLIENT"
                    self.log(user_name, user_pw, settings.CURRENT_USER_ROLE, 'кірді')
                    self.client()
            elif a==2:
                self.login()
            elif a==3:
                break
    def login(self):
         user_name = inputs('Please input a username :\n')
         user_pw = inputs(f'Please input a password {user_name}:\n')
         lis=[]
         with open ('data/users.txt','r') as f:
            data=f.read().split('\n')
            data.pop()
            for i in data:
                d=i.split(',')
                lis.append(d)
            for i in range(len(lis)):
                if lis[i][0]==user_name and lis[i][1]==user_pw and lis[i][3]=='True':
                    settings.CURRENT_USER_ROLE='ADMIN'
                    settings.CURRENT_USER=user_name
                    self.log(user_name,user_pw,settings.CURRENT_USER_ROLE,'кірді')
                    self.admin()
                elif lis[i][0]==user_name and lis[i][1]==user_pw and lis[i][4]=='True':
                    settings.CURRENT_USER_ROLE='MANAGER'
                    settings.CURRENT_USER=user_name
                    self.log(user_name,user_pw,settings.CURRENT_USER_ROLE,'кірді')
                    self.manager()
                elif lis[i][0]==user_name and lis[i][1]==user_pw and lis[i][5]=='True':
                    settings.CURRENT_USER_ROLE='STAFF'
                    settings.CURRENT_USER=user_name
                    self.log(user_name,user_pw,settings.CURRENT_USER_ROLE,'кірді')
                    self.staff()
                elif lis[i][0]==user_name and lis[i][1]==user_pw and lis[i][6]=='True':
                    settings.CURRENT_USER_ROLE='CLIENT'
                    settings.CURRENT_USER=user_name
                    self.log(user_name,user_pw,settings.CURRENT_USER_ROLE,'кірді')
                    self.client()
            else:
                print('siz tirkelmegensiz')
                self.logout()
    def client(self):
         home_admin = view.Home()
         home_admin.welcome()
         while True:
             client_choice = inputi("Please select your choice 1-Logout, 2 - Buy, 3 - Profile \n")
             if client_choice == 1:
                 with open('data/log.txt', 'r') as f:
                     data = f.read().split('\n')
                     data.pop()
                 self.log(data[len(data) - 1][0], data[len(data) - 1][2], settings.CURRENT_USER_ROLE, 'шықты')
                 self.logout()
             elif client_choice == 2:
                 shopping_list = []
                 product_list=[]
                 with open('1mall.txt','r') as f1:
                    a=f1.read().split('\n')
                    for i in a:
                        sp=i.split(',')
                        product_list.append(tuple(sp))
                 product_list.pop()
                 salary = inputi('Input your salary:')
                 s=salary
                 print('Your salary',salary)
                 while True:
                     for index, item in enumerate(product_list):
                         print(index, item)
                     while True:
                         user_choice = inputs("Input 'ok' to continue: 'q' for exists")
                         if user_choice == 'ok':
                             user_choice = inputi("Which product do you want to buy:")
                             if user_choice < len(product_list) and user_choice >= 0:
                                 p_item = product_list[user_choice]
                                 if int(p_item[1]) <= salary:
                                     shopping_list.append(tuple(p_item))
                                     salary -= int(p_item[1])
                                     print(f"Added {p_item} into shopping cart, your current balance is {salary}")
                                 else:
                                     print(f"Sorry, only {salary} left on your credit. You can't buy!")
                             else:
                                 print(f"Product {user_choice} dose not exist! Dude!")
                         elif user_choice == 'q':
                             if s - salary > 0:
                                 l = set()
                                 print("------------shopping list-----------")
                                 print("Your current balance:", salary)
                                 print('AzatAI Python Shop'.center(50, '-'))
                                 time_format = "%Y-%m-%d %X %A %B %p %r"
                                 time_current = time.strftime(time_format)
                                 print(time_current)
                                 for i in shopping_list:
                                     qaz = (i, shopping_list.count(i))
                                     l.add(qaz)
                                 for each in l:
                                     print(each)
                                 with open('a.txt', 'r') as file:
                                     daso = file.read()
                                 l2 = []
                                 with open('data/log.txt', 'r') as f:
                                     daso1 = f.read().split('\n')
                                     daso1.pop()
                                     for i in daso1:
                                         asq = i.split(',')
                                         l2.append(asq)
                                 q1 = str(l2[len(l2) - 1][0])
                                 q2 = str(l2[len(l2) - 1][1])
                                 if q1 in daso and q2 in daso:
                                     print('You vip client, you have 15% discount')
                                     print(''.center(50, '-'))
                                     print('Itogo=            ', ((s - salary) - ((s - salary) * 0.15)))
                                     print('Spasibo za pokupku')
                                 else:
                                     print(''.center(50, '-'))
                                     print('Itogo=            ', (s - salary))
                                     print('Spasibo za pokupku')
                                 if s - salary >= 200000:
                                    f_list = []
                                    with open('data/log.txt', 'r') as f:
                                        data = f.read().split('\n')
                                        data.pop()
                                        for i in data:
                                            a = i.split(',')
                                            f_list.append(a)
                                    q = str(f_list[len(f_list) - 1][0])
                                    q1 = str(f_list[len(f_list) - 1][1])
                                    with open('a.txt', 'a') as file:
                                        file.write(q + ',' + q1 + '\n')
                             self.client()
             elif client_choice == 3:
                self.client()
             elif client_choice > 3:
                print('Again')

    def staff(self):
        view.Home().welcome()
        while True:
            staff_choice = inputi(" 1-Logout, 2- Profile , 3 - Dalee")
            if staff_choice==3:
                while True:
                    ase= inputi('1 - add new product , 2 - edit product salary , 3 - see all products , 4 - profile , 5 - logout ' )
                    if ase == 1:
                        product_list = []
                        with open('1mall.txt', 'r') as f1:
                            a = f1.read().split('\n')
                            a.pop()
                            for i2 in a:
                                i3=i2.split(',')
                                product_list.append(tuple(i3))
                        with open('1mall.txt', 'r') as f1:
                            a = f1.read().split('\n')
                            a.pop()
                            for i in a:
                                print(i)
                        eng=inputs('Product name: ')
                        eng1=inputs("Salary: ")
                        product_list.append(tuple([eng,eng1]))
                        with open('1mall.txt','w') as defd:
                            for i in product_list:
                                defd.write(str(i[0]+','+str(i[1]+'\n')))
                    elif ase ==2:
                        qazas=[]
                        with open('1mall.txt', 'r') as f1:
                            a = f1.read().split('\n')
                            a.pop()
                            for i in a:
                                sp=i.split(',')
                                qazas.append(tuple(sp))
                            for index,item in enumerate(qazas):
                                print(index,item)
                            while True:
                                it = inputs("Продукты бағасын өзгерту үшін индексін енгізіңіз, q-artka")
                                if int(it)<len(a) and int(it)>=0:
                                    i1=int(it)
                                    prod_i=list(qazas[i1])
                                    baga=inputi('Producty zhana bagasy:')
                                    prod_i.insert(1,baga)
                                    prod_i.pop()
                                    qazas.insert(i1,tuple(prod_i))
                                    qazas.pop(i1+1)
                                    with open('1mall.txt','w') as zh:
                                        for i in range(len(qazas)):
                                            zh.write(str(qazas[i][0])+','+str(qazas[i][1]))
                                            zh.write('\n')
                                elif it == 'q':
                                    break
                                elif it == 'q1':
                                    self.log(data[len(data) - 1][0], data[len(data) - 1][3], settings.CURRENT_USER_ROLE, 'шықты')
                                    self.logout()
                                elif it == 'q2':
                                    self.staff()
                    elif ase == 3:
                        with open('1mall.txt', 'r') as f1:
                            a = f1.read().split('\n')
                            a.pop()
                            for i in a:
                                print(i)
                    elif ase == 4:
                        self.log(data[len(data) - 1][0], data[len(data) - 1][3], settings.CURRENT_USER_ROLE, 'шықты')
                        self.logout()
                    elif i == 5:
                        self.staff()
                    else:
                        print('again')

            elif staff_choice == 2:
                self.staff()
            elif staff_choice == 1:
                with open('data/log.txt', 'r') as f:
                    data = f.read().split('\n')
                    data.pop()
                self.log(data[len(data) - 1][0], data[len(data) - 1][3], settings.CURRENT_USER_ROLE, 'шықты')
                self.logout()
    def manager(self):
        view.Home().welcome()
        while True:
            aser = inputi('1 - Satylgan products, 2 - del product , 3 - see all products , 4 - profile , 5 - logout ')
            if aser == 1:
                with open('man.txt', 'r') as defd:
                        for item in defd:
                            print(item)
            elif aser == 2:
                qazas = []
                with open('1mall.txt', 'r') as f1:
                    a = f1.read().split('\n')
                    for i in a:
                        sp = i.split(',')
                        qazas.append((sp))
                    for index, item in enumerate(a):
                        print(index, item)
                    while True:
                        iqra = inputi(" 1- oshiru , 2-artka, 3-logout,4-profile: ")
                        if iqra ==1:
                            ewq= inputi('Index the product ')
                            a.pop(ewq)
                            with open ('1mall.txt','w') as darganius:
                                ass=darganius.write(' ')
                            with open ('1mall.txt','a') as f:
                                for i in a:
                                    f.write(i)
                        elif iqra == 2:
                            break
                        elif iqra == 3:
                            with open('data/log.txt', 'r') as f:
                                data = f.read().split('\n')
                                data.pop()
                                self.log(data[len(data) - 1][0], data[len(data) - 1][4], settings.CURRENT_USER_ROLE, 'шықты')
                                self.logout()
                        elif iqra == 4:
                            self.manager()
            elif aser == 3:
                with open('1mall.txt', 'r') as f1:
                    a = f1.read().split('\n')
                    for i in a:
                        print(i)
            elif aser == 4:
                self.manager()
            elif aser == 5:
                with open('data/log.txt', 'r') as f:
                    data = f.read().split('\n')
                    data.pop()
                    self.log(data[len(data) - 1][0], data[len(data) - 1][2], settings.CURRENT_USER_ROLE, 'шықты')
                    self.logout()
            else:
                print('again')

    def log(self,usr,pwd,role,soz):
        time_format  = "%Y-%m-%d %X %A %B %p %r"
        time_current = time.strftime(time_format)
        with open('data/log.txt','a') as f:
            f.write(f"{usr},{pwd} {role} {soz} {time_current}")
            f.write('\n')