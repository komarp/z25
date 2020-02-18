import json
import csv
import pickle
import xml.etree.ElementTree as etree
import sys

 ###################################################################
# parse_xml_function


def parse_xml(file_r):
    tree = etree.parse(file_r)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result


# Json_reader
def json_reader(file_r):
    with open(file_r) as file:
        content = json.load(file)
        return content


# CSV writer
def csv_writer(file_w, result):
    with open(file_w, 'w') as filew:
        fieldnames = list(result[0].keys())
        writer = csv.DictWriter(filew, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)


# pickle writer
def pickle_writer(file_w, result):
    with open(file_w, 'wb') as filew:
        pickle.dump(result, filew)


# pickle reader
def pickle_reader(file_r):
    with open(file_r, 'rb') as filer:
        content = pickle.load(filer)
        return content


 #################################################################
def data_format(file_r=sys.argv[1], file_w=sys.argv[2]):
    if file_w == 'print':
        with open(file_r) as filer:
            print(filer.read())
            return None
    # XML >> JSON
    if file_r.endswith('.xml') and file_w.endswith('.json'):
        result = parse_xml(file_r)
        with open(file_w, 'w') as filew:
            json.dump(result, filew, indent=4)
    # XML >> CSV
    elif file_r.endswith('.xml') and file_w.endswith('.csv'):
        result = parse_xml(file_r)
        result = [result]
        with open('_data_.csv', 'w') as filew:
            fieldnames = list(result[0].keys())
            writer = csv.DictWriter(filew, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)
    # XML >> pickle
    elif file_r.endswith('.xml') and file_w.endswith('.txt'):
        result = parse_xml(file_r)
        with open('_data_.txt', 'wb') as filew:
            pickle.dump(result, filew)
    # JSON >> XML
    if file_r.endswith('.json') and file_w.endswith('.xml'):
        result = json_reader(file_r)
        with open(file_w, 'w') as filew:
            _str = """
            <user>
                <name>{name}</name>
                <surname>{surname}</surname>
                <age>{age}</age>
                <sex>{sex}</sex>
                <education>{education}</education>
            </user>
            """
            new_str = _str.format(**result)
            for line in new_str:
                filew.write(line.lstrip())
    # JSON >> CSV
    elif file_r.endswith('.json') and file_w.endswith('.csv'):
        result = [json_reader(file_r)]
        csv_writer(file_w, result)
    # JSON >> pickle
    elif file_r.endswith('.json') and file_w.endswith('.txt'):
        result = json_reader(file_r)
        pickle_writer(file_w, result)
    # CSV >> JSON
    if file_r.endswith('.csv') and file_w.endswith('.json'):
        with open(file_r) as filer:
            reader = csv.DictReader(filer)
            with open(file_w, 'w') as filew:
                for elem in reader:
                    json.dump(elem, filew, indent=4)
    # CSV >> XML
    elif file_r.endswith('.csv') and file_w.endswith('.xml'):
        with open(file_r) as filer:
            reader = csv.DictReader(filer)
            reader = list(reader)
            with open(file_w, 'w') as filew:
                _str = """
            <user>
                <name>{name}</name>
                <surname>{surname}</surname>
                <age>{age}</age>
                <sex>{sex}</sex>
                <education>{education}</education>
            </user>
            """
                for line in _str.format(**reader[0]):
                    filew.write(line.lstrip())
    # CSV >> pickle
    elif file_r.endswith('.csv') and file_w.endswith('.txt'):
        with open(file_r) as filer:
            reader = csv.DictReader(filer)
            reader = list(reader)
            pickle_writer(file_w, reader[0])
    # pickle >> json
    if file_r.endswith('.txt') and file_w.endswith('.json'):
        result = pickle_reader(file_r)
        with open(file_w, 'w') as filew:
            json.dump(result, filew, indent=4)
    # pickle >> CSV
    elif file_r.endswith('.txt') and file_w.endswith('.csv'):
        result = pickle_reader(file_r)
        result = [result]
        csv_writer(file_w, result)
    # pickle >> XML
    elif file_r.endswith('.txt') and file_w.endswith('.xml'):
        result = pickle_reader(file_r)
        with open(file_w, 'w') as filew:
            _str = """
        <user>
            <name>{name}</name>
            <surname>{surname}</surname>
            <age>{age}</age>
            <sex>{sex}</sex>
            <education>{education}</education>
        </user>
        """
            for line in _str.format(**result):
                filew.write(line.lstrip())


data_format()

