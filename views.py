from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
import datetime
import datetime
import re
import string
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier


# Create your views here.
from Remote_User.models import ClientRegister_Model,prediction_botnet_attack

def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/login.html')

def Add_DataSet_Details(request):

    val=''
    return render(request, 'RUser/Add_DataSet_Details.html', {"excel_data": val})


def Register1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city, address=address, gender=gender)
        obj = "Registered Successfully"
        return render(request, 'RUser/Register1.html', {'object': obj})
    else:
        return render(request,'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})


def Predict_Attack_Type(request):
    if request.method == "POST":

        if request.method == "POST":

            Fid=request.POST.get('Fid')
            stime=request.POST.get('stime')
            flgs_number=request.POST.get('flgs_number')
            proto=request.POST.get('proto')
            proto_number=request.POST.get('proto_number')
            saddr=request.POST.get('saddr')
            sport=request.POST.get('sport')
            daddr=request.POST.get('daddr')
            dport=request.POST.get('dport')
            pkts=request.POST.get('pkts')
            bytes1=request.POST.get('bytes1')
            state=request.POST.get('state')
            state_number=request.POST.get('state_number')
            ltime=request.POST.get('ltime')
            seq=request.POST.get('seq')
            duration=request.POST.get('duration')
            spkts=request.POST.get('spkts')
            dpkts=request.POST.get('dpkts')
            sbytes=request.POST.get('sbytes')
            dbytes=request.POST.get('dbytes')
            rate=request.POST.get('rate')
            srate=request.POST.get('srate')
            drate=request.POST.get('drate')
            webcategory=request.POST.get('webcategory')


            data = pd.read_csv("Datasets.csv", encoding='latin-1')

            def apply_results(results):
                if (results == 0):
                    return 0 # Botnet Attack Not Found
                elif (results == 1):
                    return 1 # Botnet Attack Found

            data['Results'] = data['Label'].apply(apply_results)

            x = data['Fid'].apply(str)
            y = data['Results']

            print(x)
            print(y)


            cv = CountVectorizer()
            x = cv.fit_transform(x)

            models = []
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
            X_train.shape, X_test.shape, y_train.shape

            print("Convolutional Neural Network (CNN)")

            from sklearn.neural_network import MLPClassifier
            mlpc = MLPClassifier().fit(X_train, y_train)
            y_pred = mlpc.predict(X_test)
            print("ACCURACY")
            print(accuracy_score(y_test, y_pred) * 100)
            print("CLASSIFICATION REPORT")
            print(classification_report(y_test, y_pred))
            print("CONFUSION MATRIX")
            print(confusion_matrix(y_test, y_pred))
            models.append(('MLPClassifier', mlpc))


            print("Gradient Boosting Classifier")

            from sklearn.ensemble import GradientBoostingClassifier
            clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(
                X_train,
                y_train)
            clfpredict = clf.predict(X_test)
            print("ACCURACY")
            print(accuracy_score(y_test, clfpredict) * 100)
            print("CLASSIFICATION REPORT")
            print(classification_report(y_test, clfpredict))
            print("CONFUSION MATRIX")
            print(confusion_matrix(y_test, clfpredict))
            models.append(('GradientBoostingClassifier', clf))


            classifier = VotingClassifier(models)
            classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)

            Fid1 = [Fid]
            vector1 = cv.transform(Fid1).toarray()
            predict_text = classifier.predict(vector1)

            pred = str(predict_text).replace("[", "")
            pred1 = pred.replace("]", "")

            prediction = int(pred1)

            if prediction == 0:
                val = 'Botnet Attack Not Found'
            elif prediction == 1:
                val = 'Botnet Attack Found'

            print(prediction)
            print(val)

            prediction_botnet_attack.objects.create(
            Fid=Fid,
            stime=stime,
            flgs_number=flgs_number,
            proto=proto,
            proto_number=proto_number,
            saddr=saddr,
            sport=sport,
            daddr=daddr,
            dport=dport,
            pkts=pkts,
            bytes1=bytes1,
            state=state,
            state_number=state_number,
            ltime=ltime,
            seq=seq,
            duration=duration,
            spkts=spkts,
            dpkts=dpkts,
            sbytes=sbytes,
            dbytes=dbytes,
            rate=rate,
            srate=srate,
            drate=drate,
            webcategory=webcategory,
            Prediction=val)

        return render(request, 'RUser/Predict_Attack_Type.html',{'objs': val})
    return render(request, 'RUser/Predict_Attack_Type.html')





