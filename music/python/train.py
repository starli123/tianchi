#!/usr/bin/python
import numpy as np
import os
import csv
import datetime
import os.path
from sklearn import svm
from sklearn import gaussian_process
from sklearn.tree import DecisionTreeRegressor
root_dir="/home/star/project/music/data/everyData/"
test_dir="/home/star/project/music/data/data/"
testxd="/home/star/project/music/data/"
filelist=[]
def f(x):
        return x*np.sin(x)
def loading_data():
	for par,dirname,filenames in os.walk(root_dir):
		for filename in filenames:
			filelist.append(filename)

def gaussian_train():
        csvfile=file('oksian_traincsv','wb')
        fi=open('gaussian.txt','a')
        writer=csv.writer(csvfile)
        for f in filelist:
                print f
                dataset=np.loadtxt(root_dir+f,delimiter=",")
                #testxx=np.loadtxt(testxd+"testx.txt",delimiter="\t")
                #testx=testxx.astype(int)
                testx=file(testxd+"textx.txt")
                x=dataset[2:181,0]
		y=dataset[2:181,1]
		#v=np.var(x)
		#print x
		#print y
		#xu=np.unique(x)
                #idx = [np.where(x==x1)[0][0] for x1 in xu]
		#gp = gaussian_process.GaussianProcess(corr='squared_exponential', theta0=1e-1,thetaL=1e-3, thetaU=1,random_start=100)
		#gp.fit(xu[:,np.newaxis], y[idx])
		xx=[]
                xx1=[]
                for m in x:
                        xx1.append(m)
                        xx.append(xx1)
                        xx1=[]
                #clf=svm.SVR(kernel='rbf')
		#gp = gaussian_process.GaussianProcess(regr='quadratic',corr='squared_exponential', theta0=1e-1,thetaL=1e-1,nugget=v, thetaU=1, optimizer='fmin_cobyla', random_start=10)
                #gp = gaussian_process.GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1)
                #xx=np.nan_to_num(xx)
		#y=np.nan_to_num(y)
		#x=np.atleast_2d(x).T
		#y=np.atleast_2d(y).T
		#gp.fit(x,y)
                #clf.fit(xx,y)
		dtr2 = DecisionTreeRegressor(max_depth=5)
		dtr2.fit(xx,y)
                print "starting test"
                for a in testx:
                        b=dtr2.predict(int(a.split(',')[1]))
                        #c=b.astype(int)
                        d=int(b[0])
                        da=f.split(".")[0]+","+str(d)+","+str(a.split(',')[0])
                        fi.write(da+"\n")
                        #writer.writerow(da)
        fi.close()

def train_play():
	csvfile=file('ok.csv','wb')
	fi=open('ok.txt','a')
	writer=csv.writer(csvfile)
	for f in filelist:
		print f
		dataset=np.loadtxt(root_dir+f,delimiter=",")
		#testxx=np.loadtxt(testxd+"testx.txt",delimiter="\t")
		#testx=testxx.astype(int)
		testx=file(testxd+"textx.txt")
		x=dataset[:,0]
		y=dataset[:,1]
		xx=[]
		xx1=[]
		for m in x:
			xx1.append(m)
			xx.append(xx1)
			xx1=[]
		clf=svm.SVR(kernel='rbf')
		clf.fit(xx,y)
		print "starting test"
		for a in testx:
			b=clf.predict(a.split(',')[1])
			c=b.astype(int)
			d=int(c[0])
			da=f.split(".")[0]+","+str(d)+","+str(a.split(',')[0])
			fi.write(da+"\n")
			#writer.writerow(da)
	fi.close()
		
if __name__=="__main__":
	loading_data()
	gaussian_train()
