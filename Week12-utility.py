# METHOD USED
# Brody Clark
# CSCI102 - Section C
# Week 12 - Part A

import sys

def PrintOutput(string):
     print('OUTPUT', string)

def LoadFile(file_name):
    with open(file_name, 'r') as read_file:
        lines = read_file.readlines()
    PrintOuput(lines)

def UpdateString(string_one, string_two, integer):
     list_one = list(string_one)
     
     for index in range(len(list_one)):
          
          if index == integer:
               list_one[index] = string_two
     
     PrintOutput(''.join(list_one))

def FindWordCount(a, string):
     count = 0
     
     for index in range(len(a)):
          
          if a[index] == string:
               count += 1
               
     PrintOutput(count)

def ScoreFinder(players, scores, player_name):
     players_string = ''
     
     for index in range(len(players)):
          
          players_string += players[index]
          players_string += ' '
     players_string = players_string.lower()
     players_list = players_string.split()
          
     for index in range(len(players_list)):

          if players_list[index] == player_name:
               i = index
               score = players[i] + ' got a score of ' + str(scores[i])
               break
          else:
               score = 'player not found'

     PrintOutput(score)
               

     

     
