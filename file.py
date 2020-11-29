import json
import os
from jsonschema import validate
import jsonschema
from jsonschema.exceptions import ValidationError

path_json = 'event/'
path_schema = 'schema/'
result_folder = 'result/'


def open_files_in_dir(path_dir):
    mass_files = []
    for root, dir, files in os.walk(path_dir):
        for file in files:
            mass_files.append([path_dir + file, file])
    return mass_files


def write_to_file(file_path, content,method):
    with open(file_path, method) as answer:
        answer.write(content)


def create_list_code_schema(path_schema_files):
    schema_cod = []
    for schema_file in path_schema_files:
        try:
            with open(schema_file) as schema_file:
                schema_cod.append(json.load(schema_file))
        except BaseException:
            print('Schema не открыается', schema_file)
    return schema_cod


def validate_json_schema(path_json_files, schemas_list):
    for path_json_file in path_json_files:
        try:
            with open(path_json_file[0]) as json_file:
                json_text = json.load(json_file)
                for schema in schemas_list:
                    name = result_folder + str(path_json_file[1]).split('.')[0] +'-'+ str(schema[1]).split('.')[
                        0] + '.txt'
                    try:
                        validate(instance=json_text, schema=schema[0])
                        write_to_file('Success_file',str(path_json_file[1]) + ' and ' +  str(schema[1]),'a')
                    except BaseException as e:
                        write_to_file(name, str(e),'w+')

        except BaseException as err:
            write_to_file(result_folder+'file_not_open',str(path_json_file[1]),'a')
            continue


def main():
    try:
        path_json_files = open_files_in_dir(path_json)
        path_schema_files = open_files_in_dir(path_schema)
        validate_json_schema(path_json_files, path_schema_files)

        #
        # with open(path) as json_file:
        #     json_file = json.load(json_file)
        #     if str(json_file).lower() == 'none':
        #         return 'The file does not contain correct information.', str(json_file)
        #     for key in json_file:
        #         if key in json_file == False :
        #             return 'Not data'
        #     return path, 'open'
    except Exception as e:
        return 'The file is not written correctly', str(e)


main()
