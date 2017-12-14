import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

# data = pd.read_csv('comPerMerge.csv')
# train,test = train_test_split(data,test_size=0.2)
train = pd.read_csv('out-train.csv')
test = pd.read_csv('out-test.csv')

Target=train['Is Acquired']
testTruePred = test['Is Acquired']
#
# #Take all columns as features except Name of company
Train=train[['age','category_code','competitions','acquisitions','offices','products','funding_rounds','investments'
,'number_of_employees','number_of_company']]

Test_Main=test[['age','category_code','competitions','acquisitions','offices','products','funding_rounds','investments'
,'number_of_employees','number_of_company']]

print('Input')
print(Test_Main[5276:5277])
print(Test_Main[5275:5276])

clf = svm.SVC()
X,y = Train,Target
clf.fit(X,y)
print('Model Prediction')
print(clf.predict(Test_Main[5276:5277]))
print(clf.predict(Test_Main[5275:5276]))

# print('Actual Prediction:')
# print(testTruePred[5276:5277])
# print(testTruePred[5278:5279])


