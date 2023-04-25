import pickle
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect,HttpResponse


# render Home Page
def home(request):
    return render(request, 'home.html')


# loading our ML model
with open(r"C:\Users\Mayurika\Downloads\Crop-Recommendation-System-master\Crop-Recommendation-System-master\saved_models\RandomForest.pkl", "rb") as file:
    model = pickle.load(file)

# render Predtion Page


def predictor(request):
    return render(request, 'main.html')


def formInfo(request):
    context = {}
    if request.method == 'GET':
        N = float(request.GET['N'])
        P = float(request.GET['P'])
        K = float(request.GET['K'])
        T = float(request.GET['T'])
        H = float(request.GET['H'])
        Ph = float(request.GET['Ph'])
        R = float(request.GET['R'])

    y_pred = model.predict([[N, P, K, T, H, Ph, R]])
  #  print(y_pred)

    context = {
        'crop_result': "Crop Recommended :  "+y_pred[0]
    }
    return render(request, 'main.html', context)


def plantde(request):
    # context = {"message": "This is a dictionary"}
    return render(request, 'plantde.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
