from pyxample import controller


#Inserts a new key with a value
#Input:
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


#Returns the value of a key
#Input:
#       key : string
def get(key):
    return controller.send_request("GET", key).decode("utf-8")


#Deletes a key
#Input:
#       key : string
def delete(key):
    controller.send_request("DELETE", key)


#Increments a key with numeric value
#Input:
#       key : string
def increment(key):
    header = {'op' : 'INCR'}
    controller.send_request("PUT", key, header)


#Decrements a key with numeric value
#Input:
#       key : string
def decrement(key):
    header = {'op' : 'DECR'}
    controller.send_request("PUT", key, header)
