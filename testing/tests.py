import pyxample as pyx
pyx.connect("localhost", 5333)
response = pyx.set("test", "testval1")  # Insertamos string
print(response, '\n')
response = pyx.get("test")
print(response, '\n')

pyx.set("testNum", 23)  # Insertamos numero
response = pyx.get("testNum")
print(response, '\n')

pyx.increment("testNum")  # Incrementamos el valor
response = pyx.get("testNum")
print(response, '\n')

pyx.decrement("testNum")  # Decrementamos el valor
response = pyx.get("testNum")
print(response, '\n')

# BULK
operations = [
    {
        "key": "NUMERIC",
        "type": "SET",
        "value": "1",
        "parameters": ["NUM"]

    }
]
for i in range(100):
    operations.append({
        "key": "NUMERIC",
        "type": "INCR",
        "value": "1",
        "parameters": ["NUM"]

    })

id = pyx.bulk(operations).body
print('bulk id: ',id)
print('final value: ', pyx.get("NUMERIC").body)
print('body bulk operation: ',pyx.get_bulk_op(id).body)
