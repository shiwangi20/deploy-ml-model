from flask import Flask
import pickle

app = Flask(__name__)
model = None
app.config['SECRET_KEY'] = '468c710afb86dcbc10f7c3db1aa394f3'


def load_model():
    global model
    filename = 'MLModel/iris_trained_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model


from MLModel import routes
