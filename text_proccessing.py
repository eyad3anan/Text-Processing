import nltk # importing the library nltk which stands for (natural Language toolkit)
from nltk.corpus import stopwords # importing the dataset stopwords from the module corpus
# stopwords ==> is a dataset containing a collection of stop words
import pandas as pd # Importing the python library
nltk.download("stopwords") # to download the stopwords dataset which contains a collection of stoping words
nltk.download("punkt")
data_frame = pd.read_csv("random_paragraphs.txt" , sep = "\t" , header = None) # Reading the txt file 
text_column = data_frame.iloc[:, 0] # Taking all the data in the first row
raw_text = ' '.join(text_column) # Convert the text data to a single string
# print(raw_text) # printing the raw text
separated_words = nltk.word_tokenize(raw_text) # word_tokenize(): This is the most common type of tokenization, where text is divided into words based on whitespace or punctuation

english_stop_words = set(stopwords.words('english')) # getting the stop words in the english

# Removing stopping words from the text
filtered_words = [word for word in separated_words if word.lower() not in english_stop_words]

from collections import Counter # Importing the Counter class to count the occurence of each word
words_count = Counter(filtered_words) # it will counts the occurence of each word and put the answer in dictionary
for word , count in words_count.items():
    print(f"{word}:{count}")
