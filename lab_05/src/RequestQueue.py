class RequestQueue:
    
    def __init__(self) -> None:
        self.size = 0
        
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_not_empty(self) -> bool:
        return not self.is_empty()
        
        
    def add_request(self) -> None:
        self.size += 1
        
    
    def remove_request(self) -> None:
        if self.is_not_empty():
            self.size -= 1
            
            
    def clear(self) -> None:
        self.size = 0