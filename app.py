import flask
from flask import render_template
import pickle
import sklearn
import sklearn.linear_model 
from sklearn.linear_model import LinearRegression

app = flask.Flask(__name__, template_folder='templates')

@app.route('/',methods = ['POST', 'GET'])

@app.route('/index',methods = ['POST', 'GET'] )
def main():
    if flask.request.method =='GET':
        return render_template('main.html')

    if flask.request.method =='POST':
        with open('modelNN.pkl','rb') as f:
            loaded_model = pickle.load(f)  
        a1 = float(flask.request.form['Модуль упругости при растяжении, ГПа'])
        a2 = float(flask.request.form['Плотность, кг/м3'])
        a3 = float(flask.request.form['модуль упругости, ГПа'])
        a4 = float(flask.request.form['Количество отвердителя, м.%'])
        a5 = float(flask.request.form['Содержание эпоксидных групп,%_2'])
        a6 = float(flask.request.form['Температура вспышки, С_2'])
        a7 = float(flask.request.form['Поверхностная плотность, г/м2'])
        a8 = float(flask.request.form['Потребление смолы, г/м2'])
        a9 = float(flask.request.form['Угол нашивки, град'])
        a10 = float(flask.request.form['Шаг нашивки'])
        a11 = float(flask.request.form['Плотность нашивки'])
        a12 = float(flask.request.form['Прочность при растяжении, МПа'])
        y_pred = loaded_model.predict([[a1,a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,a12]])


        return render_template('main.html', result = y_pred)

if __name__ == '__main__' :
    app.run()           