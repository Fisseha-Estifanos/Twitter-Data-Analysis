# import libraries
import pandas as pd
import sqlite3
from sqlite3 import Error


def DBConnect(dbName=None):
    """
    A data base connection creator method

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
