from .models import Login
import numpy as nm
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import metrics

# Create your views here.
def home(request):
    
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = request.POST['user']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']


        if password1==password2:
            if User.objects.filter(username=user).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'User created')
                return redirect('login')
        else:
            print('User password is not matching')
            return redirect('register')
    else:
        return render(request,'registers.html')

#---------------------------Login-----------------------------
def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass1']

        users=auth.authenticate(username=username,password=password)

        if users is not None:
            auth.login(request,users)
            return redirect('attribute')
        else:
            messages.info(request,'Invalid User')
            return redirect('login')
    else:  
        return render(request,'logins.html')


def logout(request):
    auth.logout(request);
    return redirect('/')

#============================Start the function of District=====================================
def district(dist):
    if dist == 'Ahmednagar':
        a=1
        return a
    elif dist == 'Akola':
        a=2
        return a
    elif dist == 'Amravati':
        a=3
        return a
    elif dist == 'Aurangabad':
        a=4
        return a
    elif dist == 'Beed':
        a=5
        return a
    elif dist == 'Bhandara':
        a=6
        return a
    elif dist == 'Buldhana':
        a=7
        return a
    elif dist == 'Chandrapur':
        a=8
        return a
    elif dist == 'Dhule':
        a=9
        return a
    elif dist == 'Gadchiroli':
        a=10
        return a
    elif dist == 'Gondia':
        a=11
        return a
    elif dist == 'Hingoli':
        a=12
        return a
    elif dist == 'Jalgaon':
        a=13
        return a
    elif dist == 'Jalna':
        a=14
        return a
    elif dist == 'Kolhapur':
        a=15
        return a
    elif dist == 'Latur':
        a=16
        return a
    elif dist == 'Mumbai City':
        a=17
        return a
    elif dist == 'Mumbai Suburban':
        a=18
        return a
    elif dist == 'Nanded':
        a=19
        return a
    elif dist == 'Nandurbar':
        a=20
        return a
    elif dist == 'Nashik':
        a=21
        return a
    elif dist == 'Osmanabad':
        a=22
        return a
    elif dist == 'Palghar':
        a=23
        return a
    elif dist == 'Parbhani':
        a=24
        return a
    elif dist == 'Pune':
        a=25
        return a
    elif dist == 'Raigad':
        a=26
        return a
    elif dist == 'Ratnagiri':
        a=27
        return a
    elif dist == 'Sangli':
        a=28
        return a
    elif dist == 'Satara':
        a=29
        return a
    elif dist == 'Sindhudurg':
        a=30
        return a
    elif dist == 'Solapur':
        a=31
        return a
    elif dist == 'Thane':
        a=32
        return a
    elif dist == 'Wardha':
        a=33
        return a
    elif dist == 'Washim':
        a=34
        return a
    elif dist == 'Yavatmal':
        a=35
        return a
    else:
        print('wrong input')
        a=0
        return a
#==========================================Start the function of branch=========================== 

def branchs(branch):

    if branch == 'mechanical':
        b=1
        return b
    elif branch == 'civil':
        b=2
        return b
    elif branch == 'computer':
        b=3
        return b
    elif branch == 'electrical':
        b=4
        return b
    elif branch == 'eandtc':
        b=5
        return b
    elif branch == 'it':
        b=6
        return b
    elif branch == 'chemical':
        b=7
        return b
    else:
        print('invalid input')
        b = 0
        return b
#===============================End the function of branch=========================================================

#==============================Start the function of cast==========================================================

            
def casts(cast):
    if cast == 'open':
        c=1
        return c
    elif cast == 'SEBC':
        c=2
        return c
    elif cast == 'OBC':
        c=3
        return c
    elif cast == 'SBC':
        c=4
        return c
    elif cast == 'SC':
        c=4
        return c
    elif cast == 'ST':
        c=5
        return c
    elif cast == 'NTb':
        c=6
        return c
    elif cast == 'NTc':
        c=7
        return c
    elif cast == 'NTd':
        c=8
        return c
    elif cast == 'VJ':
        c=9
        return c
    else:
        c=0
        return c
#============================End of Cast function =======================================

def gend(gender):
    if gender == 'male':
        gender = 1
        return gender 
    else:
        gender = 2
        return gender
#=============================End of gender function=====================================
def attribute(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        dist = request.POST['dist']
        branch = request.POST['branch']
        cet = request.POST['cetp']
        cast = request.POST['cast']
        g = gend(gender)
        print(g)
        mm = district(dist)
        print(mm)
        b = branchs(branch)
        print(b)
        print(cet)
        Cast = casts(cast)
        print(Cast)
        

        
        

        # Taking CSV file as input
        data_set= pd.read_csv('OBC.csv')
        result = pd.read_csv('collegename.csv')
        res=pd.DataFrame(result,columns=['CC','collegeName'])
        # Print basic static information
        print("----------Basic Information about Data----------")
        print(data_set.describe())

        # Prints data about the data NaN has default data type Float
        print("----------Information about data columns----------")
        print(data_set.info())

        #Taking required columns from the dataset
        x= pd.DataFrame(data_set,columns=['BN','University', 'MHTCET','cast','Gender'])
        y=pd.DataFrame(data_set,columns=['CC'])

        #print(x_train)
        #print("Test data...................")

        #print(x_test)

        #obj_df = data_set.select_dtypes(include=['object']).copy()
        #obj_df.head()
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder

        # Encoding Categorical Data
        Clean = {"BN":     {"CSE": 3, "ME": 1, "CE": 2,"EE": 4, "ENTC": 5,"IT": 6,"CHEM": 7},
                        "University" :{"home" :1 ,"other":2},
                        "cast": {"OBC": 3, "OPEN": 1,"SEBC": 1,"SBC": 4 },
                "Gender": {"M": 1,"F":2}
                }
        x.replace(Clean, inplace=True)
        x.head()

        print(x)

        print(y)

        # Spliting data into Training and Testing set
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test=train_test_split(x,y, test_size= 0.26, random_state=0)

        #Taking data from user for testing and prediction
        #test=[['BN','University','MHTCET','cast','gender']]
        test=[[b,1,cet,Cast,g]]

        # Implementing KNN Model for recommendation
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=5)
        #knn.fit(x_train, nm.ravel(y_train,order='C'))
        knn.fit(x,nm.ravel(y,order='C'))
        y_pred = knn.predict(test)
        y_pred1=knn.predict(x_test)
        print(y_pred)

        # Accuracy Score
        print('...Accuracy Score...')
        print(metrics.accuracy_score(y_test, y_pred1))
        # Confusion Matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, y_pred1)
        print('...Confusion Matrix...')
        print(cm)

        m = result[result.CC.isin(y_pred)]
        print(m)
        n=m['collegeName']
        print(n)
        pr=str(m)
        messages.info(request,pr)
            

       
            

        


        return redirect('results')
        
    else:
        return render(request,'attribute.html')


def results(request):
    return render(request,'results.html')
        