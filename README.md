# Pyxample
Pyxample it's a library that lets you use EixampleDB in Python 3.5 and above  
  
## API

```python
connect(ip='localhost', port=5333)
```
Specifies the host and the port where EixampleDB is running  
  
**Parameters:**  
- **ip** - string with the IP of the DB
- **port** - int whit the port of the DB  
  
---
  
```python
set(key, value, keyType='DEF')
```
Inserts a new key with a value  
  
**Parameters:**  
- **key** - string that will be the key
- **value** - string or numeric that will be the value  
- **keyType** - string that specifies how that key is treated  
  - *DEF*: As a default key  
  - *STARTS*: As a prefix  
  - *REGEX*: As a Regular Expression, following this [specification](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)  
    
**Returns:** A [`Response`](#response) object  

---

```python
get(key, keyType='DEF')
```
Returns the value of a key in the body of a [`Response`](#response) object  
  
**Parameters:**  
- **key** - string with the key
- **keyType** - string that specifies how that key is treated  
  - *DEF*: As a default key  
  - *STARTS*: As a prefix  
  - *REGEX*: As a Regular Expression, following this [specification](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)  
    
**Returns:** A [`Response`](#response) object  
  
---
  
```python
delete(key, keyType='DEF')
```
Deletes a key
  
**Parameters:**  
- **key** - string with the key
- **keyType** - string that specifies how that key is treated  
  - *DEF*: As a default key  
  - *STARTS*: As a prefix  
  - *REGEX*: As a Regular Expression, following this [specification](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)  
    
**Returns:** A [`Response`](#response) object  

---

```python
increment(key, keyType='DEF')
```
Increments by one the value of a given key if it is a numeric one  
  
**Parameters:**  
- **key** - string with the key
- **keyType** - string that specifies how that key is treated  
  - *DEF*: As a default key  
  - *STARTS*: As a prefix  
  - *REGEX*: As a Regular Expression, following this [specification](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)  
    
**Returns:** A [`Response`](#response) object  
  
---
  
```python
decrement(key, keyType='DEF')
```
Decrements by one the value of a given key if it is a numeric one  
  
**Parameters:**  
- **key** - string with the key
- **keyType** - string that specifies how that key is treated  
  - *DEF*: As a default key  
  - *STARTS*: As a prefix  
  - *REGEX*: As a Regular Expression, following this [specification](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)  
    
**Returns:** A [`Response`](#response) object  

---
  
```python
bulk(operations)
```
Realizes N operations by a given list
  
**Parameters:**  
- **operations** - list of dicts with form:
```python  
{  
  'key': <string>,  
  'type':'SET' | 'INCR' | 'DECR',  
  'value': <string>,  
  'parameters':['NUM' | 'STR']  
}  
```
    
**Returns:** A [`Response`](#response) object with the id of the operation  
  
---
  
```python
get_bulk_op(id)
```
Gets the operations made by the bulk operation
  
**Parameters:**  
- **id** - numeric id of the bulk operation
    
**Returns:** A [`Response`](#response)

### Response
Object with the following attributes:
- **header**: String with the headers of the DB response
- **body**: String with the body of the DB response
- **code**: Integer with the code of the DB reponse
