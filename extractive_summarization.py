
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
import string

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

def extractive_sum(text, summary_percentage=20):
    
    stop_words = set(stopwords.words("english"))
    punctuation_set = set(string.punctuation)
    
    words = word_tokenize(text.lower())
    
    freq_table = {}
    for word in words:
        if word in stop_words or word in punctuation_set:
            continue
        
        freq_table[word] = freq_table.get(word, 0) + 1
    
    sentences = sent_tokenize(text)
    
    sentence_values = {}
    for sentence in sentences:
        lower_sentence = sentence.lower()
        
        sentence_score = sum(
            freq_table.get(word, 0) 
            for word in word_tokenize(lower_sentence) 
            if word in freq_table
        )
        
        sentence_values[sentence] = sentence_score
    
    if sentence_values:
        sorted_sentences = sorted(
            sentence_values.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        target_length = len(text) * (summary_percentage / 100)
        
        summary_sentences = []
        current_length = 0
        
        for sentence, _ in sorted_sentences:
            if current_length < target_length:
                summary_sentences.append(sentence)
                current_length += len(sentence)
            else:
                break
        
        summary = ' '.join(summary_sentences)
        
        return summary
    
    return ""


