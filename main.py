def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    word_count = num_words(text)
    char_count = num_chars(text)
    clean_report = clean_count(char_count)

    print(f"--- Begin report of {book} ---")
    print(f"There are {word_count} words in the document")
    
    for item in clean_report:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['number']} times")

    print("--- End report ---")

def num_words(text):
    words = text.split()
    return len(words)

def book_text(book):
    with open(book) as f:
        return f.read()

def num_chars(text):
    lower_text = text.lower()
    char_count = {}
    for i in lower_text:
        if i in char_count:
            char_count[i] += 1
        else: 
            char_count[i] =1 
    return char_count

def sort_on(d):
    return d["number"]

def clean_count(char_count):
    clean_order = []
    for char in char_count:
        clean_order.append({"character": char, "number": char_count[char]})
    clean_order.sort(reverse=True, key=sort_on)
    return clean_order

main()