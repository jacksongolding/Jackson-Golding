InfoDb = []
InfoDb.append({
  "Game": "Rainbow Six Siege",  
  "Publisher": "Ubisoft",  
  "ReleaseDate": "December 1st, 2015",  
  "FavoriteCharacters": ["Rook", "Jager", "Nokk", "Lion"]  
})

def print_data(n):
    print(InfoDb[n]["Game"]),
    print(InfoDb[n]["Publisher"],),
    print(InfoDb[n]["ReleaseDate"]),
    print("Favorite Characters: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["FavoriteCharacters"]))  # join allows printing a string list with separator
    print()
  # using comma puts space between values

def tester():
    print(" ")
    print("For loop")
    for_loop()
    print(" ")
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print(" ")
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
    print(" ")

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition