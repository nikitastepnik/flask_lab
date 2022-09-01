from math import sqrt

from data_base.data_base import DataBase


class Triangle:
    @staticmethod
    def prepare_nodes(nodes):
        parsed_nodes = str(nodes).replace('[', '').replace(']', '').split(',')
        prepared_nodes = {}
        for index in range(0, int(len(parsed_nodes) / 2)):
            value = [{'x': float(parsed_nodes[2 * index])}, {'y': float(parsed_nodes[2 * index + 1])}]
            prepared_nodes.update({f'{index + 1}': value})
        return prepared_nodes

    @staticmethod
    def prepare_elements(elements):
        parsed_elements = str(elements).replace('[', '').replace(']', '').split(',')
        prepared_elements = {}
        for index in range(0, int(len(parsed_elements))):
            split_elements = parsed_elements[index].lstrip(' ').split(' ')
            value = [{'n1': int(split_elements[0])}, {'n2': int(split_elements[1])}, {'n3': int(split_elements[2])}]
            prepared_elements.update({f'{index + 1}': value})
        return prepared_elements

    @staticmethod
    def calculate_length_of_sides_of_element(prep_nodes, prep_elem):
        length_of_sides = {}
        for i in range(0, len(prep_elem)):
            cur_iter = prep_elem.get(str(i + 1))
            n1 = str(cur_iter[0].get('n1'))
            n2 = str(cur_iter[1].get('n2'))
            n3 = str(cur_iter[2].get('n3'))

            x_n1 = prep_nodes.get(n1)[0]['x']
            y_n1 = prep_nodes.get(n1)[1]['y']

            x_n2 = prep_nodes.get(n2)[0]['x']
            y_n2 = prep_nodes.get(n2)[1]['y']

            x_n3 = prep_nodes.get(n3)[0]['x']
            y_n3 = prep_nodes.get(n3)[1]['y']

            n1_n2 = round(sqrt((x_n2 - x_n1) ** 2 + (y_n2 - y_n1) ** 2), 2)
            n1_n3 = round(sqrt((x_n3 - x_n1) ** 2 + (y_n3 - y_n1) ** 2), 2)
            n2_n3 = round(sqrt((x_n2 - x_n3) ** 2 + (y_n2 - y_n3) ** 2), 2)

            values = [{'n1_n2': n1_n2, 'n1_n3': n1_n3, 'n2_n3': n2_n3}]
            length_of_sides.update({i + 1: values})
        return length_of_sides

    @staticmethod
    def calculate_perimeter_of_elements(length_of_sides_of_elements):
        perimeters_of_elements = {"elem": [], "perimeter": []}
        for i in range(0, len(length_of_sides_of_elements)):
            cur_elem = length_of_sides_of_elements.get(i + 1)[0]
            perimetr_of_cur_elem = round((cur_elem.get('n1_n2') + cur_elem.get('n1_n3') + cur_elem.get('n2_n3')), 2)
            perimeters_of_elements["elem"].append(str(i + 1))
            perimeters_of_elements["perimeter"].append(perimetr_of_cur_elem)
        return perimeters_of_elements


triangle = Triangle()
data_base = DataBase()

data_base.mysql_client_connection()

elements_from_db = data_base.select_elements()
nodes_from_db = data_base.select_nodes()

prepared_nodes = Triangle.prepare_nodes(nodes_from_db)
prepared_elements = Triangle.prepare_elements(elements_from_db)

length_of_sides_of_elements = Triangle.calculate_length_of_sides_of_element(prepared_nodes, prepared_elements)
perimeters = Triangle.calculate_perimeter_of_elements(length_of_sides_of_elements)
