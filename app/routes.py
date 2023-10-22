from flask import Blueprint, jsonify 

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index(): 
    return "Hello Backend"

@main.route('/about_me', methods=['POST'])
def about_me():
    reponse = {
        'name': 'Lu Xinming',
        'course': "Quantitative Finance",
        'Year': 1,
        'CCAs': ['RHDevs', 'ComMotion', 'Squash', 'Sets', 'Culture Committee']
    }
    return jsonify(reponse)