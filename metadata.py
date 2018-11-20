import sqlite3
from sqlite3 import Error
import sys
import json
import pprint

db_file = "metadata-110mil.sqlite"

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
my_flat_list2 = sorted(set(my_flat_list2))

#unique_short = []
array = []
count = 0
for i in my_flat_list2:
    count += 1
    name = (i[:64])
    short = (i[:8])
#    unique_short.append(short)
    new_set = {
        "model": "ff2ksite.Fandom",
        "pk": count,
        "fields": {
            "fandom_name": name.lstrip().rstrip(),
            "fandom_descr": "add description",
            "fandom_short": short.lstrip().rstrip()
        }
    }
    array.append(new_set)

#print("", file=open("unique_short.txt", "w", encoding='utf8'))
#for i in unique_short:
#    if (unique_short.count(i) > 1):
#        print(i, file=open("unique_short.txt", "a", encoding='utf8'))

array = json.dumps(array)
print(array, file=open("fandoms.json", "w", encoding='utf8'))


