  
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder='Template')
def model_selection(name):
    if (name=='randomforest'):
        model= pickle.load(open('model_1.pkl', 'rb'))
    elif (name== 'elasticnet'):
        model=pickle.load(open('model_2.pkl', 'rb'))
    else:
        model=pickle.load(open('model_3.pkl', 'rb'))
    return model

        
          


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def prediction():
    '''
    For rendering results on HTML GUI
    '''
    if request.method== 'POST':
        watertemp= float(request.form['watertemp'])
        turbidity= float(request.form['turbidity'])
        coliform= float(request.form['coliform'])
        color= float(request.form['color'])
        enterococci= float(request.form['enterococci'])
        ecoli_fast_1= float(request.form['ecoli_fast_1'])
        ecoli_fast_2= float(request.form['ecoli_fast_2'])

        regressor= request.form['algorithms']
        model=model_selection(regressor)
        prediction = model.predict([[watertemp, turbidity, coliform, color, enterococci, ecoli_fast_1, ecoli_fast_2]])
        
        output=round(prediction[0],2)
        if output > 4.2:
            return render_template('index.html', prediction_text='The E. coli levels is {} is not safe for drinking'.format(output))
        else:

            return render_template('index.html', prediction_text='The E. coli levels is {} is safe for drinking'.format(output))

        else:
            return render_template('index.html')


if __name__=="__main__":        
    app.run(debug=True)
    
    