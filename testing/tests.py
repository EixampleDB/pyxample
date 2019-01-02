import pyxample as pyx
pyx.connect("localhost", 5333)
pyx.set("test", "testval1")  # Insertamos string
print(pyx.get("test"))

pyx.set("testNum", 23)  # Insertamos numero
print(pyx.get("testNum"))
pyx.increment("testNum")  # Incrementamos el valor
print(pyx.get("testNum"))
pyx.decrement("testNum")  # Decrementamos el valor
print(pyx.get("testNum"))

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

id = pyx.bulk(operations)
print(id)
print(pyx.get("NUMERIC"))
print(pyx.get_bulk_op(id))
