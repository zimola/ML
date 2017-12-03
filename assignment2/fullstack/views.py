from django.shortcuts import render
from .forms import SplitForm, PreprocessingForm, MachineLearningForm
import os
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from django.conf import settings

##Global Variables 
#dataSetPath = "/classification"
#dirFileList = os.listdir(os.path.dirname(dataSetPath))
#path = os.path.join(settings.STATIC, dataSetPath)


#dataSetPath = '/Users/m/desktop/python/nov24/classification/'
#dirFileList = os.listdir(dataSetPath)

dataSetPath = "/Users/m/desktop/python/nov24/assignment2/fullstack/classification"
dirFileList = os.walk(dataSetPath)
myDataset = []



# Create your views here.
def index(request):
	preprocessingForm = PreprocessingForm(request.POST or None)
	splitForm= SplitForm(request.POST or None) 
	machineLearningForm = MachineLearningForm(request.POST)
	context={'preprocessingForm': preprocessingForm, 'splitForm': splitForm, 'machineLearningForm': machineLearningForm}

	if request.method =="POST":
		if splitForm.is_valid() and machineLearningForm.is_valid() and preprocessingForm.is_valid():
			#print(request.POST)
			readFile(dataSetPath)



			percent  = splitForm.cleaned_data['splitPercent']
			lowerCase = preprocessingForm.cleaned_data['preprocessingVariables']
			algorithm = machineLearningForm.cleaned_data['machineLearningVariable'] #tfidf or freq
			print(algorithm)
			
			lower = False
			punct = False
			numb = False
			if 'lower' in lowerCase:
				lower = True
			if 'punctuation' in lowerCase:
				punct = True
			if 'numbers' in lowerCase:
				numb = True

			print(percent, lower, punct, numb)
		context = {'splitPercent':percent, 'algorithm':algorithm, 'lower':lower, 'punct': punct, 'numbers':numb }
		print(context)
		return render(request, 'fullstack/success.html',context)
	return render(request, 'fullstack/index.html', context)



def readFile(filePath):
    dataFile = open(filePath)
    return dataFile.read()
'''
myDataset=[]
for file in dirFileList:
    if file.endswith('.txt'):
        myDataset.append(readFile(dataSetPath + file))
'''
def cleanData(dataset): #returns the dataset witout punctuation
    for index, text in enumerate(myDataset):
        text = re.sub('[!@#$%^\.=&\*()_\+]', ' ', text) # Remove Punctuations, Solution 1
        text = re.sub(r'[0-9]', '', text)
        text = re.sub(r'[-,"|><]', '', text)# remove numbers
        text = re.sub('\s+', ' ', text).strip()
        text = text.lower()
        myDataset[index] = text
    return myDataset

