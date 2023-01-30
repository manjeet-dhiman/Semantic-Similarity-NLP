import spacy

# load medium language model in english
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# when comparing cat and monkey it shows the highest similarity 0.59 as they are animals
print(word1.similarity(word2))
# monkey and banana is high 0.40, the similarity is that monkeys eat bananas
print(word3.similarity(word2))
# banana and cat show a low similarity at 0.22. there's little connection between the words
print(word3.similarity(word1))

#  working with vectors allows us to compare each word with each other
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
Animals (cat & monkey) and fruits (apple & banana) show high similarity (>0.58) with each other.
Monkey and banana show a high similarity (0.4) as monkeys eat bananas.
However monkeys show low similarity to apple (0.23) as they do not eat them normally.
Cats show a low similarity to both fruits as they are not normally associated with eating them.
'''

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''
Highest similarity is with "Hello, there is my car" at 0.80 as they both mention a car
and also it might seem to answer the question.

Least similarity is "I\'d like my boat back"  at 0.56 as the sentence doesn't
mention a cat or a car, it brings up a boat which is a vehicle (same entity as a car).

The other sentences are in between (0.6-0.7) as they mention a car 
or a dog (animal entity which both dog and cat belong to).
'''

'''
Example of your own.
'''
word1 = nlp("cow")
word2 = nlp("milk")
word3 = nlp("juice")

# cow and barn, 0.54 is higher similarity as a cow produces milk.
print(word1.similarity(word2))
# milk and juice, 0.61, high similarity as they are both a drinkable liquid.
print(word3.similarity(word2))
# juice and cow, 0.19 shows low similarity as they have little connection in the real world.
print(word3.similarity(word1))

'''
Run the example file with the simpler language model 'en_core_web_sm' 
and write a note on what you notice is different from the model
'en_core_web_md'.

When running simpler language model (en_core_web_sm) I found that the numbers are far lower, 
it's finding a lower similarity between words than running en_core_web_md language model.

The definitions of the end:
md - medium model
sm - simple model
In general, we expect larger models to be "better" and more accurate overall
as it is modelled off a larger data set.
'''
