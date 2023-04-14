from flask import render_template, request, redirect

from dojos_and_ninjas_app.models.dojo_model import Dojo

from dojos_and_ninjas_app import app

# Default page redirects to dojo page
@app.route('/')
def dojo_redirect():
    return redirect('/dojo')

# Home page to view all dojos and add dojo
@app.route('/dojo')
def dojo():
    dojo_list = Dojo.get_all_dojos()

    return render_template('dojo.html', dojo_list = dojo_list)

# View a single dojo
@app.route('/dojo/<int:id>')
def dojo_id(id):

    return render_template('/dojo_details.html')

# Creating a new dojo
@app.route('/create', methods=['POST'])
def create():
    Dojo.create(request.form)
    return redirect('/dojo')