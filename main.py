def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    
    def char_counter():
      char_appearances = {}
      for char in file_contents.lower():
        if char in char_appearances:
          char_appearances[char] +=1
        elif char != " " and char != "\n":
          char_appearances[char] = 1
      return char_appearances
    
    def report():
      char_dictionnary = char_counter()
      words_count = len(words)
      print("--- Begin report of books/frankenstein.txt ---")
      print(f"{words_count} words found in the document")
      for k in char_dictionnary:
        print(f"The {k} character was found {char_dictionnary[k]} times")
      print("---End report ---")

    report()
main()