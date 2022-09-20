import csv
from functools import lru_cache


@lru_cache
def read(path):
   with open(path, encoding="utf8") as file:
        result = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in result]
