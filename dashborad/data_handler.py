import os
import sys
import pandas as pd
import sqlite3
from sqlite3 import Error


sys.path.append(os.path.abspath(os.path.join("../..")))
sys.path.append(".")
sys.path.append("..")
from defaults import *

def DBConnect(dbName=None):
    """
    Parameters
    ----------
    dbName :
        Default value = None
        string : the database name

    Returns :
        sqlite.connection : the database connection
    -------
    """
    conn = sqlite3.connect(dbName)
    print(conn)
    return conn


def execute_query(connection: sqlite3.Connection, query:str) -> None:
    """
    Parameters
    ----------
    connection :
        sqlite3.Connection : the database connection
    query :
        string : the query string
    Returns :
    -------
    return : nothing
    """

    cursor = connection.cursor()
    fd = open(query, 'r')
    sql_query = fd.read()
    fd.close()


if __name__ == "__main__":
    connection = DBConnect(dbName='tweets.db')
    execute_query(connection=connection, query='create_table.sql')
