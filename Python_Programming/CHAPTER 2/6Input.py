a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

print("Number a is : ", a)
print("Number b is : ", b)
print("sum is : ",a+b)
help(print)
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.

#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.
help(input)
# input(prompt='', /)
#     Read a string from standard input.  The trailing newline is stripped.

#     The prompt string, if given, is printed to standard output without a
#     trailing newline before reading input.

#     If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
#     On *nix systems, readline is used if available