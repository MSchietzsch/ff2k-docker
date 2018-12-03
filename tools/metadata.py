import sqlite3
from sqlite3 import Error
import sys
import json
import argparse
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('db', nargs='?', help='sqlite path', default="metadata-110mil.sqlite")
args = parser.parse_args()
db_file = args.db

try:
    conn = sqlite3.connect(db_file)
except Error as e:
    print(e)

c = conn.cursor()
cats = c.execute('select distinct Category from metadata;').fetchall()
conn.close()

catlist = list(cats)

my_flat_list = [item for sublist in catlist for item in sublist]

finallist = []

for i in my_flat_list:
    newlists = i.split(', ')
    finallist.append(newlists)

my_flat_list2 = [item for sublist in finallist for item in sublist]
my_flat_list2 = filter(None, my_flat_list2) # fastest

my_flat_list_strip = map(str.strip, my_flat_list2)

my_flat_list_strip = sorted(set(my_flat_list_strip))

array = []
count = 0
for i in my_flat_list_strip:
    count += 1
    name = (i[:64])
    new_set = {
        "model": "ff2ksite.Fandom",
        "pk": count,
        "fields": {
            "fandom_name": name.strip(),
            "fandom_descr": "add description",
            "fandom_short": count
        }
    }
    array.append(new_set)

array = json.dumps(array)
print(array, file=open("..\\django-site\\django-site\\ff2ksite\\fixtures\\fandoms.json", "w", encoding='utf8'))