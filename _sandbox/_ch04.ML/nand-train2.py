import pandas as pd
from sklearn import svm, metrics

#NAND

nand_input = [
	[0,0,1],
	[0,1,1],
	[1,0,1],
	[1,1,0]
]

# preprocessing

nand_df = pd.DataFrame(nand_input)
nand_data = nand_df.ix[:,0:1] # data
nand_label = nand_df.ix[:,2] #label

# learning and prediction

clf = svm.SVC()
clf.fit(nand_data,nand_label)
pre = clf.predict(nand_data)


# accuracy

ac_score = metrics.accuracy_score(nand_label,pre)
print("정답률 = ",ac_score)
