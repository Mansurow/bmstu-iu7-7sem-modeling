from RequestQueue import RequestQueue

class RequestProcessor:
    
    def __init__(self, processing_time: int) -> None:
        self.remaining_time = 0
        self.processing_time = processing_time
        
        
    def is_busy(self) -> bool:
        return True if self.remaining_time > 0 else False
    
    def is_not_busy(self) -> bool:
        return not self.is_busy()
    
    
    def is_new_request(self) -> bool:
        return self.remaining_time == self.processing_time
    
    def is_not_new_request(self) -> bool:
        return not self.is_new_request()
        
        
    def update_processing_time(self, queue: RequestQueue, delta_t: float = 0.01) -> None:
        self.remaining_time -= delta_t
        if self.is_not_busy() and queue.is_not_empty():
            queue.remove_request()
            self.remaining_time = self.processing_time
            