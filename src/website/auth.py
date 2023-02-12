from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint('auth', __name__)

@auth.route('/lecture_halls', methods=['GET', 'POST'])
def halls():
    if request.method == 'POST':
        first_point = request.form.get('firstPoint')
        second_point = request.form.get('secondPoint')
        if first_point == "Cabinet_A" and second_point == "Cabinet_B":
            return render_template("AB.html")
        elif first_point == "Cabinet_A" and second_point == "Cabinet_C":
            return render_template("AC.html")

        else:
            return redirect(url_for('views.home'))       
    return render_template("lecture_halls.html")

@auth.route('/toilets', methods=['GET', 'POST'])
def toilets():
    if request.method == 'POST':
        first_point = request.form.get('firstPoint')
        second_point = request.form.get('secondPoint')
        if first_point == "Cabinet_A" and second_point == "Cabinet_B":
            return render_template("AB.html")
        elif first_point == "Cabinet_A" and second_point == "Cabinet_C":
            return render_template("AC.html")

        else:
            return redirect(url_for('views.home'))        
    return render_template("toilets.html")

@auth.route('/canteen', methods=['GET', 'POST']) 
def canteen():
    if request.method == 'POST':
        first_point = request.form.get('firstPoint')
        second_point = request.form.get('secondPoint')
        if first_point == "Cabinet_A" and second_point == "Cabinet_B":
            return render_template("AB.html")
        elif first_point == "Cabinet_A" and second_point == "Cabinet_C":
            return render_template("AC.html")

        else:
            return redirect(url_for('views.home'))

    return render_template("canteen.html")