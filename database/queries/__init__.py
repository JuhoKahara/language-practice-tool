cursor = ''

def set_cursor(c):
    global cursor
    cursor = c

def query(query, *args):
    if args:
        return cursor.execute(query, args).fetchone()
    else:
        return cursor.execute(query).fetchall()
