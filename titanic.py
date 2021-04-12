import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn import model_selection
from sklearn import ensemble 
from sklearn import linear_model
from sklearn.svm import SVC

import numpy as np
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
full=train.append(test,ignore_index = True)
print(full.shape)
print(full.head(n=1309))


names=full.columns
null_count=full.isnull().sum()
null_pct=full.isnull().mean()
null_count.name='Null Count'
null_pct.name='Null Percent'
nulls=pd.concat([null_count,null_pct],axis=1)
print(nulls)


print(full.describe(include='all'))
print(full[full['Embarked'].isnull()|full['Fare'].isnull()])


full['Fare']=full.groupby(['Pclass'])['Fare'].transform(lambda x: x.fillna(x.median()))
print(full['Fare'])


print(full[full['Name'].str.contains('Stone') | full['Name'].str.contains('Icard') | full['Ticket'].str.contains('113572')])
full['Embarked']=full['Embarked'].fillna(full['Embarked'].mode()[0])

print(full['Embarked'].value_counts())


names=full.columns
null_count=full.isnull().sum()
null_pct=full.isnull().mean()
null_count.name='Null Count'
null_pct.name='Null Percent'
nulls=pd.concat([null_count,null_pct],axis=1)
print(nulls)


full['Sex']=full['Sex'].map({'male' :0,'female' : 1}).astype(int)
full['FamilySize']=full['Parch']+full['SibSp']+1
full.drop(['Parch','SibSp'],axis=1,inplace=True)
print(full.corr())


plt.show(full['Fare'].hist(bins=50,grid=False));
print(full[full['Fare']>=250].sort_values('Fare'))


full['CabinCode']=full[full['Cabin'].notnull()].Cabin.astype(str).str[0]
print(full['CabinCode'].replace(np.NaN,'U',inplace=True))


full['Title']=full.Name.str.extract('([A-Za-z]+)\.',expand=False)
full['FamilyName']=full.Name.str.extract('([A-Za-z]+)',expand=False)
print(full['Title'].value_counts())


replacements=[[['Mr'],['Capt','Col','Don','Dr','Jonkheer','Major','Sir']],
             [['Miss'],['Dona','Lady','Mlle','Ms']],[['Mrs'],['Countess','Mme']]
              ]
for title,replacement in replacements:
	full['Title']=full['Title'].replace(replacement,''.join(title))

print(full['Title'].value_counts())

print(full[full['Title'].isin(['Rev'])])

full['FamilySurvivalRate']=full.groupby(['FamilyName'])['Survived'].transform(lambda x:x.mean())
print(full['FamilySurvivalRate'].fillna(value=.5,inplace=True))You must create a model which predicts a probability of each type of toxicity for each comment.

full.loc[full['Title'] =='Rev','FamilySurvivalRate']=0
print(full[full['Title']=='Rev'])

full['Age']=full.groupby(['Pclass','Sex','Title'])['Age'].transform(lambda x:x.mean())
full.drop(['Cabin','FamilyName','Name','Ticket','Title'],axis=1,inplace=True)
print(full.corr())

def plot_distribution(df,var,target,**kwargs):
	row=kwargs.get('row',None)
	col=kwargs.get('col',None)
	facet=sns.FacetGrid(df,hue=target,aspect=4,row=row,col=col)
	facet.map(sns.kdeplot,var,shade=True)
	facet.set(xlim=(0,df[var].max() ))
	plt.show(facet.add_legend())
plt.show(plot_distribution(full[full['Survived'].notnull()],var='Age',target='Survived',row='Sex'))

plt.show(plot_distribution(full[full['Survived'].notnull()],var='Fare',target='Survived'))

def plot_bars(df,var,target,**kwargs):
	col=kwargs.get('col',None)
	sns.set()
	sns.set_style('white')
	sns.set_context('notebook')
	colors=['sky blue','light pink']
	sns.barplot(data=df,x=var,y=target,hue=col,ci=None,palette=sns.xkcd_palette(colors))
	sns.despine()

plt.show(plot_bars(full[full['Survived'].notnull()],'Embarked','Survived',col='Sex'))


plt.show(plot_bars(full[full['Survived'].notnull()],'Pclass','Survived',col='Sex'))

full=pd.concat((full,pd.get_dummies(data=full['Pclass'],prefix='Pclass')),axis=1)
full.drop('Pclass',axis=1,inplace=True)
print(full.head())

X_train=full[full['Survived'].notnull()].copy()

X_train.drop(['Embarked','PassengerId','CabinCode','Survived'],axis=1,inplace=True)

Y_train=full[full['Survived'].notnull()].Survived.copy()

X_test=full[full['Survived'].isnull()].copy()

X_test.drop(['Embarked','PassengerId','CabinCode','Survived'],axis=1,inplace=True)

models=[ensemble.RandomForestClassifier(n_estimators=100),ensemble.GradientBoostingClassifier(),
          linear_model.LogisticRegression(),SVC()]


for model in models:
	model_name=model.__class__.__name__
	model.fit(X_train,Y_train)
	model_score=model.score(X_train,Y_train)
	accuracy=model_selection.cross_val_score(model,X_train,Y_train,scoring='accuracy',cv=10).mean()*100
	Y_pred=model.predict(X_test).astype(int)
	submission=pd.DataFrame({ 'PassengerId':test['PassengerId'],'Survived':Y_pred})
	submission.to_csv('./'+ model_name + '_submission.csv',index=False)

	print('*' * 10,model_name,'*' * 10)
	print('Model score is:',model_score)
	print('Cross validation accuracy is:',accuracy)