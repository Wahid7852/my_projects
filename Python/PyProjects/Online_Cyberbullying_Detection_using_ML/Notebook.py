import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from nltk.stem.porter import PorterStemmer
import nltk
import re, string
from nltk.corpus import stopwords

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report
from sklearn import metrics



# Load Data
url = 'https://drive.google.com/uc?export=download&id=12fBlhsa5GIdtme1jT3KlPPIgIdjzqhv1'
df = pd.read_json(url, lines=True, orient='columns')

# Convert labels to binary
df['annotation'] = df['annotation'].apply(lambda x: 1 if x['label'][0] == '1' else 0)

# Preprocessing
tfIdfVectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True, stop_words='english')
tfIdf = tfIdfVectorizer.fit_transform(df['content'])

X = tfIdf.toarray()
y = df['annotation'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define batch size for oversampling
batch_size = 1000

# Create RandomOverSampler instance
from imblearn.over_sampling import RandomOverSampler
oversample = RandomOverSampler(sampling_strategy='not majority')

# Oversample in batches
X_over_batches, y_over_batches = [], []
for i in range(0, len(X_train), batch_size):
    X_batch, y_batch = oversample.fit_resample(X_train[i:i+batch_size], y_train[i:i+batch_size])
    X_over_batches.append(X_batch)
    y_over_batches.append(y_batch)

X_over = np.vstack(X_over_batches)
y_over = np.concatenate(y_over_batches)

def getStatsFromModel(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    
    print(f"Results for {model_name}:")
    
    # Classification Report
    classification_rep = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(classification_rep)
    
    # Confusion Matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(conf_matrix)
    
    # Calculate and display precision-recall curve
    precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(X_test)[:, 1])
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
    
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'Precision-Recall Curve for {model_name}')
    plt.show()

# Gaussian Naive Bayes
gnb = GaussianNB()
gnbmodel = gnb.fit(X_over, y_over)
getStatsFromModel(gnbmodel, X_test, y_test, "Gaussian Naive Bayes")

# Logistic Regression
lgr = LogisticRegression()
lgr.fit(X_over, y_over)
getStatsFromModel(lgr, X_test, y_test, "Logistic Regression")

# Decision Tree Classifier
dtc = DecisionTreeClassifier()
dtc.fit(X_over, y_over)
getStatsFromModel(dtc, X_test, y_test, "Decision Tree Classifier")

# AdaBoost Classifier
abc = AdaBoostClassifier() 
abc.fit(X_over, y_over)
getStatsFromModel(abc, X_test, y_test, "AdaBoost Classifier")

# Random Forest Classifier
rfc = RandomForestClassifier(verbose=True)
rfcmodel = rfc.fit(X_over, y_over)
getStatsFromModel(rfcmodel, X_test, y_test, "Random Forest Classifier")
