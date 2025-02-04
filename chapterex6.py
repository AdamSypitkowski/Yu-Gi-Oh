#definition for music_func goes here
def music_func(music, group, singer) -> None:
  if music == None:
    music = "Classic Rock"
    group = "The Beatles"
    singer = "Freddie Mercury"

  print("The best kind of music is", music)
  print("The best music group is", group)
  print("The best lead vocalist is", singer)

def main():
    #DO NOT CHANGE THE MAIN FUNCTION
    music, group, singer = input().split(',')
    music_func(music, group, singer)
    print()
    music_func()

if __name__ == "__main__":
    main()
