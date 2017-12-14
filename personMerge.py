
import pandas as pd
import math
import numpy as np
import csv


personMerge = pd.read_csv('/personFinal.csv',skipinitialspace=True)
personMergeFrame=pd.DataFrame(personMerge)
mergeDataFrame=personMergeFrame.drop_duplicates();


companyMerge = pd.read_csv('/companyFinal.csv',skipinitialspace=True)
companyMergeFrame=pd.DataFrame(companyMerge)

mergeDataFrame=personMergeFrame.drop_duplicates();
personMergeFrame['first_name'] = personMergeFrame['first_name'].astype(str)
companyMergeFrame['first_name'] = companyMergeFrame['first_name'].astype(str)

personMergeFrame['last_name'] = personMergeFrame['last_name'].astype(str)
companyMergeFrame['last_name'] = companyMergeFrame['last_name'].astype(str)

personMergeFrame=personMergeFrame.drop_duplicates(subset=['first_name','last_name'],keep='last');

finalDF=pd.merge(companyMergeFrame, personMergeFrame, on=['first_name','last_name'],how='inner')
finalDF = finalDF.replace("nan",0)
finalDF = finalDF.replace(np.nan,0)
outputCSV=finalDF.values.tolist()
writer = csv.writer(open('comPerMerge.csv', 'w'))
writer.writerow(['name', 'age',"milestones","competitions","category_code","acquisition",
                     "acquisitions","offices","products","providerships"
                    ,"funding_rounds","investments","Funding per round","firstName",
                    "lastName","number_of_employees","Is Acquired","number_of_company"])

for row in outputCSV:
    writer.writerow(row)
