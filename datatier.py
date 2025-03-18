# Name: Manan Patel
# UIN: 658283320
# NetID: mpate360@uic.edu

# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#
def select_one_row(dbConn, sql, parameters = None):
    if (parameters == None): #if no parameters then it passes empty list
        parameters = []
    try:
        dbCursor = dbConn.cursor()  #create a cursor
        dbCursor.execute(sql, parameters)  #execute query with sql and parameters
        row = dbCursor.fetchone()  #get the first row
        return row if row else () #if no row, return empty
    except Exception as err:  #exception
        print("Error:", err)
        return None
    finally: #close the cursor
        dbCursor.close()


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass
# the values as a list via parameters; this parameter
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the
#          given query; if an error occurs a msg is
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    if (parameters == None):  #if no parameters then it passes empty list
        parameters = []

    dbCursor = dbConn.cursor()  #create a cursor

    try:
        dbCursor.execute(sql, parameters)  #execute query with sql and parameters
        rows = dbCursor.fetchall()  #fetch all rows
        return rows
    except Exception as err:  #exception
        print("select_n_rows failed:", err)
        return None



##################################################################
#
# perform_action:
#
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert",
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an
#          error occurs a msg is output and -1 is
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g.
#          because the where condition was false?).
#
def perform_action(dbConn, sql, parameters = None):
    try:
        dbCursor = dbConn.cursor()  #create a cursor
        if parameters:
            dbCursor.execute(sql, parameters)  #if parameters then execute query with sql and parameters
        else:
            dbCursor.execute(sql)  #if not cursor then without parameters
        dbConn.commit()
        return dbCursor.rowcount  #returns numbers of rows
    except Exception as err:  #exception
        print("perform_action failed:", err)
        return -1

