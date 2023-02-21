from sqlalchemy import create_engine
from sqlalchemy import text

class PostgresHandler:
    def __init__(self, postgres_url):
        self.engine = create_engine(postgres_url)
        # self.create_objects()

    def run_query(self, query, data=None):
        with self.engine.connect() as conn: 
            try:
                if not data:
                    conn.execute(text(query))
                else:
                    for item in data:
                        conn.execute(text(query), **item)                
            except Exception as e:                
                print(str(e))