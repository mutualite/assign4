from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_table_size = get_next_size()
        old_table = self.table  # Store old table data
        self.table_size = new_table_size  # Update table size
        self.table = [[] if self.collision_type == 'Chain' else None for _ in range(new_table_size)]
        self.load = 0  # Reset load count

        # Rehash elements from old table into new table
        for slot in old_table:
            if self.collision_type == 'Chain':
                for key in slot:  # slot is a list for chaining
                    self.insert(key)
            else:  # Linear Probing or Double Hashing
                if slot is not None:
                    self.insert(slot)
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_table_size = get_next_size()
        old_table = self.table  # Store old table data
        self.table_size = new_table_size  # Update table size
        self.table = [[] if self.collision_type == 'Chain' else None for _ in range(new_table_size)]
        self.load = 0  # Reset load count

        # Rehash elements from old table into new table
        for slot in old_table:
            if self.collision_type == 'Chain':
                for key, value in slot:  # slot is a list of (key, value) pairs for chaining
                    self.insert(key, value)
            else:  # Linear Probing or Double Hashing
                if slot is not None:
                    self.insert(slot[0], slot[1])
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()