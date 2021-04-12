import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

white=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')

red=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

np.random.seed(570)
redlabels=np.unique(red['quality'])

whitelabels=np.unique(white['quality'])

fig,ax=plt.subplots(1,2,figsize=(8,4))
redcolors=np.random.rand(6,4)
whitecolors=np.append(redcolors,np.random.rand(1,4),axis=0)
for i in range(len(redcolors)):
	redy=red['alcohol'][red.quality==redlabels[i]]
	redx=red['volatile acidity'][red.quality==redlabels[i]]
	ax[0].scatter(redx,redy,c=redcolors[i])

for j in range(len(whitecolors)):
	whitey=white['alcohol'][white.quality==whitelabels[j]]
	whitex=white['volatile acidity'][white.quality==whitelabels[j]]
	ax[1].scatter(whitex,whitey,c=whitecolors[j])

ax[0].set_title("red wine")
ax[1].set_title("white wine")
ax[0].set_xlim([0,1.7])
ax[1].set_xlim([0,1.7])
ax[0].set_ylim([5,15.5])
ax[1].set_ylim([5,15.5])
ax[0].set_xlabel("volatile acidity")
ax[0].set_ylabel("alcohol")
ax[1].set_xlabel("volatile acidity")
ax[1].set_ylabel("alcohol")
ax[1].legend(whitelabels,loc='best',bbox_to_anchor=(1.3,1))
fig.subplots_adjust(top=0.85,wspace=0.7)


red['type']=1
white['type']=0
wines=red.append(white,ignore_index=True)

corr=wines.corr()
X=wines.iloc[:,0:11]
y=np.ravel(wines.type)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)

from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

scaler=StandardScaler().fit(X_train)

X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)
	
model=Sequential()
model.add(Dense(12,activation='relu',input_shape=(11,)))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
