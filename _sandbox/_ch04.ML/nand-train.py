from sklearn import svm

# NAND data

nand_data = [
    #P, Q, P NAND Q
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# divide data and label for learning

data = []
label = []
for row in nand_data:
	p = row[0]
	q = row[1]
	r = row[2]
	data.append([p,q])
	label.append(r)

# learning

clf = svm.SVC()
clf.fit(data,label)


# prediction

pre = clf.predict(data)
print(" 예측결과:",pre)

# display accuracy

ok, total = 0,0
for idx, answer in enumerate(label):
	p = pre[idx]
	if p == answer: ok +=1
	total +=1
print("정답률:",ok,"/",total,"=",ok/total)
