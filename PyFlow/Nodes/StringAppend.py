from Node import Node
from AbstractGraph import *


class StringAppend(Node, NodeBase):
    def __init__(self, name, graph):
        super(StringAppend, self).__init__(name, graph)
        self.first = self.add_input_port('first', DataTypes.String)
        self.second = self.add_input_port('second', DataTypes.String)
        self.output = self.add_output_port('output', DataTypes.String)
        portAffects(self.first, self.output)
        portAffects(self.second, self.output)

    @staticmethod
    def category():
        return 'String'

    def compute(self):

        first_str = self.first.get_data()
        second_str = self.second.get_data()
        try:
            result = first_str + second_str
            self.output.set_data(result)
        except Exception, e:
            print e
