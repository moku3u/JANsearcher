import JAN

r=JAN.search("4902102083188")

print(r["product"]["name"])
print(r["product"]["company"])
print(r["status_code"])