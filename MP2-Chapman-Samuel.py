# import the required modules

import csv
import mymod
if __name__ == "__main__":
    file_name = input("Please enter the name of your file(including extension i.e. .csv .txt .xlsx). ")

    while True:
        try:

            elect_year = str(input("Please enter the election year."))
            if int(elect_year) % 4 != 0:
                print("Please enter a valid election year.")
                if int(elect_year) < 2016:
                    print("Please enter a valid election year.")
                if int(elect_year) > 1976:
                    print("Please enter a valid election year.")
            else:
                break
            
        except(TypeError):

            elect_year = str(input("Please enter a valid election year."))

        except(ValueError):

            elect_year = str(input("Please enter a valid election year."))

    def get_data(file, elect):
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['YEAR']==elect]
            file.close()
            print("There are", len(rows),"rows for this year.")
            return rows

##    def write_data(data, write_file):
##        try:
##            with open(write_file, 'w'):
##                write_file.writelines(data)
##                write_file.close()
##        except IOError:
##            print("No such file or directory")
##         
##        print("File saved.")
    
    data = get_data(file_name, elect_year)
    
    #print(data)
    while True:

        print("\nOption A","Given an election year, how many votes did each candidate receive total (in the whole country)?\n")
        print("\nOption B","Given an election year, how many votes did each party receive total (in the whole country)?\n")
        print("\nOption C","Given an election year, how many votes were “write-in” votes?\n")
        print("\nOption D","Given an election year, who won the popular vote?\n")
        user_choice = str(input("\nPlease select your choice, enter q to quit.\n"))

        if user_choice.lower() == 'q':
            break

        elif user_choice.lower() == 'a':
             print(mymod.table_print(mymod.tallied_data(data, "CANDIDATE", "VOTES"),['Candidate','Votes'],width = 50))

        elif user_choice.lower() == 'b':
            print(mymod.table_print(mymod.tallied_data(mymod.insertion_sort(data,'PARTY'), "PARTY", "VOTES"),['Party','Votes'],width = 50))
            
        elif user_choice.lower() == 'c':
            writein = dict(mymod.tallied_data(data, "WRITEIN", "VOTES"))

            print("In", elect_year, "there were",writein["TRUE"], "write in votes")

        elif user_choice.lower() == 'd':
            candidate = mymod.tallied_data(data, "CANDIDATE", "VOTES")

            print("In", elect_year,candidate[0][0], "won the popular vote.")

        else:
            print("That isn't a valid option")

##             print(mymod.table_print(mymod.tallied_data(mymod.insertion_sort(data,'TOTALVOTES'), "STATE", "TOTALVOTES"),['State','Total State']))
##             max_votes = []
##             for item in mymod.tallied_data(mymod.insertion_sort(data,'VOTES'), "CANDIDATE", "VOTES"):
##                max_votes.append(item[-1:8])
##             print(max_votes[max(max_votes)])
#1976-2016-president.csv
##
##    newtxtfile = str(input("Please enter your desired file name(Use .txt extension)."))
##
##    party = mymod.tallied_data(data, "PARTY", "VOTES")
##
##    for file in newtxtfile:
##        write_data(party[0][0],file)
        

# read in and clean up data

# write a function for each pf the 4 questions you want to answer

# write the main body of your code

#{'YEAR': '2012', 'STATE': 'Alabama', 'STATE_ABR': 'AL', 'CANDIDATE': 'Romney, Mitt', 'PARTY': 'republican', 'WRITEIN': 'FALSE', 'VOTES': '1255925', 'TOTALVOTES': '2074338'}


