import sqlite3

dbName = "storage.db"

# used to initialise the database for use. mostly needed on first time use of this api
def Init():
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
    except:
        print("unable to open database")
        return

    # create users table if it doesn't exist
    # userId: int (primary key) -- uuid for a given user
    # username: string -- it's a username idk what you want me to tell you
    try:
        print("creating users table...")
        cursor.execute("""
            CREATE TABLE users (
                userId   INTEGER NOT NULL PRIMARY KEY,
                username TEXT    NOT NULL
            )
        """)
        conn.commit()
        print("success")
    except:
        print("table already exists")

    # create patterns table if it doesn't exist
    # userId: int (composite primary key) -- uuid for user who owns this pattern
    # weekStart: int (composite primary key) -- unix timestamp of week start
    # prices: string -- serialised data for a week's prices
    # first: boolean -- is this the user's first week doing turnips?
    # pattern: int -- the pattern which the user had last week
    try:
        print("creating patterns table...")
        cursor.execute("""
            CREATE TABLE patterns (
                userId    INTEGER NOT NULL,
                weekStart INTEGER NOT NULL,
                prices    TEXT    NOT NULL,
                first     INTEGER NOT NULL,
                pattern   INTEGER NOT NULL,
                PRIMARY KEY(userId, weekStart)
            )
        """)
        conn.commit()
        print("success")
    except:
        print("table already exists")

    conn.close()
    return

# execute query on the database
def Execute(query, params=None, commit=False):
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
    except:
        return None

    try:
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        res = cursor.fetchall()
    except:
        return None

    # we only really need to commit if we add/alter records
    if commit:
        conn.commit()
    conn.close()

    return res