
#split(str,num)   here, num specifies number of splits and str specifies where split will occur
#splits str into list elements
s='python program'
print(s.split())#returns list of two items ['python', 'program']
s2='11 ,12 , 13'
# Splitting by a Specific Separator:
print(s2.split(',',2))
# Splitting by Whitespace:
print(s2.split(' ',2))
print(s.split('o',2))