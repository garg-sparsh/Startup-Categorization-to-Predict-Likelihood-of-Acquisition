
import pandas as pd
import math
import numpy as np
import csv

path = '/Users/prakharmaheshwari/Desktop/PROJECTS/PATTERN-PROJECT/DATASETS/csvfiles'
finalCSV = pd.read_csv(path+'/comPerMerge.csv',skipinitialspace=True)
initialDF=pd.DataFrame(finalCSV)


IsAcquiredDF = initialDF[initialDF['Is Acquired'] == True]
IsNotAcquiredDF = initialDF[initialDF['Is Acquired'] == False]

outputCSV=IsAcquiredDF.values.tolist()
writer = csv.writer(open(path+'/IsAcquired.csv', 'w'))
writer.writerow(['name', 'age',"milestones","competitions","acquisition",
                     "acquisitions","offices","products","providerships"
                    ,"funding_rounds","investments","acquisitions","Funding per round","firstName",
                    "lastName","number_of_employees","Is Acquired","number_of_company,"])

for row in outputCSV:
    writer.writerow(row)

outputCSV=IsNotAcquiredDF.values.tolist()
writer = csv.writer(open(path+'/IsNotAcquired.csv', 'w'))
writer.writerow(['name', 'age',"milestones","competitions","acquisition",
                     "acquisitions","offices","products","providerships"
                    ,"funding_rounds","investments","acquisitions","Funding per round","firstName",
                    "lastName","number_of_employees","Is Acquired","number_of_company,"])

for row in outputCSV:
    writer.writerow(row)