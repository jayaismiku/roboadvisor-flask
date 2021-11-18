import pandas as pd
import matplotlib.pyplot as plt
import pickle as pc
import warnings

warnings.filterwarnings("ignore")

dataframe = pd.read_csv('static/dataset/dataset.csv')
datatest = pd.read_csv('./static/dataset/datatest.csv')

# print(datatest.head(), '\n')
# print(dataframe.columns, '\n')
# print(dataframe.isnull().sum(), '\n')
# print(dataframe.dtypes, '\n')

X = dataframe[['KelaminInt', 'MenikahInt', 'TanggunganInt', 'PendidikanInt', 'PekerjaanInt', 'PendapatanUtamaInt',
               'PemasukanTambahanInt', 'JenisPropertiInt', 'BiayaRumahTanah', 'UangMuka', 'PeriodeCicilan',
               'RiwayatPinjamanInt']]
Y = dataframe[['PersetujuanPembelianInt']]
Z = datatest[['KelaminInt', 'MenikahInt', 'TanggunganInt', 'PendidikanInt', 'PekerjaanInt', 'PendapatanUtamaInt',
              'PemasukanTambahanInt', 'JenisPropertiInt', 'BiayaRumahTanah', 'UangMuka', 'PeriodeCicilan',
              'RiwayatPinjamanInt']]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

# 3. Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn import metrics
from sklearn.metrics import accuracy_score

i = 1
mean = 0
kf = StratifiedKFold(n_splits=5, random_state=True, shuffle=True)
forester = RandomForestClassifier(random_state=True, max_depth=10)
for train_index, test_index in kf.split(X, Y):
    print('\n{} of kfold {} '.format(i, kf.n_splits))
    rf_xtr, rf_xvl = X.loc[train_index], X.loc[test_index]
    rf_ytr, rf_yvl = Y.loc[train_index], Y.loc[test_index]

    forester.fit(rf_xtr, rf_ytr)
    # # Saving model to disk
    # pc.dump(forester, open('static/model.pkl', 'wb'))

    pred_test = forester.predict(rf_xvl)
    score = accuracy_score(rf_yvl, pred_test)
    mean += score
    print('accuracy_score', score)
    i += 1
    pred_rf = forester.predict_proba(rf_xvl)[:, 1]
    pred_test_rf = forester.predict(Z)
print('\n Mean Validation Accuracy: ', mean / (i - 1))
print('\n Prediction Accuracy: ', pred_test_rf)

# Saving model to disk
pc.dump(forester, open('model.pkl', 'wb'))
# Loading model to compare the results
model = pc.load(open('model.pkl', 'rb'))
# print(model)
print('Loading model to compare the results: ', model.predict([[1, 0,	0, 5, 3, 3, 1, 1, 227000000, 62000000, 18, 1]]))

rf_fpr, rf_tpr, _ = metrics.roc_curve(rf_yvl, pred_rf)
auc = metrics.roc_auc_score(rf_yvl, pred_rf)
plt.figure(figsize=(10, 8))
plt.plot(rf_fpr, rf_tpr, label="validation, auc=" + str(auc))
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc=4)
plt.show()
