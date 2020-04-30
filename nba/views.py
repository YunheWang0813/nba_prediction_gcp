from flask import request, redirect, url_for, render_template, flash
from nba import app, db
from nba.models import Menu
import random
import requests
import json


@app.route('/')
def show_lootbox():
    return render_template('show_selection.html')

# @app.route('/post', methods=['POST'])
# def post():
#     a = request.form['myData']
#     print(a)
#     return result(a)

def space_helper(name):
    return name.replace(" ", "%20")

@app.route('/result/<name1>/<name2>', methods=['GET'])
def result(name1, name2):

    string = 'https://bajrakawc7.execute-api.us-east-1.amazonaws.com/test/nba-match?' + 'Team=' + space_helper(name1) + '&Oppt=' + space_helper(name2)
    print('https://bajrakawc7.execute-api.us-east-1.amazonaws.com/test/nba-match?Team=Atlanta%20Hawks&Oppt=Oklahoma%20City%20Thunder')
    r = requests.get(string)
    item = json.loads(r.text)['Item']
    
    score1 = item["Team"]
    score2 = item["Oppt"]

    team_win_ratio = item["oppt_loss_probability"]  # Team win ratio
    oppt_win_ratio = item["team_loss_probability"]  # Oppt win ratio
    score3 = round(float(team_win_ratio) * 100, 2)
    score4 = round(float(oppt_win_ratio) * 100, 2)
    
    # score5 = space_helper(name1)
    # score6 = space_helper(name2)

    team_ast = item["team_AST%"]  # Team assist%
    oppt_ast = item["oppt_AST%"]  # Oppt assist%
    score5 = round(float(team_ast) * 100, 2)
    score6 = round(float(oppt_ast) * 100, 2)

    team_offrtg = item["team_OffRtg"]  # Team offensive rating
    oppt_offrtg = item["oppt_OffRtg"]  # Oppt offensive rating
    score7 = round(float(team_offrtg) * 100, 2)
    score8 = round(float(oppt_offrtg) * 100, 2)

    team_defrtg = item["team_DefRtg"]  # Team defensive rating
    oppt_defrtg = item["oppt_DefRtg"]  # Oppt defensive rating
    score9 = round(float(team_defrtg) * 100, 2)
    score10 = round(float(oppt_defrtg) * 100, 2)

    return render_template('show_result.html', score1=score1, score2=score2, score3=score3, score4=score4, score5=score5, score6=score6, score7=score7, score8=score8, score9=score9, score10=score10)