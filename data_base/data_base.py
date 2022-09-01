from mysql.models import TableElements, TableNodes
from mysql.mysql_client import MySqlClient


class DataBase:
    def __init__(self):
        self.mysql_client = MySqlClient(user='root', password='pass', db_name='femdb')

    def mysql_client_connection(self):
        self.mysql_client.connect()

    def select_elements(self):
        elements = self.mysql_client.session.query(TableElements).all()
        return elements

    def select_nodes(self):
        nodes = self.mysql_client.session.query(TableNodes).all()
        return nodes
