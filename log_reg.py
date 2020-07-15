from sklearn.linear_model import LogisticRegression
import pandas as pd 

data=pd.read_csv('C:\\Users\\TITAS\\Downloads\\iris.csv')
print(data)
data.keys()
m='species'
y=data[m]
x=data.drop(['species'],axis=1)

print(y)
print(x)
clf = LogisticRegression(random_state=0).fit(x, y)
p=clf.predict([[5.0,3.6,1.4,0.2]])
print(y[5])
print(p)
d=clf.predict_proba([[5.0,3.6,1.4,0.2]])
print(d)
clf.score(x, y)

#push to github
