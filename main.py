from fastapi import FastAPI

from db.db_operations import select_count_from_first_row, increment_table_counter, create_table_and_insert_row

app = FastAPI()


@app.get("/")
def endpoint_a_root():
    count = select_count_from_first_row()
    increment_table_counter(count)
    return {"message": f"Endpoint was called {count} times"}


@app.get("/ct/")
def endpoint_a_root():
    create_table_and_insert_row()
    return {"message": f"Table initialized"}

