"""Sorting Test"""

from pprint import pprint
from typing import Any, Union

FIELDS_LIST = [
    {"uuid": "uuid1", "sort": 1},
    {"uuid": "uuid2", "sort": 2},
    {"uuid": "uuid3", "sort": 3},
    {"uuid": "uuid4", "sort": 4},
    {"uuid": "uuid5", "sort": 5},
]


def update_position_db(
    field_uuid: str, new_pos: int, fields_list: list[dict[str, Any]]
) -> int:
    """Updates position in db"""
    for field in fields_list:
        if field.get("uuid") == field_uuid:
            current_pos = field.get("sort")
            field["sort"] = new_pos

    return current_pos


def sort_list(fields_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sorts the fields list"""
    return sorted(fields_list, key=lambda x: x["sort"])


def update_position(
    field_uuid: str, new_pos: int, fields_list: list[dict[str, Any]]
) -> Union[dict, str]:
    """Update the position of a field"""
    current_pos = update_position_db(field_uuid, new_pos, fields_list)

    if new_pos > len(fields_list) or new_pos < 1 or new_pos == current_pos:
        return "Invalid number"

    if current_pos < new_pos:
        for field in fields_list[current_pos:new_pos]:
            field["sort"] -= 1
    elif new_pos < current_pos:
        for field in fields_list[new_pos - 1 : current_pos - 1]:
            field["sort"] += 1

    return sort_list(fields_list)


pprint(update_position("uuid5", 1, sort_list(FIELDS_LIST)), sort_dicts=False)
pprint(update_position("uuid1", 5, sort_list(FIELDS_LIST)), sort_dicts=False)
pprint(update_position("uuid3", 2, sort_list(FIELDS_LIST)), sort_dicts=False)
