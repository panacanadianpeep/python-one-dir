import urllib

def get_file():
    quotes = open("/Users/administrator/Dropbox/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

read_text()