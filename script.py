def print_phrase_words(phrase: str):
    for word in phrase.split():
        print(word)

def get_length_phrase(phrase: str):
    return len(phrase.split())
        
print_phrase_words("Today I'm very happy because I'm moving towards $2000 per month")

