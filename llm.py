import json

import openai
from pydantic import BaseModel, Field


def openai_schema(cls):
    data = cls.model_json_schema()

    # Remove keys with name 'title'
    return remove_keys_with_name(data, "title")


BaseModel.openai_schema = classmethod(openai_schema)


def remove_keys_with_name(json_obj, key_to_remove):
    if isinstance(json_obj, dict):
        return {
            k: remove_keys_with_name(v, key_to_remove)
            for k, v in json_obj.items()
            if k != key_to_remove
        }
    elif isinstance(json_obj, list):
        return [remove_keys_with_name(item, key_to_remove) for item in json_obj]
    else:
        return json_obj
