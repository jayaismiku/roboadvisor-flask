# save this as app.py
import pickle
import numpy as np
from flask import Flask, render_template, request

model = pickle.load(open('model.pkl', 'rb'))
print(model)

app = Flask(__name__)

@app.route("/")
def home():
    # return "Hello, World!"
    return render_template('index.html')


@app.route("/coba-beli")
def form():
    return render_template('form.html')


@app.route("/predict", methods=['post'])
def predict():
    # read the posted values from the UI
    _namalengkap = request.form['namalengkap']
    _kelamin = request.form['kelamin']
    _nikah = request.form['nikah']
    _tanggungan = request.form['tanggungan']
    _pendidikan = request.form['pendidikan']
    _pekerjaan = request.form['pekerjaan']
    _pendapatanutama = request.form['pendapatanutama']
    _pendapatantambahan = request.form['pendapatantambahan']
    _jenisproperti = request.form['jenisproperti']
    _nup = request.form['nup']
    _bookingfee = request.form['bookingfee']
    _hargarumah = request.form['hargarumah']
    _uangmuka = request.form['uangmuka']
    _periodecicilan = request.form['periodecicilan']
    _cicilanlain = request.form['cicilanlain']

    data_form = [_kelamin, _nikah, _tanggungan, _pendidikan, _pekerjaan, _pendapatanutama, _pendapatantambahan, _jenisproperti, _hargarumah, _uangmuka, _periodecicilan, _cicilanlain]
    final_features = [np.array(data_form)]
    prediction = model.predict(final_features)

    # print(model.predict([[1, 0,	0, 5, 3, 3, 1, 1, 227000000, 62000000, 18, 1]]))
    # output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Perkiraan persetujuan pembelian rumah adalah {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
