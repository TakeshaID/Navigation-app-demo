from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__) #don't have to name view but that it is simpler\

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        first_point = request.form.get('firstPoint')
        second_point = request.form.get('secondPoint')
        if first_point == "Cabinet_A" and second_point == "Cabinet_B":
            return render_template("AB.html")
        elif first_point == "Cabinet_A" and second_point == "Cabinet_C":
            return render_template("AC.html")
    
    return render_template("home.html")



