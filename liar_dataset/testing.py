import sys

sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
sys.path.append("C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/easyocr")
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')

import easyocr

img = sys.argv[1]


reader = easyocr.Reader(['en'], gpu=False, model_storage_directory='C:/Users/Kyle/.EasyOCR/model', user_network_directory='C:/Users/Kyle/.EasyOCR/user_network')
result = reader.readtext(img, detail = 0) #reading the image 

result_list = []

#appending extracted words into a list 
for word in result:
    result_list.append(word)

#Concatenation of list
sentences = " ".join(result_list)

#Test Results

import pandas as pd
import re
import numpy as np
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.metrics import accuracy_score


def read_dataframe(csv_file) -> pd.DataFrame:
   
    df = pd.read_csv("test.csv")
    
    # replaces all "null" or "NaN" values with an empty string
    df.fillna("", inplace=True)
    
    # labels the columns in the dataset using the data dictionary described in the README
    df.columns = [
        'statement',     # Column 1: Statement.
        'label',         # Column 1: Label.

    ]
    
    return df

#create a dataframe from the training data
data = read_dataframe('train.csv')

stemmer = SnowballStemmer('english')
words = stopwords.words("english")

data['preprocessed'] = data['statement'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]"," ",x).split() if i not in words]).lower())

X_train, X_test,y_train,y_test = train_test_split(data['preprocessed'],data.label, test_size=.3)

pipeline = Pipeline([('vect',TfidfVectorizer(ngram_range=(1,1),stop_words = "english",sublinear_tf=True)),
                    ('chi',SelectKBest(chi2, k=1000)),
                    ('clf',LinearSVC(C=1.0, penalty='l1', max_iter=3000, dual = False))])

model = pipeline.fit(X_train,y_train)

vectorizer = model.named_steps['vect']
chi = model.named_steps['chi']
clf = model.named_steps['clf']

feature_names = vectorizer.get_feature_names()
feature_names = [feature_names[i] for i in chi.get_support(indices = True)]
feature_names = np.asarray(feature_names)


# Model prediction
prediction = model.predict([sentences])

print(sentences)

print(str(model.score(X_test,y_test)) + "\n")

print(prediction)