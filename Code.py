# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ya0xUIfB1_ZrVpdvqAPskpIHqQQ12wM6
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print("Shape of train: ", train.shape)
print("Shape of test: ", test.shape)

train_ID = train['Id']
test_ID = test['Id']
train.drop("Id", axis = 1, inplace = True)
test.drop("Id", axis = 1, inplace = True)

fig, ax = plt.subplots()
ax.scatter(x = train['GrLivArea'], y = train['SalePrice'])
plt.ylabel('SalePrice', fontsize=13)
plt.xlabel('GrLivArea', fontsize=13)
plt.show()

train = train.drop(train[(train['GrLivArea']>4000) & (train['SalePrice']<300000)].index)
fig, ax = plt.subplots()
ax.scatter(train['GrLivArea'], train['SalePrice'])
plt.ylabel('SalePrice', fontsize=13)
plt.xlabel('GrLivArea', fontsize=13)
plt.show()

from scipy import stats
from scipy.stats import norm
sns.distplot(train['SalePrice'] , fit = norm)
(mu, sigma) = norm.fit(train['SalePrice'])
print('mu = {:.2f} and sigma = {:.2f}'.format(mu, sigma))
plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')
fig = plt.figure()
res = stats.probplot(train['SalePrice'], plot = plt)
plt.show()

train["SalePrice"] = np.log1p(train["SalePrice"])
sns.distplot(train['SalePrice'] , fit = norm)
(mu, sigma) = norm.fit(train['SalePrice'])
print('mu = {:.2f} and sigma = {:.2f}'.format(mu, sigma))
plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')
fig = plt.figure()
res = stats.probplot(train['SalePrice'], plot = plt)
plt.show()

ntrain = train.shape[0]
ntest = test.shape[0]
y_train = train.SalePrice.values
combine = pd.concat([train, test])
combine.drop(['SalePrice'], axis = 1, inplace =  True)
combine.shape

combine_na = (combine.isnull().sum() / len(combine)) * 100
combine_na = combine_na.drop(combine_na[combine_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio' :combine_na})
missing_data.head(20)

combine.isnull().sum()

combine['BsmtFinSF2'].fillna(0, inplace = True)
combine['BsmtFinSF2'].isnull().any()

combine['BsmtFinSF1'].fillna(0, inplace = True)
combine['BsmtFinSF1'].isnull().any()

combine['BsmtFinType2'].fillna('None', inplace = True)
combine['BsmtFinType2'].isnull().any()

combine['BsmtFinType1'].fillna('None', inplace = True)
combine['BsmtFinType1'].isnull().any()

combine['BsmtFullBath'].fillna(0, inplace = True)
combine['BsmtFullBath'].isnull().any()

combine['BsmtHalfBath'].fillna(0, inplace = True)
combine['BsmtHalfBath'].isnull().any()

combine['BsmtQual'].fillna('None', inplace = True)
combine['BsmtQual'].isnull().any()

combine['BsmtUnfSF'].fillna(0, inplace = True)
combine['BsmtUnfSF'].isnull().any()

combine['Electrical'].fillna(combine['Electrical'].mode()[0], inplace = True)
combine['Electrical'].isnull().any()

combine['Exterior1st'].fillna(combine['Exterior1st'].mode()[0], inplace = True)
combine['Exterior1st'].isnull().any()

combine['Exterior2nd'].fillna(combine['Exterior2nd'].mode()[0], inplace = True)
combine['Exterior2nd'].isnull().any()

combine['Fence'].fillna('None', inplace = True)
combine['Fence'].isnull().any()

combine['FireplaceQu'].fillna('None', inplace = True)
combine['FireplaceQu'].isnull().any()

combine['MSZoning'].fillna('None', inplace = True)
combine['MSZoning'].isnull().any()

combine['MasVnrArea'].fillna(0, inplace = True)
combine['MasVnrArea'].isnull().any()

combine['MasVnrType'].fillna('None', inplace = True)
combine['MasVnrType'].isnull().any()

combine['MiscFeature'].fillna('None', inplace = True)
combine['MiscFeature'].isnull().any()

combine['PoolQC'].fillna('None', inplace = True)
combine['PoolQC'].isnull().any()

combine['SaleType'].fillna(combine['SaleType'].mode()[0], inplace = True)
combine['SaleType'].isnull().any()

combine['TotalBsmtSF'].fillna(combine['TotalBsmtSF'].mean(), inplace = True)
combine['TotalBsmtSF'].isnull().any()

combine['Utilities'].value_counts()

combine.drop(['Utilities'], axis = 1, inplace = True)
combine.shape

combine["LotFrontage"] = combine.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))
combine['LotFrontage'].isnull().any()

combine['Alley'].fillna('None', inplace = True)
combine['Alley'].isnull().any()

combine['BsmtCond'].fillna('None', inplace = True)
combine['BsmtCond'].isnull().any()

combine['BsmtExposure'].replace(('No'), ('None'), inplace = True)
combine['BsmtExposure'].fillna('None', inplace = True)
combine['BsmtExposure'].isnull().any()

combine['KitchenQual'].value_counts(dropna = False)

combine['KitchenQual'].fillna(combine['KitchenQual'].mode()[0], inplace = True)
combine['KitchenQual'].isnull().any()

combine['GarageYrBlt'].fillna('None', inplace = True)
combine['GarageYrBlt'].isnull().any()

combine['GarageType'].fillna('None', inplace = True)
combine['GarageType'].isnull().any()

combine['GarageQual'].fillna('None', inplace = True)
combine['GarageQual'].isnull().any()

combine['GarageFinish'].fillna('None', inplace = True)
combine['GarageFinish'].isnull().any()

combine['GarageCond'].fillna('None', inplace = True)
combine['GarageCond'].isnull().any()

combine['GarageCars'].fillna(0, inplace = True)
combine['GarageCars'].isnull().any()

combine['GarageArea'].fillna(0, inplace = True)
combine['GarageArea'].isnull().any()

combine['Functional'].fillna(combine['Functional'].mode()[0], inplace = True)
combine['Functional'].isnull().any()

combine.isnull().sum().sum()

combine['MSSubClass'] = combine['MSSubClass'].apply(str)
combine['OverallCond'] = combine['OverallCond'].astype(str)
combine['YrSold'] = combine['YrSold'].astype(str)
combine['MoSold'] = combine['MoSold'].astype(str)

from sklearn.preprocessing import LabelEncoder
cols = ('FireplaceQu', 'BsmtQual', 'BsmtCond', 'GarageQual', 'GarageCond','ExterQual',
        'ExterCond','HeatingQC', 'PoolQC', 'KitchenQual', 'BsmtFinType1','BsmtFinType2', 
        'Functional', 'Fence', 'BsmtExposure', 'GarageFinish', 'LandSlope','LotShape', 
        'PavedDrive', 'Street', 'Alley', 'CentralAir', 'MSSubClass', 'OverallCond','YrSold', 'MoSold')
for c in cols:
    lb = LabelEncoder() 
    lb.fit(list(combine[c].values)) 
    combine[c] = lb.transform(list(combine[c].values))
print('Shape all_data: {}'.format(combine.shape))

combine['total_area'] = combine['1stFlrSF'] + combine['2ndFlrSF'] + combine['TotalBsmtSF']
combine.shape

from scipy.stats import skew
numerical_feats = combine.dtypes[combine.dtypes != 'object'].index
skewed_feats = combine[numerical_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending = False)
skewness = pd.DataFrame({'skew':skewed_feats})
skewness.head(10)

skewness = skewness[abs(skewness > 0.8)]
print("There are {} skewed numerical features to box cox transform".format(skewness.shape[0]))
from scipy.special import boxcox1p
skewed_features = skewness.index
lam = 0.15
for feat in skewed_features:
    combine[feat] += 1
    combine[feat] = boxcox1p(combine[feat], lam)
combine[skewed_features] = np.log1p(combine[skewed_features])

combine = pd.get_dummies(combine)
combine.head()

x_train = combine.iloc[:ntrain]
x_test = combine.iloc[ntrain:]
print("Shape of train :", x_train.shape)
print("Shape of test :", x_test.shape)

n_folds = 5
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
def rmsle_cv(model):
    kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(x_train.values)
    rmse= np.sqrt(-cross_val_score(model, x_train.values, y_train, scoring="neg_mean_squared_error", cv = kf))
    return(rmse)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import Lasso
lasso = make_pipeline(RobustScaler(), Lasso(alpha = 0.0005, random_state = 3))
lasso.fit(x_train, y_train)

score = rmsle_cv(lasso)
print("\nLasso score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

from sklearn.linear_model import ElasticNet
ENet = make_pipeline(RobustScaler(), ElasticNet(alpha=0.0005, l1_ratio=.9, random_state=3))
score = rmsle_cv(ENet)
print("ElasticNet score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))
ENet.fit(x_train, y_train)

from sklearn.ensemble import GradientBoostingRegressor
GBoost = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,max_depth=4,
                                   max_features='sqrt',min_samples_leaf=15, min_samples_split=10,
                                   loss='huber', random_state =5)
score = rmsle_cv(GBoost)
print("ElasticNet score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

GBoost.fit(x_train, y_train)
predictions = GBoost.predict(x_test)

import lightgbm as lgb
model_lgb = lgb.LGBMRegressor(objective='regression',num_leaves=5,learning_rate=0.05,
                              n_estimators=720,max_bin = 55, bagging_fraction = 0.8,
                              bagging_freq = 5, feature_fraction = 0.2319,feature_fraction_seed=9, 
                              bagging_seed=9,min_data_in_leaf =6, min_sum_hessian_in_leaf = 11)
model_lgb.fit(x_train, y_train)

predictions = model_lgb.fit(x_train, y_train)

from sklearn.kernel_ridge import KernelRidge
KRR = KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5)
score = rmsle_cv(KRR)
print("Kernel Ridge score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

from sklearn.base import BaseEstimator
from sklearn.base import RegressorMixin
from sklearn.base import TransformerMixin
from sklearn.base import clone
class AveragingModels(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, models):
        self.models = models
    def fit(self, X, y):
        self.models_ = [clone(x) for x in self.models]
        for model in self.models_:
            model.fit(X, y)
        return self
    def predict(self, X):
        predictions = np.column_stack([model.predict(X) for model in self.models_])
        return np.mean(predictions, axis=1)

averaged_models = AveragingModels(models = (ENet, GBoost, KRR, lasso))
score = rmsle_cv(averaged_models)
print(" Averaged base models score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

class StackingAveragedModels(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, base_models, meta_model, n_folds=5):
        self.base_models = base_models
        self.meta_model = meta_model
        self.n_folds = n_folds
    def fit(self, X, y):
        self.base_models_ = [list() for x in self.base_models]
        self.meta_model_ = clone(self.meta_model)
        kfold = KFold(n_splits=self.n_folds, shuffle=True, random_state=156)
        out_of_fold_predictions = np.zeros((X.shape[0], len(self.base_models)))
        for i, model in enumerate(self.base_models):
            for train_index, holdout_index in kfold.split(X, y):
                instance = clone(model)
                self.base_models_[i].append(instance)
                instance.fit(X[train_index], y[train_index])
                y_pred = instance.predict(X[holdout_index])
                out_of_fold_predictions[holdout_index, i] = y_pred
        self.meta_model_.fit(out_of_fold_predictions, y)
        return self
    def predict(self, X):
        meta_features = np.column_stack([
            np.column_stack([model.predict(X) for model in base_models]).mean(axis=1)
            for base_models in self.base_models_ ])
        return self.meta_model_.predict(meta_features)

stacked_averaged_models = StackingAveragedModels(base_models = (ENet, GBoost, KRR),meta_model = lasso)
score = rmsle_cv(stacked_averaged_models)
print("Stacking Averaged models score: {:.4f} ({:.4f})".format(score.mean(), score.std()))

def rmsle(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

stacked_averaged_models.fit(x_train.values, y_train)
stacked_train_pred = stacked_averaged_models.predict(x_train.values)
stacked_pred = np.expm1(stacked_averaged_models.predict(x_test.values))
print(rmsle(y_train, stacked_train_pred))

import xgboost as xgb
model_xgb = xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468,learning_rate=0.05,
                             max_depth=3,min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,subsample=0.5213, 
                             silent=1,random_state =7, nthread = -1)
score = rmsle_cv(model_xgb)
print("Xgboost score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

model_xgb.fit(x_train, y_train)
xgb_train_pred = model_xgb.predict(x_train)
xgb_pred = np.expm1(model_xgb.predict(x_test))
print(rmsle(y_train, xgb_train_pred))

model_lgb.fit(x_train, y_train)
lgb_train_pred = model_lgb.predict(x_train)
lgb_pred = np.expm1(model_lgb.predict(x_test.values))
print(rmsle(y_train, lgb_train_pred))

print('RMSLE score on train data:')
print(rmsle(y_train,stacked_train_pred*0.70 +
               xgb_train_pred*0.15 + lgb_train_pred*0.15 ))

predictions = stacked_pred*0.70 + xgb_pred*0.15 + lgb_pred*0.15

submission = pd.DataFrame({'Id': test_ID,'SalePrice': predictions})
submission.head()

filename = 'submission.csv'
submission.to_csv(filename, index=False)
print('Saved file: ' + filename)
