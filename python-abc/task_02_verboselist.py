#!/usr/bin/python3

from typing import Iterable

class VerboseList(list):
    def append(self, element):
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, delete):
        super().remove(delete)
        print(f"Removed [{delete}] from the list.")

    def pop(self, index: int = -1):
        items = super().pop(index)
        print(f"Popped [{items}] from the list.")
        return items