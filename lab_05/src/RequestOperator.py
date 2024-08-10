from RequestQueue import RequestQueue
from Distributions import Distribution

class RequestOperator:
    
    def __init__(self, distribution: Distribution) -> None:
        self.remaining_time = 0
        self.have_request = False
        self.distribution = distribution
        
        
    def is_busy(self) -> bool:
        return True if self.remaining_time > 0 else False
    
    def is_not_busy(self) -> bool:
        return not self.is_busy()
    
    
    def update_operating_time(self, queue: RequestQueue, delta_t: float = 0.01) -> None:
        self.remaining_time -= delta_t
        if self.is_not_busy() and self.have_request:
            queue.add_request()
            self.have_request = False
            
            
    def start_operating_request(self):
        self.have_request = True
        self.remaining_time = self.distribution.get_value()