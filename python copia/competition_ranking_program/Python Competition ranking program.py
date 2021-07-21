
File = input("What is the file location")

def read_text():
    file_read = open(File)
    contents_of_file = file_read.read()
    print(file_read)
    quotes.close()

read_text()

