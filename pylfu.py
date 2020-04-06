
class LFUCache(object):
    '''LFUCache defines class for cache
    '''
    def __init__(self, capacity:int):
        self.cache = {}
        self.capacity = capacity
        self.freq_link_head = None
    
    def __getitem__(self, key):
        if key not in self.cache:
            return -1
        cache_node = self.cache[key]
        freq_node = cache_node.freq_node
        value = cache_node.value
        self.move_forward(cache_node, freq_node)
        return value
        
    def dump_cache(self):
        head_freq_node = self.freq_link_head
        self.cache.pop(head_freq_node.cache_head.key)
        head_freq_node.pop_head_cache()

        if head_freq_node.count_caches() == 0:
            self.freq_link_head = head_freq_node.nxt
            head_freq_node.remove()

    def __setitem__(self, key, value):
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

class CacheNode(object):
    def __init__(self, key, value, node, pre, nxt):
        self.node = node
        self.key = key
        self.value = value
        self.previous = previous
        self.nxt = nxt

    def free_myself(self):
        if self.node.cache_head == self.node.cache_tail:
            self.node.cache_head = self.node.cache_tail = None
        elif self.node.cache_head == self:
            self.nxt.previous = None
            self.node.cache_head = self.nxt
        elif self.node.cache_tail == self:
            self.previous.nxt = None
            self.node.cache_tail = self.previous
        else:
            self.previous.nxt = self.nxt
            self.nxt.previous = self.previous

        self.previous = None
        self.nxt = None
        self.node = None