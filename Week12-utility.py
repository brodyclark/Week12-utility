# METHOD USED
# Brody Clark
# CSCI102 - Section C
# Week 12 - Part A

def PrintOutput(string):
     print('OUTPUT', string)

def LoadFile(file_name):
    with open(file_name, 'r') as read_file:
        lines = read_file.readlines()
    print(lines)

def UpdateString(string_one, string_two, integer):
     list_one = list(string_one)
     
     for index in range(len(list_one)):
          
          if index == integer:
               list_one[index] = string_two
     
     print(''.join(list_one))


     
               
