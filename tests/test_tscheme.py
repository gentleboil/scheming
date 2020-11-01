import pytest
from tscheme import validate
schema = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "age" : {
            "type" : "number",
        }
    },
    "required": ["age","name"]
}

badSchema = {
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

def test_valid_json():
    assert validate(validJson, schema)

def test_invalid_json():
    assert validate(invalidJson, schema)

def test_invalid_schema():
    assert validate(validJson, badSchema)