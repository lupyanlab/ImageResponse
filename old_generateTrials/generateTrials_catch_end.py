#!/usr/bin/env python
import random
from itertools import permutations, combinations_with_replacement, combinations
import pandas as pd
import sys

images = pd.read_csv('filesdoc1.csv')
question_ids = images.Question_ID.unique()
ID = images.ID.unique()

def createCombos(stims):
    stimCombos=[]
    for i in range(1):
        stimCombos= stimCombos + list(combinations(stims, 2))

    stimCombos = stimCombos 
    return stimCombos

positions = ['left','right']
positionPermutations = list(permutations(positions, 2))
ratioDiffSame = 2
separator = ","


def circularList(lst):
	if not isinstance(lst,list):
		lst = range(lst)
	i = 0
	random.shuffle(lst)
	while True:
		yield lst[i]
		if (i+1) % len(lst) ==0:
			random.shuffle(lst)
		i = (i + 1)%len(lst)


						
def generateTrials(runTimeVars,runTimeVarsOrder):
	testFile = open('trials/'+runTimeVars['workerId']+ '_trials.csv','w')
	print runTimeVarsOrder
	header = separator.join(runTimeVarsOrder) + separator + separator.join(("Category", "Subcategory1","Subcategory2","firstStimPosition", "secondStimPosition","pic1","pic2"))
	print >>testFile, header
	trialList =[]
	positionList = circularList(positionPermutations)
	
	subcategory = images[['Image', 'subcategory']]

	images_list = []
	
	# If I put this part in the loop below it will select more than one exemplar within a subID e.g., owl. This keeps it constant so the same 'owl' is compared with each other subID member.
	catag1 = random.choice(ID)
	images_list.append(
		list(images.loc[
		(images.ID == (catag1)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C2 = [x for x in ID if x not in catag1]
	catag2 = random.choice(C2)
	images_list.append(
		list(images.loc[
			(images.ID == (catag2)) & (images.Question_ID == random.choice(question_ids)),
			'Image'])
		) #and so on... append all of them
	C3 = [x for x in C2 if x not in catag2]
	catag3 = random.choice(C3)
	images_list.append(
		list(images.loc[
		(images.ID == (catag3)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C4 = [x for x in C3 if x not in catag3]
	catag4 = random.choice(C4)
	images_list.append(
		list(images.loc[
		(images.ID == (catag4)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C5 = [x for x in C4 if x not in catag4]
	catag5 = random.choice(C5)
	images_list.append(
		list(images.loc[
		(images.ID == (catag5)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C6 = [x for x in C5 if x not in catag5]
	catag6 = random.choice(C6)
	images_list.append(
		list(images.loc[
		(images.ID == (catag6)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C7 = [x for x in C6 if x not in catag6]
	catag7 = random.choice(C7)
	images_list.append(
		list(images.loc[
		(images.ID == (catag7)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))
	C8 = [x for x in C7 if x not in catag7]
	catag8 = random.choice(C8)
	images_list.append(
		list(images.loc[
		(images.ID == (catag8)) & (images.Question_ID == random.choice(question_ids)),
		'Image']))

	stim_lists = map(createCombos, images_list)
	catch_lists = ['catch_a', 'catch_1', 'catch_b', 'catch_2', 'catch_c', 'catch_3']
	
	print (stim_lists)

	for curIter in range(1):
			for cur_stim_list in stim_lists:
				for curCombination in cur_stim_list:
				   curIsSimult=1
				   pic1 = curCombination[0]
				   pic2 = curCombination[1]
				   curPosition = positionList.next() 
				   subC1 = images.loc[images['Image'] == pic1, 'subcategory'].iloc[0]
				   subC2 = images.loc[images['Image'] == pic2, 'subcategory'].iloc[0]
				   (firstStimPosition, secondStimPosition) = (curPosition[0],curPosition[1])
				   maincata = images.loc[images['Image'] == pic1, 'category'].iloc[0]
				   trialList.append(separator.join((str(maincata), str(subC1), str(subC2), firstStimPosition,secondStimPosition,pic1,pic2)))

	trialList = trialList[:224]

	random.shuffle(trialList)
	
	for curIter in range(1):
			for cur_stim_list in catch_lists:
				for curCombination in cur_stim_list:
				   curIsSimult=1
				   pic1 = catch_lists[0]
				   pic2 = catch_lists[1]
				   pic3 = catch_lists[2]
				   pic4 = catch_lists[3]
				   pic5 = catch_lists[4]
				   pic6 = catch_lists[5]
				   curPosition = positionList.next() 
				   subC1 = 'plain'
				   subC2 = 'writing'
				   maincata = 'Catch'
				   trialList.append(separator.join((str(maincata), str(subC1), str(subC2), 'left', 'right', str(pic1),str(pic2))))
				   trialList.append(separator.join((str(maincata), str(subC1), str(subC2), 'left', 'right', str(pic3),str(pic4))))
				   trialList.append(separator.join((str(maincata), str(subC1), str(subC2), 'right', 'left', str(pic5),str(pic6))))
	
	trialList = trialList[:227]

	for curTrialList in trialList:
		trialData = separator.join([str(runTimeVars[curRuntimeVar]) for curRuntimeVar in runTimeVarsOrder])+separator+curTrialList
		print >>testFile, trialData
					
if __name__ == "__main__":
    trialList = generateTrials({'workerId':sys.argv[1]},['workerId'])
	
