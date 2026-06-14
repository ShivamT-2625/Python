str1 ="This is a string"
str2="\nShivam The coding blaze"
print(str1 +str2)

# escape sequence character = \n , \t
name = "Shivam"
print(len(name))
print(name[0:])
name2 = name[:]
print(name[2])
print(name2)
# name[2]="T" throws error coz string doesnt support item assignment

print(name[-1:-2])

# function 
print(name.endswith("m"))
print(name.capitalize()) #creates new string instead
print(name.replace("a","j"))
# print(name.find(word))
print(name.count("m"))