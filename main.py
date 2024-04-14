def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    
    def char_counter():
      char_appearances_dict = {}
      char_appearances_list = []
      for char in file_contents.lower():
        if char.isalpha():
          if char in char_appearances_dict:
            char_appearances_dict[char] +=1
          elif char != " " and char != "\n":
            char_appearances_dict[char] = 1

      for k in char_appearances_dict:
        single_dict = {"char_name" : k, "appearances" : char_appearances_dict[k] }
        char_appearances_list.append(single_dict)

      
      char_appearances_list.sort(reverse=True, key= sort_on_dict)

      return char_appearances_dict, char_appearances_list
    

    def sort_on_dict(dict):
      return dict["appearances"]
    

    def report():
      char_dictionnary, char_list = char_counter()
      words_count = len(words)
      print("--- Begin report of books/frankenstein.txt ---")
      print(f"{words_count} words found in the document")
      for char in char_list:
        print(f"The {char['char_name']} character was found {char['appearances']} times")
      print("---End report ---")

    report()
main()