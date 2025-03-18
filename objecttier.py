# Name: Manan Patel
# UIN: 658283320
# NetID: mpate360@uic.edu

# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
# @property
class Lobbyist:  #all properties of Lobbyist
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone




##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
# @property
class LobbyistDetails:  #all properties of LobbyistDetails
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax
                , Years_Registered, Employers, Total_Compensation):
       self._Lobbyist_ID = Lobbyist_ID
       self._Salutation = Salutation
       self._First_Name = First_Name
       self._Middle_Initial = Middle_Initial
       self._Last_Name = Last_Name
       self._Suffix = Suffix
       self._Address_1 = Address_1
       self._Address_2 = Address_2
       self._City = City
       self._State_Initial = State_Initial
       self._Zip_Code = Zip_Code
       self._Country = Country
       self._Email = Email
       self._Phone = Phone
       self._Fax = Fax
       self._Years_Registered = Years_Registered
       self._Employers = Employers
       self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self):
       return self._Lobbyist_ID

   @property
   def Salutation(self):
       return self._Salutation

   @property
   def First_Name(self):
       return self._First_Name

   @property
   def Middle_Initial(self):
       return self._Middle_Initial

   @property
   def Last_Name(self):
       return self._Last_Name

   @property
   def Suffix(self):
       return self._Suffix

   @property
   def Address_1(self):
       return self._Address_1

   @property
   def Address_2(self):
       return self._Address_2

   @property
   def City(self):
       return self._City

   @property
   def State_Initial(self):
       return self._State_Initial

   @property
   def Zip_Code(self):
       return self._Zip_Code

   @property
   def Country(self):
       return self._Country

   @property
   def Email(self):
       return self._Email

   @property
   def Phone(self):
       return self._Phone

   @property
   def Fax(self):
       return self._Fax

   @property
   def Years_Registered(self):
       return self._Years_Registered

   @property
   def Employers(self):
       return self._Employers

   @property
   def Total_Compensation(self):
       return self._Total_Compensation



##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
# @property
class LobbyistClients:  #all properties of LobbyistClients
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
       self._Lobbyist_ID = Lobbyist_ID
       self._First_Name = First_Name
       self._Last_Name = Last_Name
       self._Phone = Phone
       self._Total_Compensation = Total_Compensation
       self._Clients = Clients

   @property
   def Lobbyist_ID(self):
       return self._Lobbyist_ID

   @property
   def First_Name(self):
       return self._First_Name

   @property
   def Last_Name(self):
       return self._Last_Name

   @property
   def Phone(self):
       return self._Phone

   @property
   def Total_Compensation(self):
       return self._Total_Compensation

   @property
   def Clients(self):
       return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   query="select count(*) from LobbyistInfo" #select query to get LobbyistInfo
   row=datatier.select_one_row(dbConn, query)
   if row is None:  #if none then return -1
      return -1
   return row[0]

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   query="select count(*) from EmployerInfo" #select query to get EmployerInfo
   row=datatier.select_one_row(dbConn, query)
   if row is None:  #if none then return -1
      return -1
   return row[0]

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   sql="select count(*) from ClientInfo"
   row=datatier.select_one_row(dbConn, sql)  #select query to get ClientInfo
   if row is None:
      return -1  #if none then return -1
   return row[0]

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    query = ("select Lobbyist_ID, First_Name, Last_Name, Phone "  #query to get LoggyistInfo
             "from LobbyistInfo "
             "where First_Name like ? or Last_Name like ? "  
             "order by Lobbyist_ID asc")

    rows = datatier.select_n_rows(dbConn, query, [pattern, pattern])

    if rows is None:  #if none, return []
        return []

    lobbyists = []
    for row in rows:  #get all data in the row
        lobbyists.append(Lobbyist(row[0], row[1], row[2], row[3]))

    return lobbyists

##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).


#I divided get_lobbyist_detail in 5 parts where first for lobbyistInfo,
# 2nd for LoggyistYears,
# 3rd for EmployerInfor and join LobbyistAndEmployer
# 4th for compensation
# and in 5th I have used all years registration, employers, and total compensation
def fetch_lobbyist_info(dbConn, lobbyist_id):
    query = """
            select Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix,
                   Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax
            from LobbyistInfo
            where Lobbyist_ID = ?;
        """
    return datatier.select_one_row(dbConn, query, [lobbyist_id])

def fetch_years_registered(dbConn, lobbyist_id):
    query = """
        select distinct Year
        from LobbyistYears
        where Lobbyist_ID = ?;
    """
    yearsRows = datatier.select_n_rows(dbConn, query, [lobbyist_id])
    return [row[0] for row in yearsRows]

def fetch_employers(dbConn, lobbyist_id):
    query = """
            select distinct Employer_Name
            from EmployerInfo e
            join LobbyistAndEmployer lae ON e.Employer_ID = lae.Employer_ID
            where lae.Lobbyist_ID = ?
            order by Employer_Name;
        """
    employersRows = datatier.select_n_rows(dbConn, query, [lobbyist_id])
    return [row[0] for row in employersRows]

def fetch_total_compensation(dbConn, lobbyist_id):
    query = """
            select sum(Compensation_Amount)
            from Compensation
            where Lobbyist_ID = ?;
        """
    compensationRow = datatier.select_one_row(dbConn, query, [lobbyist_id])
    return compensationRow[0] if compensationRow[0] is not None else 0.00


def get_lobbyist_details(dbConn, lobbyist_id):
    try:
        lobbyistRow = fetch_lobbyist_info(dbConn, lobbyist_id)
        if not lobbyistRow:
            return None

        yearsRegistered = fetch_years_registered(dbConn, lobbyist_id)
        employers = fetch_employers(dbConn, lobbyist_id)
        totalCompensation = fetch_total_compensation(dbConn, lobbyist_id)

        return LobbyistDetails(
            lobbyistRow[0], lobbyistRow[1], lobbyistRow[2], lobbyistRow[3], lobbyistRow[4],
            lobbyistRow[5], lobbyistRow[6], lobbyistRow[7], lobbyistRow[8], lobbyistRow[9],
            lobbyistRow[10], lobbyistRow[11], lobbyistRow[12], lobbyistRow[13], lobbyistRow[14],
            yearsRegistered, employers, totalCompensation
        )
    except:
        return None


def get_top_N_lobbyists(dbConn, N, year):
    try:
        # First query to get the top N lobbyists and their total compensation
        sql = '''
                    select L.Lobbyist_ID, L.First_Name, L.Last_Name, L.Phone, 
                           sum(C.Compensation_Amount) as total
                    from LobbyistInfo L
                    join Compensation C on L.Lobbyist_ID = C.Lobbyist_ID
                    where substr(C.Period_Start, 1, 4) = ? and substr(C.Period_End, 1, 4) = ?
                    group by L.Lobbyist_ID
                    order by total desc
                    LIMIT ?
                  '''

        rows = datatier.select_n_rows(dbConn, sql, [year, year, N])

        lobbyList = [] #deeclaring to get the data and assign to lobbyList

        # Second query to get clients for each lobbyist
        sqlClient = '''
                        select distinct CI.Client_Name, CI.Client_ID
                        from Compensation C
                        join ClientInfo CI on C.Client_ID = CI.Client_ID
                        where C.Lobbyist_ID = ?
                        and substr(C.Period_Start, 1, 4) = ? and substr(C.Period_End, 1, 4) = ?
                        order by CI.Client_Name;
                          '''

        for row in rows:  #get the lobby data from the first query
            lobbyist_id = row[0]
            first_name = row[1]
            last_name = row[2]
            phone = row[3]
            totalCompensation = row[4] if row[4] is not None else 0.00

            # Fetch clients for this lobbyist
            client_rows = datatier.select_n_rows(dbConn, sqlClient, [lobbyist_id, str(year), str(year)])
            clients = [client_row[0] for client_row in client_rows]  # Extract client names

            # Add the LobbyistClients object with client names
            lobbyList.append(LobbyistClients(lobbyist_id, first_name, last_name, phone, totalCompensation, clients))

        return lobbyList

    except: return []


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    try:
        sql = "select * from LobbyistYears where Lobbyist_ID = ?"  #select query to get lobbyYears
        row = datatier.select_one_row(dbConn, sql, [lobbyist_id])
        if row:
            sql = "insert into LobbyistYears (Lobbyist_ID, Year) values (?, ?)"  #Insert the year for the lobbyist
            lYear = datatier.perform_action(dbConn, sql, [lobbyist_id, year])
            return 1
        return 0
    except:
        return 0


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    try:
        sql = "update LobbyistInfo set Salutation = ? where Lobbyist_ID = ?" #update the lobbyistInfo in salutation
        row = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
        return row
    except:
        return 0