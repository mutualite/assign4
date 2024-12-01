import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.book_titles=book_titles
        self.texts = []
        for element in texts:
            self.texts.append(element)
        #print(texts)
        def merge_sort_strings(arr):
            if len(arr) <= 1:
                return arr
        
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
        
            left_sorted = merge_sort_strings(left_half)
            right_sorted = merge_sort_strings(right_half)
        
            return merge_strings(left_sorted, right_sorted)
        
        def merge_strings(left, right):
            result = []
            i = j = 0
        
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                elif left[i]==right[j]:
                    if result==[] or result[-1]!=left[i]:
                        result.append(left[i])
                        i+=1
                        j+=1
                else:
                    result.append(right[j])
                    j += 1
        
            while i < len(left):
                result.append(left[i])
                i += 1
        
            while j < len(right):
                result.append(right[j])
                j += 1
        
            return result
        #print(self.texts)   
        for i in range(len(self.texts)):
            self.texts[i]=merge_sort_strings(self.texts[i])
        self.book_titles1=[]
        count=0
        #self.book_titles=self.booktitles
        for title in self.book_titles:
            self.book_titles1.append((self.book_titles[count],count))
            count+=1
        self.book_titles1=merge_sort_strings(self.book_titles1)
        '''self.texts=[[]*len(self.texts)]
        for k in range(len(self.texts)):'''
            
        #print(self.texts)    
            
        pass
    
    def distinct_words(self, book_title):
        distword=[]
        def binary_search_string(arr, target):
            low, high = 0, len(arr) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1
        book=self.book_titles1[binary_search_string(self.book_titles1,book_title)][-1]
        #print(self.book_titles[book])
        #break
        for word in range(len(self.texts[book])):
            if self.texts[book][word]!=self.texts[book][word-1]:
                #print(self.texts)
                distword.append(self.texts[book][word])
        #print(distword)
        return distword
        pass
    
    def count_distinct_words(self, book_title):
        def binary_search_string(arr, target):
            low, high = 0, len(arr) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1
        book=self.book_titles1[binary_search_string(self.book_titles1,book_title)][-1]
        return len(self.texts[book])
        pass
    
    def search_keyword(self, keyword):
        def binary_search_string(arr, target):
            low, high = 0, len(arr) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1
        l=[]
        for k in range(len(self.book_titles)):
            #print(k,keyword)
            ind=binary_search_string(self.texts[self.book_titles1[k][1]],keyword)
            if ind!=-1:
                l.append(self.book_titles1[k][0])
        #print(l)
        return l
            
            
        pass
    
    def print_books(self):
        for k in range(len(self.book_titles)):
            str1=str(self.book_titles1[k][0]+': ')
            for t in self.texts[self.book_titles1[k][1]]:
                str1+=t+' | '
            str1=str1[:-3]
            print(str1)
    
        pass

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name=name
        self.params=params
        if name=='Jobs':
            #self.hashset=ht.HashSet('Chain',params)
            self.hashmap=ht.HashMap('Chain',params)
        if name=='Gates':
            #self.hashset=ht.HashSet('Linear',params)
            self.hashmap=ht.HashMap('Linear',params)
        if name=='Bezos':
            #self.hashset=ht.HashSet('Double',params)
            self.hashmap=ht.HashMap('Double',params)
        self.book_titles_list=[]
        pass
    
    def add_book(self, book_title, text):
        if self.name=='Jobs':
            self.hashset=ht.HashSet('Chain',self.params)
        if self.name=='Gates':
            self.hashset=ht.HashSet('Linear',self.params)
        if self.name=='Bezos':
            self.hashset=ht.HashSet('Double',self.params)
        for word in text:
            self.hashset.insert(word)
            #if self.name=='Jobs':
                #print(text)
        self.hashmap.insert(book_title,self.hashset)
        #if self.name=='Bezos':
            #print(self.hashset.table)
        self.book_titles_list.append(book_title)
        pass
    
    def distinct_words(self, book_title):
        #print(self.hashmap.table,)
        text=self.hashmap.find(book_title).table
        l=[]
        if self.name=='Jobs':
            for key in text:
                #print(key)
                l+=key

        if self.name=='Gates':
            visit=[]
            for key in text:
                if key==None:
                    visit=[]
                elif key not in visit:
                    visit.append(key)
                    l.append(key)
        if self.name=='Bezos':
            for key in text:
                if key!=None:
                    l.append(key)
        return l
        pass
    
    def count_distinct_words(self, book_title):
        return self.hashmap.find(book_title).load
        pass
    
    def search_keyword(self, keyword):
        #l=[]
        #print(self.hashmap.table)
        books_found_in = []
        for book_title in self.book_titles_list:
            curr_text_hashset = self.hashmap.find(book_title)
            if curr_text_hashset.find(keyword):
                books_found_in.append(book_title)
        return books_found_in
        '''for oo in self.hashmap.table:
            if self.name=='Jobs':
                if oo!=[]:
                    for t in oo:
                        k=t[1].find(keyword)
                        if k!=False:
                            l.append(t[0])
            if self.name=='Gates':
                if oo!=None:
                    k=oo[1].find(keyword)
                    if k!=False:
                        l.append(oo[0])
            if self.name=='Bezos':
                if oo!=None:
                    k=oo[1].find(keyword)
                    if k!=False:
                        l.append(oo[0])
        return l'''
        pass
    
    def print_books(self):
        for book_title in self.book_titles_list:
            k = self.hashmap.find(book_title)
            print(str(book_title+': '+k.__str__()))
        '''for book in self.hashmap.table:
            if self.name=='Jobs':
                #string1=''
                if book==[]:
                    #print('<EMPTY>')
                    pass
                else:
                    for k in book:
                        string1=str(k[0]+': '+k[1].__str__())'''
        '''for t in k[1].table:
                            if t==[]:
                                string1+='<EMPTY>'+' | '
                            else:
                                #print(t)
                                count=0
                                for word in t:
                                    if len(t)<=1:
                                        string1+=word
                                    else:
                                        string1+=word+' ; '
                                if len(t)>1:
                                    string1=string1[:-2]
                                string1+=' | '''
        '''print(string1)
            else:
                if book!=None:
                    string1=str(book[0]+': '+book[1].__str__())'''
        '''for t in book[1].table:
                        if t!=None:
                            string1+=t+' | '
                        else:
                            string1+='<EMPTY>'''
        '''print(string1)'''
        pass
