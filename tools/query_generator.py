from string import Template

class query_setup:
    def __init__(self,query_template) :
        self.sql_file = open(query_template)
        self.sql_as_string = self.sql_file.read()

    def get_query(self,rule_dict):
        self.sql_template = Template(self.sql_as_string)
        self.sql_input = self.sql_template.substitute(rule_dict)
        return self.sql_input