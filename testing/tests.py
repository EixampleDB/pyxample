import pyxample as pyx
pyx.connect("localhost", 5333)

# 1.TEST SET/GET
print('TEST SET/GET')
response = pyx.set("test", "testval1")  # Insertamos string
print(response, '\n')
response = pyx.get("test")
print(response, '\n')

# 2.TEST NUMTYPE OPERATIONS
print('TEST NUMTYPE OPERATIONS')
pyx.set("testNum", 23)  # Insertamos numero
response = pyx.get("testNum")
print(response, '\n')

pyx.increment("testNum")  # Incrementamos el valor
response = pyx.get("testNum")
print(response, '\n')

pyx.decrement("testNum")  # Decrementamos el valor
response = pyx.get("testNum")
print(response, '\n')

#3. TEST PATHMATCHING

response = pyx.set("/aaabpath1", 0) # 0-1-0-1
response = pyx.set("/aaaapath11", 0) # 0-1-2-3
response = pyx.set("/bpath11", 3) # 3-4
response = pyx.set("/bpath12", 4)
response = pyx.set("/cpath21", 5) # 5-6
response = pyx.set("/cpath13", 6)
response = pyx.set("/cmatching12", 7)

#3.1 PREFIXES 'STARTS'
print('TEST STARTS')
print('set /aaa to 1 (1,1)')
pyx.set("/aaa", 1, 'STARTS')
response = pyx.get('/aaaapath11')
print(response, '\n')

print('decrement /aaab (0)')
pyx.decrement("/aaab", 'STARTS')
response = pyx.get('/aaabpath1')
print(response, '\n')

print('increment /aaaa (2)')
pyx.increment("/aaaa", 'STARTS')
response = pyx.get('/aaaapath11')
print(response, '\n')

#3.2 REGULAR EXPRESSIONS 'REGEX'

print('TEST /.*path.*1 REGEX (1,3,4,6)')
pyx.increment("/.*th.*1", 'REGEX')
response = pyx.get("/aaabpath1")
print(response, '\n')
response = pyx.get('/aaaapath11')
print(response, '\n')
response = pyx.get('/bpath11')
print(response, '\n')
response = pyx.get('/cpath21')
print(response, '\n')

# BULK
print('TEST BULK OPERATIONS')
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
