from fastapi import FastAPI

from db.db_operations import (
    select_count_from_first_row,
    increment_table_counter,
    create_table_and_insert_row,
)


class GlobalVariables:
    def __int__(self):
        print("GlobalVariables set up")


_globals = GlobalVariables()
_globals.db_is_online = False


app = FastAPI()


@app.get("/")
def endpoint_a_root():
    if not _globals.db_is_online:
        create_table_and_insert_row()
        _globals.db_is_online = True
    count = select_count_from_first_row()
    increment_table_counter(count)
    return {"message": f"Endpoint was called {count} times"}
