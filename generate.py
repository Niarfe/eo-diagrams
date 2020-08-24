import sys
from collections import namedtuple


def prow(row):
    return "{}{}{}{}".format(row.id.ljust(10), row.status.ljust(10), row.desc.ljust(40), row.parent.ljust(10))
Row = namedtuple('Row', ['id', 'status', 'desc', 'parent'])

rows = []
with open(sys.argv[1], 'r') as source:
    for row in source:
        try:
            id, status, desc, parent = row.strip().split(',')
        except Exception as e:
            print("Error: Skipping row with content <{}>".format(row))
            continue
        rows.append(Row(id=id, status=status, desc=desc, parent=parent))


#print("{} rows loaded".format(len(rows)))
#for RN, row in enumerate(rows):
#    print(RN, prow(row))

print("graph LR")
print()

def merm_to_parent(row):
    return "{pid}[{pid} {pdesc}] --> {rid}[{rid} {rdesc}]".format(pid=row.parent, pdesc="", rid=row.id, rdesc=row.desc)

for row in rows[1:]:
    print(merm_to_parent(row))
    

print()
print("classDef Active      fill:#3499DB;")
print("classDef InRelease   fill:#82E0AA;")
print("classDef Closed      fill:#566573;")
print()

for row in rows[1:]:
    print("class {} {}".format(row.id, row.status))
