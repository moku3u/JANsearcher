# JANsearcher / barcode search

## How to use

example.py
```py
import JAN

r = JAN.search("4902102083188")

print(r["product"]["name"])
print(r["product"]["company"])
print(r["status_code"])
```

output
```
ファンタワールドニューヨークアップル
日本コカ・コーラ
200
```
