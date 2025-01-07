# Check if the text appears in a file name


filename =  input("File Name :")

text = input("Text :")

with open(filename) as f :
    contents = f.read()
    text_count = contents.count(text)
    print(text_count)

    
