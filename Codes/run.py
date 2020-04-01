
import numpy as np #used to import mathematical operations
import matplotlib.pyplot as plt #used to plot different things in python
import pandas as pd #import data sets and manage data sets

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout, GaussianNoise, Conv1D
from keras.preprocessing.image import ImageDataGenerator
from keras import regularizers

import matplotlib.pyplot as plt
import seaborn as sns

from keras.models import load_model
model = load_model('Job_Role_model.h5')



'''
dataset1 = pd.read_csv('para_data_test_shuffle.csv')
X_test = dataset1.iloc[: , :38].values  #independant variable vector
'''

#HERE INSTEAD OF X_TEST[0] YOU HAVE TO WRITE
#X_test= input values from the user in array format
#y=model.predict( np.array( [X_test,] ) )

y=model.predict( np.array( [X_test[0],] )  )


result = np.where(y == np.amax(y))

#Here i am printing this on the terminal but u have to put it like this on the website

if result[0]==[0]:
    print('Business Intelligence Analyst')
elif result[0]==[1]:
    print('Database Administrator')
elif result[0]==[2]:
    print('Project Manager')
elif result[0]==[3]:
    print('Security Administrator')
elif result[0]==[4]:
    print('Software Developer')
else:
    print('Technical Support')
