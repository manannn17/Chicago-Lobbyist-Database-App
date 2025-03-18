#
# header comment!
#
# Name: Manan Patel
# UIN: 658283320
# NetID: mpate360@uic.edu

import sqlite3
import objecttier


# prints general statistics
def display_statistics(dbConn):
    print('** Welcome to the Chicago Lobbyist Database Application **')
    print("General Statistics:")

    #Get the total number of lobbyists, employers, and clients from the database.
    Num_Lobbyists=objecttier.num_lobbyists(dbConn)
    Num_Employers=objecttier.num_employers(dbConn)
    Num_Clients=objecttier.num_clients(dbConn)

    #print the data
    print(f"  Number of Lobbyists: {Num_Lobbyists:,}")
    print(f"  Number of Employers: {Num_Employers:,}")
    print(f"  Number of Clients: {Num_Clients:,}")


def command_1(dbConn):
    search_term=input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ") #get the input
    lobbyists=objecttier.get_lobbyists(dbConn, search_term) #get the data from get_lobbyists table
    print(f"\nNumber of lobbyists found: {len(lobbyists)}") #print the number of lobbies

    lobbyist_count=len(lobbyists)  #get the count of lobbyists

    if lobbyist_count > 100: #print the message if it is more than 100
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")
    else: #print each lobbyist's ID, full name, and phone number
        for lobbyist in lobbyists:
            print(f"{lobbyist.Lobbyist_ID} : {lobbyist.First_Name} {lobbyist.Last_Name} Phone: {lobbyist.Phone}")


def command_2(dbConn):
    lobbyist_id=input("\nEnter Lobbyist ID: ") #get the input

    try: #check if input is a valid integer
        lobbyist_id=int(lobbyist_id)
    except ValueError:
        print("Error: The ID must be a valid number.")
        return

    details=objecttier.get_lobbyist_details(dbConn, lobbyist_id) #get the data from the get_lobbyist_details table

    if details is None: #if no found then print the message
        print("\nNo lobbyist with that ID was found.")
        return
    if details:  #Print the lobbyist details if found
        # Print the fetched details
        print(f"\n{lobbyist_id} :")
        print(f"  Full Name: {details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix}")
        print(f"  Address: {details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} {details.Zip_Code} {details.Country}")
        print(f"  Email: {details.Email}")
        print(f"  Phone: {details.Phone}")
        print(f"  Fax: {details.Fax}")
        print(f"  Years Registered: {', '.join(map(str, details.Years_Registered))}, ")
        print(f"  Employers: {', '.join(details.Employers)}, ")
        print(f"  Total Compensation: ${details.Total_Compensation:,.2f}")

def command_3(dbConn):
    try:
        N=int(input("\nEnter the value of N: ")) #get the input
        if N<=0: #check if N is positive
            raise ValueError
    except ValueError:
        print("Please enter a positive value for N...")
        return

    year=input("Enter the year: \n") #get the year
    top_lobbyists=objecttier.get_top_N_lobbyists(dbConn, N, year) #get the data from get_top_N_lobbyists table

    # if not top_lobbyists:
    #     print(f"No lobbyists found for the year {year}.")
    #     return

    for count, lobbyist in zip(range(1, N + 1), top_lobbyists):  #Print the top N lobbyists' details
        full_name=f"{lobbyist.First_Name} {lobbyist.Last_Name}"
        formatted_comp="${:,.2f}".format(lobbyist.Total_Compensation)
        clients_list=sorted(lobbyist.Clients)  # Clients sorted in a different step
        print(f"{count} . {full_name}\n  Phone: {lobbyist.Phone}\n  Total Compensation: {formatted_comp}")
        print(f"  Clients: {', '.join(clients_list)}, ")

def command_4(dbConn):
    try:
        year=input("\nEnter year: ")  #get the year
        lobbyist_id=input("Enter the lobbyist ID: ") #get Lobbyist ID

        result=objecttier.add_lobbyist_year(dbConn, lobbyist_id, year) #get the data from add_lobbyist_year table
        if result==1:  #if result is 1 then print the message
            print("\nLobbyist successfully registered.")
        else: #if not then shows id was not found
            print("\nNo lobbyist with that ID was found.")
            # print(f"Lobbyist with ID {lobbyist_id} is already registered for the year {year}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def command_5(dbConn):
    try:
        lobbyist_id=input("\nEnter the lobbyist ID: ") #get the lobbyist id
        salutation=input("Enter the salutation: ") #get the salutation

        result=objecttier.set_salutation(dbConn, lobbyist_id, salutation) #get the data from set_salutation table

        if not result: #if not result then print the message
            print("\nNo lobbyist with that ID was found.")
            return
        print("\nSalutation successfully set.") #Success Salutation message

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    dbConn = sqlite3.connect('Chicago_Lobbyists.db')  #connect to database
    display_statistics(dbConn)  #calling general statistics

    while True: #Menudriven Program
        command=input("Please enter a command (1-5, x to exit): ").strip().lower()

        if command.lower()=='x':
            # print("Exiting the program.")
            break
        elif command=='1':
            command_1(dbConn)
        elif command=='2':
            command_2(dbConn)
        elif command=='3':
            command_3(dbConn)
        elif command=='4':
            command_4(dbConn)
        elif command=='5':
            command_5(dbConn)
        else: #else if not from the above commands then shows this message
            print("**Error, unknown command, try again...")


if __name__ == "__main__":
    main() #calling main function