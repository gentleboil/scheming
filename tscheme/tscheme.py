# from jsonschema import validate, ValidationError, SchemaError
import jsonschema as js
from typing import List, Set, Dict, Tuple, Optional

def validate(json: Dict, schema: Dict):
    """
    docstring
    """
    try:
        js.validate(json, schema)

        print("it all went swimmingly")
    
    except js.SchemaError as e:
        print("There is an error with the schema")
        
    except js.ValidationError as e:
        print("Error in json", e)
        
        # print("---------")
        # print(e.absolute_path)
    
        # print("---------")
        # print(e.absolute_schema_path)
    
    pass


if __name__ == "__main__":

    print ("hello world")

    schema = {
        "type" : "object",
        "properties" : {
            "name" : {"type" : "string"},
            "age" : {
                "type" : "number",
            }
        },
        "required": ["age","name","xxx"]
    }

    validJson = {"name" : "Eggs", "age" : 10}
    invalidJson =  {"name" : "Eggs", "age":"string"}

    # with open('schema-example.json', 'r') as f:
    #     schema_data = f.read()
    
    # schema = json.loads(schema_data)

    # with open('example.json', 'r') as f:
    #     json_data = f.read()
    
    # json_obj = json.loads(json_data)

    validate(validJson, schema)

    validate(invalidJson, schema)