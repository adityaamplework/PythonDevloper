
import re
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from goose3 import Goose
# g = Goose()
# url = 'https://en.wikipedia.org/wiki/Automatic_summarization'
# article = g.extract(url)

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back into a single string
    return ' '.join(tokens)





def summarize(text, number_of_sentences, percentage = 0):
  original_text = text
  formatted_text = preprocess_text(original_text)

  word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))
  highest_frequency = max(word_frequency.values())
  for word in word_frequency.keys():
    word_frequency[word] = (word_frequency[word] / highest_frequency)
  sentence_list = nltk.sent_tokenize(original_text)
  
  score_sentences = {}
  for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
      if word in word_frequency.keys():
        if sentence not in score_sentences.keys():
          score_sentences[sentence] = word_frequency[word]
        else:
          score_sentences[sentence] += word_frequency[word]

  import heapq
  if percentage > 0:
    best_sentences = heapq.nlargest(int(len(sentence_list) * percentage), score_sentences, key=score_sentences.get)
  else:
    best_sentences = heapq.nlargest(number_of_sentences, score_sentences, key=score_sentences.get)

  return sentence_list, best_sentences, word_frequency, score_sentences



def visualize(title, sentence_list, best_sentences):
    from IPython.core.display import HTML
    from IPython.display import display

    # Define custom CSS for mark tag
    custom_style = """
    <style>
        mark {
            background-color: lightblue; /* Change this to any color */
            color: black; /* Change text color if needed */
            padding: 2px;
            border-radius: 5px;
        }
    </style>
    """

    text = ''
    for sentence in sentence_list:
        if sentence in best_sentences:
            text += ' ' + f"<mark>{sentence}</mark>"  # Highlight best sentences
        else:
            text += ' ' + sentence
    
    # Display styled output
    display(HTML(custom_style + f'<h1>Summary - {title}</h1> {text}'))




