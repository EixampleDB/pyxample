from pyxample import controller


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
def set(key, value):
    header = {}
    if isinstance(value, int) or isinstance(value, float):
        header['type'] = 'NUM'
    elif isinstance(value, str):
        header['type'] = "STR"
    else:
        header['type'] = "STR"

    controller.send_request("POST", key, header, str(value))


# Returns the value of a key
# Input:
#       key : string
def get(key):
    return controller.send_request("GET", key).decode("utf-8")


# Deletes a key
# Input:
#       key : string
def delete(key):
    controller.send_request("DELETE", key)


# Increments a key with numeric value
# Input:
#       key : string
def increment(key):
    header = {'op': 'INCR'}
    controller.send_request("PUT", key, header)


# Decrements a key with numeric value
# Input:
#       key : string
def decrement(key):
    header = {'op': 'DECR'}
    controller.send_request("PUT", key, header)


# Returns id of a bulk operation
# Input:
#       operations : list of dicts with form:
#           {
# 			    "key":"NUMERIC",
# 			    "type":"SET",
# 			    "value":"1",
# 			    "parameters":["NUM"]
# 		    }
def bulk(operations):
    return controller.send_bulk_request(operations).decode("utf-8")


# Returns the description of a bulk operation (all the steps) by a given id
# Input:
#       id : string
def get_bulk_op(id):
    return controller.send_request("GET", "bulk/" + id).decode("utf-8")
