
import nltk
nltk.download("stopwords") #uncomment to download for first time
nltk.download('punkt_tab') 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string


# DOCUMENT ="""Theodore Finch and Violet Markey are two teenagers who live unhappily in a small Indiana town. Violet is quietly dealing with survivor guilt after the death of her sister and Finch is a loner, called a freak by other students. They meet on the bridge where Violet's sister died in a car crash nine months earlier. Violet survived the crash, and has not been in a car since. She finds herself standing on the ledge of the bridge on what would have been her sister's nineteenth birthday. Finch, out for a run, sees Violet on the ledge and climbs up next to her, talking her down from a possible suicide.
#     Finch begins a partnership with Violet for a school project that requires the students to explore Indiana together. Later, at home, Finch looks up Violet on Facebook, researching her sister's car accident, reading through Violet's old writing, and chatting with her online. Finch and Violet travel around Indiana to see sites chosen by him for the project. Violet refuses to travel by car, so they bike to the highest point in Indiana. However, to visit a miniature roller coaster too far away to bike to, Violet agrees to get in his car. She returns to writing, for the first time since her sister's death. He helps her talk about her sister, which no one else had managed to do. Violet slowly begins to heal. They fall in love.
#     However, Finch's behavior becomes more erratic. He sometimes disappears for days at a time without contacting anyone. One day, while he and Violet are swimming at the Blue Hole, he disappears under the water. By the time he resurfaces, Violet is distraught and pushes him to tell her more about himself, threatening to leave if he doesn't comply. He reveals that he had been physically abused by his father as a child, and that his mother is absent in his life.
#     On one occasion, Finch and Violet stay out all night by accident, upsetting Violet's parents. At school that day, Finch loses his temper on Violet's ex-boyfriend, Roamer, after Roamer calls him a freak. The two boys fight in the hall, and Finch takes off in his car. Violet, who broke up the fight, ends up in the principal's office with Finch's friend, Charlie. While they talk, Finch attends a support group session in a nearby town, recommended to him by Mr. Embry, the school guidance counselor. There, he runs into Amanda, Violet’s friend, who opens up to the group about her bulimia and two suicide attempts. Once Violet leaves the school, she heads to Finch's house. Since he is still at the meeting, she talks with Finch's sister, Kate, who then leaves for work. While she is working, at a bar, Finch enters and prompts her to talk about their father. This causes her to worry about him, though he reassures her. He leaves for their house, where Violet is waiting. In his room, she begs him to open up to her. He shouts at her to leave.
#     Finch disappears again. Violet tells her father how she and Finch met, and expresses her concern over his latest disappearance. He suggests she check in places they had visited together. She drives to the Blue Hole, where she finds Finch's clothes and phone abandoned, and correctly infers that he has drowned. Some time later, she attends his funeral.
#     While healing from Finch's suicide, Violet finds the map they used for travel around Indiana, and notices the last location they were supposed to visit together marked in red. It's the Travelers' Prayers Chapel, a resting place for travelers and a place of healing for mourners. She finds his signature in the guest book.
#     With Finch gone, Violet must present their school project alone. She reads aloud her writing on the lessons Finch taught her. In the last scene, Violet swims by herself in the Blue Hole."""

def extractive_sum(text, summary_percentage=20):    
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
    except:
        pass
    
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