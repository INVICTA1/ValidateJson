import json
import os
from jsonschema import validate
import jsonschema
from jsonschema.exceptions import ValidationError

path_json = 'event/'
path_schema = 'schema/'
result = 'answer_file/'


def open_files_in_dir(path_dir):
    mass_files = []
    for root, dir, files in os.walk(path_dir):
        for file in files:
            mass_files.append(path_dir + file)
    return mass_files


def write_answer(json_path, schema_path, isValid):
    name = result + str(json_path).split('.')[0] + str(schema_path).split('.')[0]
    with open(name, 'a') as answer:
        answer.write(isValid)


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
            with open(path_json_file) as json_file:
                json_text = json.load(json_file)
                for schema in schemas_list:
                    try:
                        validate(instance=json_text, schema=schema)
                        # write to success folder
                        write_answer(path_json_file, schema_file, isValid)
                    except BaseException as e:
                        # write to wrong folder
                        write_answer(path_json_file, schema_file,e)

        except BaseException:
            print('Json не открыается')
            continue


def main():
    try:
        path_json_files = open_files_in_dir(path_json)
        path_schema_files = open_files_in_dir(path_schema)
        schema = create_list_code_schema(path_schema_files)
        validate_json_schema(path_json_files, schema)

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
