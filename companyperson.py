
import pandas as pd
import math
import numpy as np
import csv

# include the category code ... category_code
fields = ['name', "founded_year",'number_of_employees',"category_code","acquisition","acquisitions",
          "milestones","competitions","offices","products","funding_rounds","investments","providerships","relationships"]
company = pd.read_csv('/company.csv',skipinitialspace=True, usecols=fields)
companyDataFrame = pd.DataFrame(company)

companyDataFrame1 = companyDataFrame[['name', "founded_year",'number_of_employees',"category_code","acquisition","acquisitions",
                                      "milestones","competitions","offices","products","funding_rounds","investments","providerships","relationships"]].copy()

mergeDataFrame = pd.DataFrame(columns=('name', 'age',"milestones","competitions","category_code","acquisition",
                                       "acquisitions","offices","products","providerships"
                                       ,"funding_rounds","investments","Funding per round","first_name","last_name",
                                       "number_of_employees","Is Acquired"))

for index, row in companyDataFrame1.iterrows():
    totalFund=0
    # if(row.notnull().values.any()):
    name=row[0]
    relationshList = row.relationships.split(",")
    if len(str(relationshList)) > 6:
        for r in relationshList:
            if "first_name" in r:
                r = r.split(":")
                firstName = r[2].replace("'", "")
            if "last_name" in r:
                r = r.split(":")
                r[1] = r[1].replace("'", "")
                lastName = r[1]
    else:
        firstName="nan"
        lastName="nan"
    if len(str(row.acquisition)) > 3:
        acquisition = (row["acquisition"].count("acquired_year"))
        list = row.acquisition.split(",")
        for k in list:
            if "acquired_year" in k and len(str(row.founded_year)) > 3:
                k = k.split(":")
                if not (k[1] == " None"):
                    year = k[1]
                    age = (int(year) - int(row.founded_year))
            else:
                if len(str(row.founded_year)) > 3:
                    age = (int(2017) - int(row.founded_year))
                else:
                    age = 0
    else:
        acquisition=0
        if len(str(row.founded_year)) > 3:
            age = (int(2017) - int(row.founded_year))
        else:
            age = 0

milestones = (row["milestones"].count("stoned_year"))
competitions = (row["competitions"].count("competitor"))
acquisitions = (row["acquisitions"].count("acquired_year"))
offices = (row["offices"].count("offices"))
products = (row["products"].count("products"))
providers = (row["providerships"].count("provider"))
funding_rounds = (row["funding_rounds"].count("funded_year"))
investments = (row["investments"].count("funded_year"))
fundList = row.funding_rounds.split(",")
for f in fundList:
    if "raised_amount" in f:
        f = f.split(":")
        if not (f[1] == " None"):
            totalFund = float(totalFund) + float(f[1])


if acquisition > 0:
    isAcquired = True
    else:
        isAcquired = False
mergeDataFrame.loc[-1] = \
[name, age, milestones, competitions, row[3], acquisition, acquisitions, offices,
 products, providers, funding_rounds, investments, totalFund, firstName, lastName, row[2], isAcquired]
    mergeDataFrame.index = mergeDataFrame.index + 1  # shifting index
    mergeDataFrame = mergeDataFrame.sort_index()


mergeDataFrame=mergeDataFrame.drop_duplicates()
outputCSV=mergeDataFrame.values.tolist()
writer = csv.writer(open('/companyFinal.csv', 'w'))
writer.writerow(['name', 'age',"milestones","competitions","category_code","acquisition",
                 "acquisitions","offices","products","providerships"
                 ,"funding_rounds","investments","Total Fund","first_name",
                 "last_name","number_of_employees","isAcquired"])

for row in outputCSV:
    writer.writerow(row)


fieldP=['first_name','last_name','relationships']
person = pd.read_csv('/person.csv',skipinitialspace=True, usecols=fieldP)
personDataFrame=pd.DataFrame(person)
# headers = personDataFrame.dtypes.index
# print(headers)
# personDataFrame1 = personDataFrame[['first_name','last_name','relationships']].copy()

mergePersonDataFrame = pd.DataFrame(columns=('first_name','last_name','number_of_company'))
for index, row in personDataFrame.iterrows():
    if row.notnull().values.all():
        number_of_company = (row["relationships"].count("firm"))
        mergePersonDataFrame.loc[-1] = [row.first_name,row.last_name,number_of_company]
        mergePersonDataFrame.index = mergePersonDataFrame.index + 1  # shifting index
        mergePersonDataFrame = mergePersonDataFrame.sort_index()


finalDF=pd.merge(mergeDataFrame, mergePersonDataFrame, on=['first_name','last_name'], how='inner')
outputCSV=finalDF.values.tolist()
writer = csv.writer(open('/9990.csv', 'w'))
writer.writerow(['name', 'age',"milestones","competitions",
                 "acquisitions","offices","products","providerships"
                 ,"funding_rounds","investments","acquisitions","Funding per round","firstName",
                 "lastName","number_of_company"])

for row in outputCSV:
    writer.writerow(row)

mergePersonDataFrame=mergePersonDataFrame.drop_duplicates()
outputCSV=mergePersonDataFrame.values.tolist()
writer = csv.writer(open('personFinal.csv', 'w'))
                         writer.writerow(['first_name','last_name','number_of_company'])
                         
                         for row in outputCSV:
                         writer.writerow(row)

