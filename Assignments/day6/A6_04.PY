# A6_04. Write a program to input player's name (string) and runs (integer) scored
#  for n number of players where n should be input from the keyboard.
#  Store the player’s details
#  in a dictionary called 'cricket'. After preparing the dictionary,
#  input the player's name and print the runs scored by the player 
# otherwise return '-1' if the player's name is not found.


n = int(input("Enter the number of players: "))

cricket = {}

for _ in range(n):
  
    name = input("Enter the player's name: ").strip()
    runs = int(input("Enter the runs scored: ").strip())
    cricket[name] = runs


search_name = input("Enter the name of the player to search: ").strip()

if search_name in cricket:
    print(f"Runs scored by {search_name}: {cricket[search_name]}")
else:
    print("-1")
