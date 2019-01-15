from pyxample import controller

keyTypes = ['DEF', 'STARTS', 'REGEX']

# Changes the ip of the DB if necessary
# Input:
#       ip : string
#       port : int
def connect(ip="localhost", port=5333):
    controller.connect(ip, port)


# Inserts a new key with a value
# Input:
#       key : string
#       value : string or numeric so far
def set(key, value, keyType='DEF'):
    header = {}
    if isinstance(value, int) or isinstance(value, float):
        header['type'] = 'NUM'
    elif isinstance(value, str):
        header['type'] = "STR"
    else:
        header['type'] = "STR"
    if keyType in keyTypes:
        header['search'] = keyType
    return controller.send_request("POST", key, header, str(value))


# Returns the value of a key
# Input:
#       key : string
def get(key, keyType='DEF'):
    header = {}
    if keyType in keyTypes:
        header['search'] = keyType
    return controller.send_request("GET", key)


# Deletes a key
# Input:
#       key : string
def delete(key, keyType='DEF'):
    header = {}
    if keyType in keyTypes:
        header['search'] = keyType
    return controller.send_request("DELETE", key)


# Increments a key with numeric value
# Input:
#       key : string
def increment(key, keyType='DEF'):
    header = {}
    header['op'] = 'INCR'
    if keyType in keyTypes:
        header['search'] = keyType
    return controller.send_request("PUT", key, header)


# Decrements a key with numeric value
# Input:
#       key : string
def decrement(key, keyType='DEF'):
    header = {}
    header['op'] = 'DECR'
    if keyType in keyTypes:
        header['search'] = keyType
    return controller.send_request("PUT", key, header)


# Returns id of a bulk operation
# Input:
#       operations : list of dicts with form:
#           {
# 			    "key":"NUMERIC",
# 			    "type":"SET",
# 			    "value":"1",
# 			    "parameters":["NUM"]
# 		    }
# "key": name of the key
# "type": operation
# "value": value
# "parameters": list of parameters
#  -- "NUM": key with numerical value
#  -- "STR": key with string value
#
def bulk(operations):
    return controller.send_bulk_request(operations)


# Returns the description of a bulk operation (all the steps) by a given id
# Input:
#       id : string
def get_bulk_op(id):
    return controller.send_request("GET", "bulk/" + id)
