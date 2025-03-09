def search(text,word):
    text=input("Please enter your text!")
    word=input("Please enter your word!")
    
    if word in text:
        return "You have your word in text above!"
    else:
        return "You can try another set of texts and words"
#You're working on a search engine. Watch your back google.
#The given code takes a text and a word as input and passes them to a function called search()
#The search() function should return "word found" if the word is present  in the text ,or "word not found",if it's not
text=input()
word=input()
search(text,word)