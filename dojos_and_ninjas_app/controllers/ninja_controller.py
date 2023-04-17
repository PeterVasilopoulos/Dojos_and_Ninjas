from flask import render_template, request, redirect

from dojos_and_ninjas_app.models.ninja_model import Ninja
from dojos_and_ninjas_app.models.dojo_model import Dojo

from dojos_and_ninjas_app import app

# Add new ninja form
@app.route('/new_ninja')
def new_ninja():
    dojo_list = Dojo.get_all_dojos()

    return render_template('new_ninja.html', dojo_list = dojo_list)

# Inserting new ninja into database
@app.route('/insert_ninja', methods=['POST'])
def insert_ninja():
    Ninja.create(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojo/{dojo_id}')