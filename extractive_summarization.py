
# import re
# import string
# from collections import Counter

# def clean_text(text):
#     """
#     Clean the input text by removing punctuation and converting to lowercase.
    
#     Args:
#         text (str): Input text to clean
    
#     Returns:
#         str: Cleaned text
#     """
#     # Remove punctuation
#     text = text.translate(str.maketrans('', '', string.punctuation))
    
#     # Convert to lowercase
#     text = text.lower()
    
#     return text

# def split_sentences(text):
#     """
#     Split text into sentences using regex.
    
#     Args:
#         text (str): Input text to split
    
#     Returns:
#         list: List of sentences
#     """
#     # Split on periods, exclamation points, and question marks
#     sentences = re.split(r'(?<=[.!?])\s+', text)
    
#     # Remove any empty sentences and strip whitespace
#     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
#     return sentences

# def calculate_word_frequencies(sentences):
#     """
#     Calculate word frequencies across all sentences.
    
#     Args:
#         sentences (list): List of sentences
    
#     Returns:
#         Counter: Word frequencies
#     """
#     # Combine all sentences
#     full_text = ' '.join(sentences)
    
#     # Clean the text
#     cleaned_text = clean_text(full_text)
    
#     # Split into words
#     words = cleaned_text.split()
    
#     # Remove common stop words
#     stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'])
#     words = [word for word in words if word not in stop_words]
    
#     # Calculate word frequencies
#     return Counter(words)

# def score_sentences(sentences, word_frequencies):
#     """
#     Score sentences based on word frequencies.
    
#     Args:
#         sentences (list): List of sentences
#         word_frequencies (Counter): Word frequencies
    
#     Returns:
#         dict: Sentence scores
#     """
#     sentence_scores = {}
    
#     for i, sentence in enumerate(sentences):
#         # Clean the sentence
#         cleaned_sentence = clean_text(sentence)
        
#         # Split into words
#         words = cleaned_sentence.split()
        
#         # Calculate score based on word frequencies
#         score = sum(word_frequencies[word] for word in words)
        
#         sentence_scores[i] = score
    
#     return sentence_scores

# def extractive_summarize(text, num_sentences=6):
#     """
#     Generate an extractive summary of the input text.
    
#     Args:
#         text (str): Input text to summarize
#         num_sentences (int, optional): Number of sentences in the summary. Defaults to 3.
    
#     Returns:
#         str: Extractive summary
#     """
#     # Split text into sentences
#     sentences = split_sentences(text)
    
#     # Ensure num_sentences doesn't exceed total sentences
#     num_sentences = min(num_sentences, len(sentences))
    
#     # Calculate word frequencies
#     word_frequencies = calculate_word_frequencies(sentences)
    
#     # Score sentences
#     sentence_scores = score_sentences(sentences, word_frequencies)
    
#     # Sort sentences by score in descending order
#     top_sentence_indices = sorted(
#         sentence_scores, 
#         key=sentence_scores.get, 
#         reverse=True
#     )[:num_sentences]
    
#     # Sort indices to maintain original text order
#     top_sentence_indices.sort()
    
#     # Construct summary
#     summary = ' '.join([sentences[i] for i in top_sentence_indices])
    
#     return summary

# # Example usage
# def main():
#     # Sample text for demonstration
#     sample_text = """
#     Technologies are becoming increasingly complicated and increasingly interconnected. Cars, airplanes, medical devices, financial transactions, and electricity systems all rely on more computer software than they ever have before, making them seem both harder to understand and, in some cases, harder to control. Government and corporate surveillance of individuals and information processing relies largely on digital technologies and artificial intelligence, and therefore involves less human-to-human contact than ever before and more opportunities for biases to be embedded and codified in our technological systems in ways we may not even be able to identify or recognize. Bioengineering advances are opening up new terrain for challenging philosophical, political, and economic questions regarding human-natural relations. Additionally, the management of these large and small devices and systems is increasingly done through the cloud, so that control over them is both very remote and removed from direct human or social control. The study of how to make technologies like artificial intelligence or the Internet of Things “explainable” has become its own area of research because it is so difficult to understand how they work or what is at fault when something goes wrong (Gunning and Aha 2019).

# This growing complexity makes it more difficult than ever—and more imperative than ever—for scholars to probe how technological advancements are altering life around the world in both positive and negative ways and what social, political, and legal tools are needed to help shape the development and design of technology in beneficial directions. This can seem like an impossible task in light of the rapid pace of technological change and the sense that its continued advancement is inevitable, but many countries around the world are only just beginning to take significant steps toward regulating computer technologies and are still in the process of radically rethinking the rules governing global data flows and exchange of technology across borders.

# These are exciting times not just for technological development but also for technology policy—our technologies may be more advanced and complicated than ever but so, too, are our understandings of how they can best be leveraged, protected, and even constrained. The structures of technological systems as determined largely by government and institutional policies and those structures have tremendous implications for social organization and agency, ranging from open source, open systems that are highly distributed and decentralized, to those that are tightly controlled and closed, structured according to stricter and more hierarchical models. And just as our understanding of the governance of technology is developing in new and interesting ways, so, too, is our understanding of the social, cultural, environmental, and political dimensions of emerging technologies. We are realizing both the challenges and the importance of mapping out the full range of ways that technology is changing our society, what we want those changes to look like, and what tools we have to try to influence and guide those shifts.
#     """
    
#     # Generate summary
#     summary = extractive_summarize(sample_text)
    
#     print("Original Text:")
#     print(len(sample_text))
#     print("\nSummary:")
#     print(summary)

# if __name__ == "__main__":
#     main()

