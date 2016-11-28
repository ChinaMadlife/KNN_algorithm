# -*- coding: utf-8 -*-

import sys  
import os 
import time
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator

# ����utf-8�������
# reload(sys)
# sys.setdefaultencoding('utf-8')
# 
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

# �н����Ҿ��빫ʽ
def cosdist(vector1,vector2):
	Lv1 = sqrt(vector1*vector1.T)
	Lv2 = sqrt(vector2*vector2.T)
	return vector1*vector2.T/(Lv1*Lv2)
    

# kNN������
# ���Լ���inX
# ѵ������dataSet
# ����ǩ��labels
# k:k���ھ���
def classify(testdata, dataSet, labels, k):
	  # ����������������
    dataSetSize = dataSet.shape[0]    
    # ������Լ���ѵ����֮��ľ��룺��׼ŷ�Ͼ���
    # 1.�����������ѵ��������Ĳ�
    diffMat = tile(testdata, (dataSetSize,1)) - dataSet
    # 2.������ƽ����
    sqDiffMat = diffMat**2
    # 3.�������
    sqDistances = sqDiffMat.sum(axis=1)
    # 4.���ɱ�׼��ŷ�Ͼ���
    distances = sqDistances**0.5
    print distances
    # 5.�������ɵ�ŷ�Ͼ����С����,���Ϊ������
    sortedDistIndicies = distances.argsort()        
    classCount={}     
    # ��ȡŷ�Ͼ����ǰ������Ϊ�ο���          
    for i in range(k):  # i = 0~(k-1)  	  
    	  # �����˳�򷵻���������Ӧ������ǩ
        voteIlabel = labels[sortedDistIndicies[i]]
        # Ϊ�ֵ�classCount��ֵ,��ͬkey����value��1
        # key:voteIlabel��value: ����voteIlabel��ǩ��ѵ������ 
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # �Է����ֵ�classCount��value��������
    # sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True) 
    # �þ��ǰ��ֵ�ֵ����Ĺ̶��÷�
    # classCount.iteritems()���ֵ����������
    # key�����������operator.itemgetter(1)���༶����
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # ��������ߵ�һ��
    return sortedClassCount[0][0]

k=3
testdata=[0.2,0.2]
dataSet,labels = createDataSet()

# ��ͼ
fig = plt.figure()
ax = fig.add_subplot(111)
indx = 0 
for point in dataSet:
	if labels[indx] == 'A' :
		ax.scatter(point[0],point[1],c='blue',marker='o',linewidths=0, s=300)
		plt.annotate("("+str(point[0])+","+str(point[1])+")",xy = (point[0],point[1]))
	else:
		ax.scatter(point[0],point[1],c='red',marker='^',linewidths=0, s=300)
		plt.annotate("("+str(point[0])+", "+str(point[1])+")",xy = (point[0],point[1]))	
	indx += 1

ax.scatter(testdata[0],testdata[1],c='green',marker='s',linewidths=0, s=300)
plt.annotate("("+str(testdata[0])+", "+str(testdata[1])+")",xy = (testdata[0],testdata[1]))		

plt.show()
print classify(testdata, dataSet, labels, k)