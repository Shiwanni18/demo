import nltk
nltk.download('punkt')

# Sample Text
text = "Natural Language Processing is a field of artificial intelligence."
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# Chunk Grammar
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
chunked_output = chunk_parser.parse(tags)

print("Chunked Output:")
chunked_output.draw()
