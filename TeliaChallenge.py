lookupTable = {"NORTH":{"NORTH":0, "SOUTH":1, "EAST":0, "WEST":0},
               "SOUTH":{"NORTH":1, "SOUTH":0, "EAST":0, "WEST":0},
               "EAST":{"NORTH":0, "SOUTH":0, "EAST":0, "WEST":1},
               "WEST":{"NORTH":0, "SOUTH":0, "EAST":1, "WEST":0}}

def dirReduc(arr):
    if len(arr) > 0:
        for i in range(len(arr) - 1):
            if lookupTable[arr[i]][arr[i + 1]]:
                del arr[i:i+2]
                dirReduc(arr)
                return arr
    return arr