import nltk

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The children are playing in the garden"

tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

print(pos_tags)
