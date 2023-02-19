from sqlglot.parser import Parser

def extract_table_columns(sql_query):
    parser = Parser()
    parsed = parser.parse(sql_query)
    if not parsed:
        raise ValueError("Failed to parse SQL query")
    if parsed.get("type") != "create_table":
        raise ValueError("Expected a CREATE TABLE query")

    table_name = parsed.get("name")
    columns = [c.get("name") for c in parsed.get("columns")]
    return table_name, columns

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    def fullname(self):
        return '{}.{}'.format(self.first,self.last)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)