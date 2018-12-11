from pyxample import controller


#Inserts a new key with a value
#Input:
#       key : string
#       value : string or numeric so far
def set(key, value):
    headers = {}
    if isinstance(value, str):
        headers['type'] = "STR"
    else:
        headers['type'] = "NUM"

    controller.send_request("POST", key, headers, str(value))


#Returns the value of a key
#Input:
#       key : string
def get(key):
    pass


#Deletes a key
#Input:
#       key : string
def delete(key):
    pass


#Increments a key with numeric value
#Input:
#       key : string
def increment(key):
    pass


#Decrements a key with numeric value
#Input:
#       key : string
def decrement(key):
    pass
