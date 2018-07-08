print("Question1")
import pandas as pd
import numpy as np

context = {
        'col-1':['name','age','mail-id','phn_no'],
        'col-2':['sam','20','sam@gmail.com','22334422'],
        'col-3':['ana','20','ana@gmail.com','66884433'],
        'col-4':['vats','20','vats@gmail.com','998875'],
        'col-5':['shr','20','shr@gmail.com','334409']
        }

data_frame = pd.DataFrame(context)
print(data_frame)
print('\n')

print("Question2")
import pandas as pd
import numpy as np

data = pd.read_csv('weather.csv')
data_frame1 = pd.DataFrame(data)
print(data_frame1.head())
print(data_frame1.head(10))
print("Basic Statistics of dataset")
print("Sum of dataset",data_frame1.sum())
print("Mean of dataset",data_frame1.mean())
print("Description of dataset",data_frame1.
      describe(include='all'))
print(data_frame1.tail())
print(data_frame1.loc[:,['Location']].describe())
