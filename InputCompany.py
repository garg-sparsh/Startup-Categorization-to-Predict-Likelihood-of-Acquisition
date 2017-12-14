'''import pandas as pd
import numpy as np
from scipy.stats import norm
a= input("Ask:")


path = '/Users/sparshgarg/Downloads/'
finalCSV = pd.read_csv(path+'/comPerMerge-1.csv',skipinitialspace=True)
finalDF=pd.DataFrame(finalCSV)
finalDF1=finalDF.copy()
c=0;
for i in finalDF1.name:
    c = c + 1
    if i==a:
        break
dlist=finalDF1.index[finalDF1['category_code'] != finalDF1.category_code[c-1]].tolist()
finalDF1 = finalDF1.drop(dlist)

number_of_employees=finalDF1.number_of_employees

a=np.array([finalDF1.age,finalDF1.investments,finalDF1.number_of_employees,finalDF1.offices,finalDF1.products,
            finalDF1.funding_rounds,finalDF1.number_of_company])
ratings = np.append(new_ratings,a)
#b=np.transpose(a)

#print(a.shape)
def normalize(a):
    num_movies = a.shape[0]
    ratings_mean = np.zeros(shape=(num_movies,1))
    ratings_norm= np.zeros(shape=a.shape)
    ratings_std = np.zeros(shape=(num_movies,1))
    for i in range(num_movies):
        idx = np.where(a[i]!=0 )[0]
        ratings_mean[i] = np.mean(a[i,idx])
        ratings_std[i] = np.std(a[i,idx])
        ratings_norm[i,idx] = norm.pdf(a[i,idx],ratings_mean[i],ratings_std[i])
        ratings_norm[i, idx] = ratings_norm[i,idx]/ratings_mean[i]
    return ratings_norm,ratings_mean


p=[]
ratings_norm,ratings_mean=normalize(a)
for i in ratings_norm:
    b=max(i)
    if b is not 0:
        p.append(i/b)
    else:
        p.append(0)

q = np.asarray(p)
r = np.transpose(q)
final_company = r[c-1,:]
print(final_company)
print(type(final_company))
for k in final_company:
    print('k=',k,",,",type(k))
idx = np.where(final_company != 0)[0]
print(idx)
print(np.prod(final_company[idx]))
#print(r[c-1,:])
for i in range(len(r)):
    idx = np.where(r[i] != 0)[0]
    #print("idx=",idx)
    #print("r[i]=",r[i])
    prediction = np.prod(r[i,idx])
   # print("prediction",finalDF1.name[i],":",prediction)
print("r=",r)'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from scipy.stats import norm
rating_user = np.zeros((7,1))
file=open( 'test5.csv', "r")
reader = csv.reader(file)
category=''
for line in reader:
    rating_user[0] = line[0]
    rating_user[1] = line[1]
    rating_user[2] = line[2]
    rating_user[3] = line[3]
    rating_user[4] = line[4]
    rating_user[5] = line[5]
    rating_user[6] = line[6]
    category=line[7]

c=0
path = '/Users/sparshgarg/Downloads/'
finalCSV = pd.read_csv(path+'/comPerMerge-1.csv',skipinitialspace=True)
finalDF1=pd.DataFrame(finalCSV)
finalDF=finalDF1.copy()
#category = str(finalDF1.category_code[c-1])
dlist=finalDF.index[finalDF['category_code'] != category].tolist()
finalDF.drop(dlist)
number_of_employees=finalDF.number_of_employees
a=np.array([finalDF.age,finalDF.investments,finalDF.number_of_employees,finalDF.offices,finalDF.products,
            finalDF.funding_rounds,finalDF.number_of_company])
a = np.append(rating_user,a,axis=1)
def normalize(a):
    num_movies = a.shape[0]
    ratings_mean = np.zeros(shape=(num_movies,1))
    ratings_norm= np.zeros(shape=a.shape)
    ratings_std = np.zeros(shape=(num_movies,1))
    for i in range(num_movies):
        idx = np.where(a[i]!=0 )[0]
        ratings_mean[i] = np.mean(a[i,idx])
        ratings_std[i] = np.std(a[i,idx])
        ratings_norm[i,idx] = norm.pdf(a[i,idx],ratings_mean[i],ratings_std[i])
        ratings_norm[i, idx] = ratings_norm[i,idx]/ratings_mean[i]
    return ratings_norm,ratings_mean


p=[]
final=[]
ratings_norm,ratings_mean=normalize(a)
#print(ratings_mean)
for i in ratings_norm:
    b=max(i)
    p.append(i/b)
q = np.asarray(p)
r = np.transpose(q)
for i in range(len(r)):
    idx = np.where(r[i] != 0)[0]
    #print("idx=",idx)
    #print("r[i]=",r[i])
    prediction = np.prod(r[i,idx])
    final.append(prediction)
print()
print("Probability of company acquisition=",final[0]**2)