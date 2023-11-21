from nltk import sent_tokenize ,word_tokenize
import nltk
# nltk.download('punkt')

text_sample = 'The Matrix is everywhere its all around us, here even in this room. \
               You can see it out your window or on your television. \
               You feel it when you go to work, or go to church or pay your taxes.'

sentences = sent_tokenize(text=text_sample)
print(type(sentences),len(sentences))
print(sentences)

sentence = "The Matrix is everywhere its all around us, here even in this room."
words = word_tokenize(sentence)
print(type(words), len(words))
print(words)

from nltk import word_tokenize, sent_tokenize


# 여러개의 문장으로 된 입력 데이터를 문장별로 단어 토큰화 만드는 함수 생성
def tokenize_text(text):
    # 문장별로 분리 토큰
    sentences = sent_tokenize(text)
    # 분리된 문장별 단어 토큰화
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    return word_tokens


# 여러 문장들에 대해 문장별 단어 토큰화 수행.
word_tokens = tokenize_text(text_sample)
print(type(word_tokens), len(word_tokens))
print(word_tokens)


text_sample = 'Hello! I am not sure which specific sentence you would like me to translate.\
                Could you please provide the sentence or text that you would like me to translate into English?'

text_sample = '''
                Hello! I am not sure which specific sentence you would like me to translate.
                Could you please provide the sentence or text that you would like me to translate into English?
            '''
word_tokens = tokenize_text(text_sample)
print(word_tokens)

'''
    생성ai -> gan
    인물, 음악 생성..
    명회-> 이정재
    
    fit predict
    
    회귀 분류...
    ax + b = y
    10 -> 30
    20 -> 40
    30 -> 50
    
    분류
    10,20 -> a
    20,30 -> b
    11,21 -> a
'''