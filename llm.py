import json

import openai
from pydantic import BaseModel, Field


class User(BaseModel):
    """This is a basemodel"""
    name: str = Field("Name of user")
    age: int = Field("age of user")
    title_: str = Field("Title of the user")

    @property
    def openai_schema(self):
        data = self.model_json_schema()

        # Remove keys with name 'title'
        result = remove_keys_with_name(data, 'title')

        return result


def remove_keys_with_name(json_obj, key_to_remove):
    if isinstance(json_obj, dict):
        return {k: remove_keys_with_name(v, key_to_remove) for k, v in json_obj.items() if k != key_to_remove}
    elif isinstance(json_obj, list):
        return [remove_keys_with_name(item, key_to_remove) for item in json_obj]
    else:
        return json_obj

