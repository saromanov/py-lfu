
class LFUCache(object):
    '''LFUCache defines class for cache
    '''
    def __init__(self, capacity:int):
        self.cache = {}
        self.capacity = capacity
        self.freq_link_head = None
    
    def get(self, key):
        if key not in self.cache:
            return -1
        cache_node = self.cache[key]
        freq_node = cache_node.freq_node
        value = cache_node.value
        self.move_forward(cache_node, freq_node)
        return value

    def set(self, key, value):
        if self.capacity <= 0:
            return -1
        
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.dump_cache()
            self.create_cache(key, value)
        else:
            cache_node = self.cache[key]
            freq_node = cache_node.freq_node
            cache_node.value = value
            self.move_forward(cache_node, freq_node)