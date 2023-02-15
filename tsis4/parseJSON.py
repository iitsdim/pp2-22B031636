import json

with open("sample-data.json", 'r') as f:
    jsondata = json.loads(f.read())

print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n"
    "-------------------------------------------------- --------------------  ------  ------")
for line in jsondata["imdata"]:
    print("{0:50} {1:20} {2:7} {3:6}".format(line["l1PhysIf"]["attributes"]["dn"]
                                             , line["l1PhysIf"]["attributes"]["descr"]
                                             , line["l1PhysIf"]["attributes"]["speed"],
                                             line["l1PhysIf"]["attributes"]["mtu"]))
