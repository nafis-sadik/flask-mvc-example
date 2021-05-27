from flask import render_template
from Application import app

from Application.Models.BaseModel import BaseModel
from Services import IUserManager
from Services.UserManager import UserManager

Model = BaseModel()


@app.route('/', methods=['GET'])
def Index():
    Model.PageTitle = 'Home'
    return render_template('Index.html', model=Model)
