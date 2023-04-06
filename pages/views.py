# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
import joblib
import pandas as pd
import numpy as np
import keras
import csv
# import pickle

# import pandas as pd

teams =  {'Argentina': 3, 'Australia': 5,   'Belgium': 10, 'Brazil': 15, 'Cameroon': 20, 'Canada': 21, 'Costa Rica': 29, 'Croatia': 30,  'Denmark': 35, 'Ecuador': 36, 'England': 39, 'France': 46, 'Germany': 49, 'Ghana': 50, 'IR Iran': 61, 'Japan': 68, 'Korea Republic': 71, 'Mexico': 86, 'Morocco': 90,  'Netherlands': 93, 'Poland': 104, 'Portugal': 105, 'Qatar': 106,  'Saudi Arabia': 112, 'Senegal': 114, 'Serbia': 115, 'Spain': 120, 'Switzerland': 125, 'Tunisia': 131, 'USA': 134, 'Uruguay': 137, 'Wales': 141}

team_flags = {
    'Argentina': 'ar',
    'Australia': 'as',
    'Belgium': 'be',
    'Brazil': 'br',
    'Cameroon': 'cm',
    'Canada': 'ca',
    'Costa Rica': 'cs',
    'Croatia': 'hr',
    'Denmark': 'da',
    'Ecuador': 'ec',
    'England': 'uk',
    'France': 'fr',
    'Germany': 'gm',
    'Ghana': 'gh',
    'IR Iran': 'ir',
    'Japan': 'ja',
    'Korea Republic': 'ks',
    'Mexico': 'mx',
    'Morocco': 'mo',
    'Netherlands': 'nl',
    'Poland': 'pl',
    'Portugal': 'po',
    'Qatar': 'qa',
    'Saudi Arabia': 'sa',
    'Senegal': 'sg',
    'Serbia': 'rs',
    'Spain': 'sp',
    'Switzerland': 'sz',
    'Tunisia': 'tn',
    'USA': 'us',
    'Uruguay': 'uy',
    'Wales': 'wl'
}



def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {
        'teams': teams,
       })



def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

def lookUpView(request):
    with open('/home/bkim128/DjangoWorld/last_team_scores.csv', 'r') as file:
        reader = csv.reader(file)
        rows = []
        header_skipped = False
        for row in reader:
            if not header_skipped:
                header_skipped = True
                continue
            rows.append([row[0]] + row[2:])
    return render(request, 'lookup.html', {'rows': rows})


def homePost(request):

    try:
        choice = request.POST.get('choice')
        f_rank1 = request.POST.get('f_rank1')
        gk_score1 = request.POST.get('gk_score1')
        def_score1 = request.POST.get('def_score1')
        off_score1 = request.POST.get('off_score1')
        mid_score1 = request.POST.get('mid_score1')
        choice2 = request.POST.get('choice2')
        f_rank2 = request.POST.get('f_rank2')
        gk_score2 = request.POST.get('gk_score2')
        def_score2 = request.POST.get('def_score2')
        off_score2 = request.POST.get('off_score2')
        mid_score2 = request.POST.get('mid_score2')
    except:

        if not (choice and f_rank1 and gk_score1 and def_score1 and off_score1 and mid_score1 and choice2 and f_rank2 and gk_score2 and def_score2 and off_score2 and mid_score2):
        # If any of the fields are empty, display an error message
            errorMessage = 'Please fill out all fields'
            return render(request, 'home.html', {'teams': teams, 'errorMessage': errorMessage})
    else:
        return HttpResponseRedirect(reverse('results', kwargs={'choice': choice,
                                                        'f_rank1': f_rank1,
                                                        'gk_score1': gk_score1,
                                                        'def_score1': def_score1,
                                                        'off_score1': off_score1,
                                                        'mid_score1': mid_score1,
                                                        'choice2': choice2,
                                                        'f_rank2': f_rank2,
                                                        'gk_score2': gk_score2,
                                                        'def_score2': def_score2,
                                                        'off_score2': off_score2,
                                                        'mid_score2': mid_score2}))



def display_predictions(model,team1, team2, t1_rank, t2_rank, t1_gk, t2_gk, t1_def, t1_off, t1_mid, t2_def, t2_off,
                        t2_mid):
    # inputs = pd.DataFrame([[teams.get(team1), teams.get(team2), t1_rank, t2_rank, t1_gk, t2_gk, t1_def, t1_off,
    #                         t1_mid, t2_def, t2_off, t2_mid]], columns=['Team1', 'Team2', 'Team1_FIFA_RANK', 'Team2_FIFA_RANK',
    #   'Team1_Goalkeeper_Score', 'Team2_Goalkeeper_Score', 'Team1_Defense',
    #   'Team1_Offense', 'Team1_Midfield', 'Team2_Defense', 'Team2_Offense',
    #   'Team2_Midfield'])

    # score = None




    # # inputs = inputs.astype(float)
    # # ANN_pred = np.argmax(model.predict(inputs), axis=1)
    # # print(ANN_pred)
    # # score = ANN_pred
    # stacked_pred = model.predict(inputs)
    # print(stacked_pred)
    # score = stacked_pred

    # # else:
    # #     stacked_pred = model.predict(inputs)
    # #     print(stacked_pred)
    # #     score = stacked_pred
    # result = ''

    # if score == 1:
    #     return team1


    # return team2

    new_match = pd.DataFrame({'Team1': [team1], 'Team2': [team2], 'Team1_FIFA_RANK': [t1_rank], 'Team2_FIFA_RANK': [t2_rank], 'Team1_Goalkeeper_Score': [t1_gk], 'Team2_Goalkeeper_Score': [t2_gk], 'Team1_Defense': [t1_def], 'Team1_Offense': [t1_off], 'Team1_Midfield': [t1_mid], 'Team2_Defense': [t2_def], 'Team2_Offense': [t2_off], 'Team2_Midfield': [t2_mid]})
    proba = model.predict_proba(new_match)
    y_pred = model.predict(new_match)
    if y_pred == 1:
        print(f'{team1} win')
        return team1, round(proba[0][1] * 100.000, 2)
    elif y_pred == 0:
        print(f'{team2} win')
        return team2, round(proba[0][0] * 100.000, 2)
    else:
        print('Draw')
    return 'DRAW', round(proba[0][2] * 100.000, 2)

def results(request, choice, f_rank1, gk_score1, def_score1, off_score1, mid_score1, choice2, f_rank2, gk_score2, def_score2, off_score2, mid_score2):
    print("*** Inside results()")

    # ANN = keras.models.load_model('/home/bkim128/DjangoWorld/ANN_model.h5')
    # stacking = joblib.load('/home/bkim128/DjangoWorld/stacking.pkl')

    xgb = joblib.load('/home/bkim128/DjangoWorld/xgb.pkl')

    singlePrediction, probability = display_predictions(xgb, choice, choice2, f_rank1, f_rank2, gk_score1, gk_score2, def_score1, off_score1, mid_score1, def_score2, off_score2, mid_score2)



    return render(request, 'results.html', {'choice': choice,
                                            'f_rank1': f_rank1,
                                            'gk_score1': gk_score1,
                                            'def_score1': def_score1,
                                            'off_score1': off_score1,
                                            'mid_score1': mid_score1,
                                            'choice2': choice2,
                                            'f_rank2': f_rank2,
                                            'gk_score2': gk_score2,
                                            'def_score2': def_score2,
                                            'off_score2': off_score2,
                                            'mid_score2': mid_score2,
                                            'prediction': singlePrediction,
                                            'probability': probability,
                                            'winner': team_flags[singlePrediction],})
