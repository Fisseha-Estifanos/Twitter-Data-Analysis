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


def execute_query(connection: sqlite3.Connection, query:str) -> None:
    """
    A data base query executor method, based on a given connection string and a query string

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

    try:
        cursor.execute(sql_query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def insert_to_tweet_table(connection: sqlite3.Connection, df: pd.DataFrame, table_name: str) -> None:
    """
    A method to insert dataframe data into a data base

    Parameters
    ----------
    connection :
        sqlite3.Connection : the database connection
    df :
        pd.DataFrame : the dataframe
    table_name :
        str : the tablename
    Returns :
        nothing
    -------
    """
    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (created_at, source, original_text, polarity, subjectivity, lang, favorite_count, statuses_count, retweet_count, screen_name, original_author, followers_count, friends_count, possibly_sensitive, hashtags, user_mentions, place, clean_hashtags, clean_mentions)
             VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])

        try:
            cur = connection.cursor()
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            connection.commit()
            print(f"{_}: Data Inserted Successfully")
            cur.close()
        except Exception as e:
            connection.rollback()
            print("Error: ", e)
    return


def db_execute_fetch(connection:sqlite3.Connection, selection_query : str, dbName : str, rdf=True, many = False) -> pd.DataFrame:
    """
    A method to execute a fetch query based on a given selection query 

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :

    Returns
    -------
    Dataframe:
        pandas dataframe
    """   
    
    cursor1 = connection.cursor()
    result = None
    try:
        cursor1.execute(selection_query)
        result = cursor1.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")

    #print(result[0], end="\n\n")
    # get column names
    field_names = [i[0] for i in cursor1.description]

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(result, columns=field_names)
    else:
        return result


if __name__ == "__main__":
    connection = DBConnect(dbName='tweets.db')
    execute_query(connection=connection, query='create_table.sql')

    df = pd.read_csv('clean_data.csv')
    sample_df = df.copy()
    
    insert_to_tweet_table(connection=connection, df=sample_df, table_name='TweetInformation')

    select_query = "select * from TweetInformation"
    returned_df = db_execute_fetch(connection, select_query, dbName="tweets.db", rdf=True)
    returned_df.info()
