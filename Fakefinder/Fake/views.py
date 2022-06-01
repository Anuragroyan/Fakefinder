from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from Fake.forms import UserForm
# Create your views here.

def home(request):
    return render(request, 'fakefinder/base.html')


def index(request):
    return render(request, 'fakefinder/index.html')    

def predict(request):
    if request.method == 'POST':
        file = open('final_model_text.sav', 'rb')
        cls = pickle.load(file)
        Text = request.POST["content"]
        ans=cls.predict([Text])
        df = pd.read_csv('news_datasets.csv')
        X_train, X_test, y_train, y_test = train_test_split(df['text'],df['label'], test_size=0.33, random_state=54)
        y_pred = cls.predict(X_test)
        acc = cls.score(y_test, y_pred) * 100
        context={'t':Text,'a':ans,'acc':acc}
        return render(request, 'fakefinder/predict.html',context)
    else:
        return render(request, 'fakefinder/predict.html') 
        
