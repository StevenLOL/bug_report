
import numpy as np
import os
from sklearn.model_selection import KFold,train_test_split
from sklearn.svm import LinearSVR,SVR
from sklearn.linear_model import SGDRegressor,LinearRegression,HuberRegressor,RANSACRegressor,TheilSenRegressor,RandomizedLogisticRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import RobustScaler,MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor,BaggingRegressor,AdaBoostRegressor
from sklearn.neighbors import RadiusNeighborsRegressor,KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.decomposition import MiniBatchSparsePCA,PCA, TruncatedSVD,NMF

from sklearn.feature_selection import SelectPercentile,chi2,mutual_info_classif,f_classif,f_regression
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.preprocessing import StandardScaler
import cPickle as pickle


fiels_wordvectors=[

    ('loadFasttextWord2Vector','/paper_cache/CWE_P_300_SG.txt'),

]


def evalTrainData(trainDatax,trainV,random_state=2016,eid=''):
    fold=10

    scores=[]
    pccs=[]
    cvcount=0
    assert len(trainDatax)==len(trainV)
    import time
    for roundindex in range(0,3):    
        skf=KFold(fold,shuffle=True,random_state=random_state+roundindex)
        for trainIndex,evalIndex in skf.split(trainDatax):
            t1=time.time()
            cvTrainx,cvTrainy=trainDatax[trainIndex],trainV[trainIndex]
            cvEvalx,cvEvaly=trainDatax[evalIndex],trainV[evalIndex]

            scaler=StandardScaler()
            cvTrainy=scaler.fit_transform(cvTrainy.reshape(-1, 1)).ravel()     
            lsvr=getxlf(random_state=random_state)
            lsvr.fit(cvTrainx,cvTrainy)
            predict=lsvr.predict(cvEvalx)
            predict=scaler.inverse_transform(predict.reshape(-1,1)).ravel()
            score=mean_absolute_error(cvEvaly,predict)
            pcc=np.corrcoef(cvEvaly,predict)[0, 1]
            print (cvcount,'MAE',score,'PCC',pcc,time.time()-t1,time.asctime( time.localtime(time.time()) ) ,'Train sahpe:',cvTrainx.shape,'eval sahpe:', cvEvalx.shape)
            scores.append(score)
            pccs.append(pcc)
            cvcount+=1

    print ('###',eid,'MAE',np.mean(scores),'PCC',np.mean(pccs))


pca_n_components=100
def getxlf(random_state=2016):
    xlf1= Pipeline([
                          ('svd',PCA(n_components=pca_n_components)),
                          ('regressor',AdaBoostRegressor(random_state=random_state,

                           base_estimator=  MLPRegressor(random_state=random_state,early_stopping=True,max_iter=2000)
                                                         ,n_estimators=30,learning_rate=0.01)),
                          ])

    return xlf1


def processTraining(emid=0,targetfilename='./paper_cache/pv01.pickle'):
    fid=fiels_wordvectors[emid][1].split('/')[-1].split('.')[0]
    print (fid)
    tempfile='./paper_cache/'+fid+'.picke'

    if os.path.isfile(tempfile):
        print ('load from cache')
        ftrainx,ftrainv,testWordInChs,testids=pickle.load(open(tempfile,'rb'))
        evalTrainData(ftrainx,ftrainv,random_state=2016,eid=fid)


for eid in range(0,len(fiels_wordvectors)):
    processTraining(emid=eid)