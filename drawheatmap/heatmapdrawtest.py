__author__ = 'jasonzhuo'
import heatmapdraw as heat
import numpy as np
confusematrix=[[0 for col in range(5)] for row in range(5)]
class_names=[i for i in range(1,5)]


#classify 0 as 0, 1 as 1 .... etc.
confusematrix[0][0]=3
confusematrix[1][1]=1
confusematrix[2][2]=7
confusematrix[3][3]=1
confusematrix[4][4]=1

heat.plotHeatmap("", "Class ID", "Predicted class ID", np.asarray(confusematrix).transpose())