#1. This program reads from a csv file which contains the data for top 100 hitters.

#2. Creates a list of tuples of the data that was inputted, and then sorts the data 
#   in descending order, where they are ranked by OBP

#3. Accesses the top 15 players with the best OBP

#4. Prints the current SF players that are in the top 100 hitters

#5. Prints the  fifteen players with the highest OBP so that the SF Giants
#   can consider trading for them or going after them in free agency
#6. If the SF Giants can't trade for or sign the top fifteen players,
#   they can choose from the list of players with an above average OBP

#Imports csv module
import csv
#inputs csv file with all the top 100 MLB OBP players for the 2021 season
fname = 'OBP for Python  Final - Sheet1.csv'
def main():
    #opens and reads the csv file
    with open(fname,'r') as csvfile:
        my_data = csv.reader(csvfile)
        
        #I needed to use lambda because of an error I was getting.
        #I looked it up on google, and found this python bug: https://github.com/python/mypy/issues/6697
        #It sugessted to use lambda as a workaround
        #Creates a list of tuples of my data
        players_list = list(map(lambda y: tuple(y),my_data))
        #calculate the average OBP of the top 100 hitters
        total_OBP = 0.0
        for row in players_list:
            #This is an arithmetic operation
            total_OBP = total_OBP + float(row[1])
        #This is a mathematical expression
        avg_OBP = total_OBP/100
        print('This is the average OBP of the top 100 hitters:', round(avg_OBP,3))
        print('')
        #list of all 100 players sorted by best OBP
        sorted_players_list = sorted(players_list, key=lambda player: player[1],reverse = True)
        # The top 15 players ranked by OBP
        top_fifteen = sorted_players_list[0:15]
        
        #calls print_sf_players that prints the SF players in the top 100 OBP players list
        print_sf_players(sorted_players_list)
        #calls print_top_fifteen that prints the top 15 OBP players 
        print_top_fifteen(top_fifteen)
        #calls print_above_avg which prints only the players with an above average OBP
        print_above_avg(sorted_players_list,avg_OBP)
        
        
 #function that prints the SF players in the top 100 OBP players list  
def print_sf_players(sorted_players_list):
    print('San Francisco players with an OBP in the top 100 ')
    print('(Name, OBP, Team)')
    print('')
    #iterates through the list of players and prints only the players that play for SF
    for row in sorted_players_list:       
        if (row[2] == 'SF'):
            print (row)
    
#prints print_top_fifteen that prints the top 15 OBP players                       
def print_top_fifteen(top_fifteen):
    print('')
    print('Top 15 of the players ranked by OBP ')
    print('(Name, OBP, Team)')
    print('')
    
    count = 0
    #prints the top fifteen players from the sorted list
    while(count >=0) and (count < len(top_fifteen)):
        
        print(top_fifteen[count])
        count += 1
        
    
#prints print_above_avg which prints only the players with an above average OBP
def print_above_avg(sorted_players_list,avg_OBP):
    print('')
    print('Players with above average OBP ')
    print('(Name, OBP, Team)')
    print('')
    #iterates through the list of players and prints only the players that have an above average OBP
    for row in sorted_players_list:       
        if (float(row[1]) >  avg_OBP):
            #This is a boolean expression
            ok_to_print = True
            if(ok_to_print):
                print (row)
 
#Call the main() function in the shell after compiling to get the output      
        
  
    







    
    


    
    
