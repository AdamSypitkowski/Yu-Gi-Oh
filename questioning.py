#build_wordlist() function goes here
def build_wordlist(infile):
  word_list = []
  for line in infile:
    word = line.strip()
    for i in range(len(word)):
      word_list.append(word[i])

#find_unique() function goes here
def find_unique(word_list):
  new_wordlist = [word_list[0]]
  for i in range(len(word_list)):
    counter = 0
    for j in range(len(new_wordlist)):
      if wordlist[i] == new_wordlist[j]:
        counter = 1
        break
    if counter == 0:
      new_wordlist.append(wordlist[i])

def main():
    #DO NOT CHANGE THIS FUNCTION
    #filename = input("Enter a file name:")
    #infile = open(filename, 'r')
    infile = '''here is a line in the test file
this is another line
one more line
that was the line
guess it was not
stopping now'''
    word_list = build_wordlist(infile)
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print()
    print(new_wordlist)

if __name__ == "__main__":
    main()