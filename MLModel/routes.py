import numpy as np
from flask import render_template, redirect, url_for, flash

from MLModel import app, load_model
from MLModel.forms import DataForm

flower = {1: 'Iris-Setosa', 2: 'Iris-Versicolor', 3: 'Iris-Virginica'}


@app.route('/', methods=['POST', 'GET'])
def predict():
    form = DataForm()
    if form.validate_on_submit():
        sl = form.sepal_length.data
        sw = form.sepal_width.data
        pl = form.petal_length.data
        pw = form.petal_width.data
        data = np.array([sl, sw, pl, pw])
        data = data.reshape(1, -1)
        model = load_model()
        prediction = model.predict(data)
        flash(f'Flower: {flower[prediction[0]]}, Specifications: Sepal Length- {sl}, Sepal Width- {sw}, Petal Length- {pl}, Petal Width- {pw}', 'success')
        return redirect(url_for('predict'))
    return render_template('DataForm.html', form=form)
