class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        self.load=0
        if collision_type == 'Chain':
            self.z = params[0]
            self.table_size = params[1]
            self.table = [[] for _ in range(self.table_size)]  # list of lists for chaining

        elif collision_type == 'Linear':
            self.z = params[0]
            self.table_size = params[1]
            self.table = [None] * self.table_size  # None for empty slots

        elif collision_type == 'Double':
            self.z1 = params[0]
            self.z2 = params[1]
            self.c2 = params[2]
            self.table_size = params[3]
            self.table = [None] * self.table_size  # None for empty slots

    def polyhashfunc(self, key):
        def char_value(c):
            if 'a' <= c <= 'z':
                return ord(c) - ord('a')
            elif 'A' <= c <= 'Z':
                return ord(c) - ord('A') + 26
            else:
                return 0  # Use 0 for non-alphabet characters

        hash_value = 0
        for i, char in enumerate(key):
            hash_value += char_value(char) * (self.z ** i if self.collision_type in ['Chain', 'Linear'] else self.z1 ** i)

        return hash_value % self.table_size

    
    '''def polyhashfunc(self, key):
        def char_value(c):
            if 'a' <= c <= 'z':  # For lowercase letters
                return ord(c) - ord('a')
            elif 'A' <= c <= 'Z':  # For uppercase letters
                return ord(c) - ord('A') + 26
            else:
                return float(c)
                #raise ValueError("String contains non-alphabet characters")
    
        # Compute polynomial hash value
        hash_value = 0
        if self.collision_type == 'Chain' or self.collision_type == 'Linear':
            for i in range(len(list(key))):
                #print(list(key)[i],key)
                hash_value += char_value(list(key)[i]) * (self.z ** i)
        else:
            for i in range(len(list(key))):
                #print(list(key)[i])
                hash_value += char_value(list(key)[i]) * (self.z1 ** i)
        
        return hash_value%self.table_size'''
    
    def doublepolyhashfunc(self, key):
        def char_value(c):
            if 'a' <= c <= 'z':  # For lowercase letters
                return ord(c) - ord('a')
            elif 'A' <= c <= 'Z':  # For uppercase letters
                return ord(c) - ord('A') + 26
            else:
                return 0
                #raise ValueError("String contains non-alphabet characters")
    
        # Compute polynomial hash value
        hash_value = 0
        #print(key)
        for i in range(len(list(key))):
                #print(list(key)[i])
                hash_value += char_value(list(key)[i]) * (self.z2 ** i)
        # Compress to get slot number
        slot_number = hash_value % self.c2

        return self.c2-slot_number

    def insert(self, x):
        key = self.polyhashfunc(x)
        if self.collision_type == 'Chain':
            if x not in self.table[key]:
                if self.table[key]==[]:
                    self.table[key]=[x]
                else:
                    #print(self.table[key])
                    self.table[key].append(x)
                #print(self.table[key])
                self.load+=1

        elif self.collision_type == 'Linear':
            index = key
            for _ in range(self.table_size):
                if self.table[index] == None:
                    self.table[index] = x
                    self.load+=1
                    return
                elif self.table[index]==x:
                    return
                index = (index + 1) % self.table_size
            #self.Dynamic

        elif self.collision_type == 'Double':
            index = key
            step_size = self.doublepolyhashfunc(x)
            flag=0
            while flag==0:
                if self.table[index]==None:
                    self.table[index] = x
                    #print('in None',x)
                    #print(index,x)
                    self.load+=1
                    return
                elif x in self.table:
                    #print('already there',x, self.table[index])
                    return
                index = (index + step_size) % self.table_size
                if index==key:
                    flag=1
                    return
            #print(self.table)
            #print(key, step_size, x, self.table)

    def find(self, key):
        hashed_key = self.polyhashfunc(key)
        if self.collision_type == 'Chain':
            for item in self.table[hashed_key]:
                if item == key:
                    return True
            return False

        elif self.collision_type == 'Linear':
            index = hashed_key
            for _ in range(self.table_size):
                if self.table[index]==None:
                    return False
                if self.table[index] == key:
                    return True
                index = (index + 1) % self.table_size
            return False

        elif self.collision_type == 'Double':
            index = hashed_key
            step_size = self.doublepolyhashfunc(key)
            for _ in range(self.table_size):
                if self.table[index] ==None:
                    return False
                if self.table[index] == key:
                    return True
                index = (index + step_size) % self.table_size
            return False

    def get_slot(self, key):
        hashed_key = self.polyhashfunc(key)
        return hashed_key

    def get_load(self):
        #filled_slots = sum([1 for slot in self.table if slot is not None])
        return self.load / self.table_size

    def __str__(self):
        str1=[]
        for i in self.table:
            if i==None or not i:
                str1.append('<EMPTY>')
            elif self.collision_type=='Chain':
                str1.append(' ; '.join( str(x) for x in i))
            else:
                str1.append(i)
        return ' | '.join(str1)
        #for k in self.hashmap
        #return str(self.table)

    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        # Placeholder for rehashing function for dynamic hash table expansion
        pass

# HashSet class where only the key is stored
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, key):
        if not self.find(key):
            #print(self.table)
            super().insert(key)

    def find(self, key):
        return super().find(key)

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):
        return super().__str__()

# HashMap class where (key, value) pairs are stored
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, x, value):
        key = self.polyhashfunc(x)
        if self.collision_type == 'Chain':
            if (x,value) not in self.table[key]:
                if self.table[key]==[]:
                    self.table[key]=[(x,value)]
                else:
                    self.table[key].append((x,value))
                self.load+=1

        elif self.collision_type == 'Linear':
            index = key
            for _ in range(self.table_size):
                if self.table[index]==None:
                    self.table[index] = (x,value)
                    self.load+=1
                    return
                elif self.table[index]==(x,value):
                    return 
                index = (index + 1) % self.table_size

        elif self.collision_type == 'Double':
            index = key
            step_size = self.doublepolyhashfunc(x)
            flag=0
            while flag==0:
                if self.table[index] ==None:
                    self.table[index] = (x,value)
                    self.load+=1
                    #print(index,step_size)
                    return
                elif self.table[index]==(x,value):
                    #print('imhere')
                    return
                index = (index + step_size) % self.table_size
                if index==key:
                    flag=1
            #print(key, step_size, self.table)
            
    def find(self, key):
        hashed_key = self.polyhashfunc(key)
        if self.collision_type == 'Chain':
            for k, v in self.table[hashed_key]:
                if k == key:
                    return v
            return None
        else:
            index = hashed_key
            if self.collision_type == 'Linear':
                for _ in range(self.table_size):
                    if self.table[index] ==None:
                        return None
                    if self.table[index][0] == key:
                        return self.table[index][1]
                    index = (index + 1) % self.table_size
            elif self.collision_type == 'Double':
                step_size = self.doublepolyhashfunc(key)
                #print('index',index)
                #print(self.doublepolyhashfunc('book2'))
                for _ in range(self.table_size):
                    if self.table[index]==None:
                        #print(self.table,index)
                        return None
                    if self.table[index][0] == key:
                        return self.table[index][1]
                    index = (index + step_size) % self.table_size
            return None

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):#on of HashMap
        if self.collision_type == "Chain":
            # Chaining HashMap: elements within one chain separated by ";", different chains separated by "|"
            return " | ".join(
                    [f"{' ; '.join(f'({x[0]}, {x[1]})' for x in bucket)}" if bucket else "<EMPTY>" for bucket in self.table])
        elif self.collision_type in {"Linear", "Double"}:
            # Probing HashMap: elements separated by "|"
            return " | ".join(
                [f"({slot[0]}, {slot[1]})" if slot else "<EMPTY>" for slot in self.table])
