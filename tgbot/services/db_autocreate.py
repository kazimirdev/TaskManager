import sqlite3


def db_check(path):
    try:
        print("------", "File has been created", "-------", sep="\n")
        db_conn = sqlite3.connect(path)
        print("------", "Connect to DB", "-------", sep="\n")
        db_cursor = db_conn.cursor()
        print("------", "Using cursor", "-------", sep="\n")
        db_cursor.execute(
                """
                CREATE TABLE tasks (
                user_id int not null,
                task_id bigint unique not null,
                name tinytext not null, 
                description text not null, 
                timezone tinytext not null, 
                user_date datetime2 not null, 
                server_date datetime2 not null, 
                is_active bool);
                """) 
        print("------", "Table has been created", "-------", sep="\n")
        db_conn.commit()
        print("------", "Commit has been created", "-------", sep="\n")
        db_conn.close()
        print("------", "DB has been closed", "-------", sep="\n")
    except sqlite3.OperationalError:
        pass

