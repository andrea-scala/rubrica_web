import pymysql
from dotenv import load_dotenv
import os
class DB:
    def __init__(self, config):
        load_dotenv()
        self.host = config.get("HOST", os.getenv("HOST"))
        self.port = config.get("PORT", os.getenv("PORT"))
        self.db = config.get("DB", os.getenv("DB"))
        self.username = config.get("USERNAME", os.getenv("USERNAME"))
        self.password = config.get("PASSWORD", os.getenv("PASSWORD"))
    def get_connection(self):
        return pymysql.connect(
            host        = self.host,
            port        = int(self.port),
            database    = self.db,
            user        = self.username,
            password    = self.password,
            cursorclass = pymysql.cursors.DictCursor
        )