# write a python program to print the contents of a directory using the os module.
import os

def print_directory_contents(directory_path):
  """Prints the contents of a specified directory.

  Args:
    directory_path: The path to the directory to list.
  """

  try:
    contents = os.listdir(directory_path)
    for item in contents:
      print(item)
  except FileNotFoundError:
    print(f"Directory '{directory_path}' not found.")
  except OSError as e:
    print(f"Error accessing directory: {e}")

if __name__ == "__main__":
  directory_path = input("Enter the directory path: ")
  print_directory_contents(directory_path)
