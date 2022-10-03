from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_map = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.value_map:
            self.value_map.move_to_end(key)
            return self.value_map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.value_map:
            self.value_map.move_to_end(key)

        self.value_map[key] = value

        if self.capacity < len(self.value_map.keys()):
            self.value_map.popitem(last=False)



# value_map = { key,  (value, order) }
# p_queue = [(key, order)]
# capacity: int
# putされたorderも保持する必要がある -> sorted map