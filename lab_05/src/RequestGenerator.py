from Distributions import Distribution

class RequestGenerator:
    
    def __init__(self, distribution: Distribution) -> None:
        self.remaining_time = 0
        self.generated_time = 0
        self.distribution = distribution
    
    
    def can_generate(self) -> bool:
        return False if self.remaining_time > 0 else True
    
    def can_not_generate(self) -> bool:
        return not self.can_generate()
    
    
    def is_new_request(self) -> bool:
        return self.remaining_time == self.generated_time
    
    def is_not_new_request(self) -> bool:
        return not self.is_new_request()
    
    
    def update_generating_time(self, delta_t: float = 0.01) -> None:
        self.remaining_time -= delta_t
        if self.can_generate():
            self.generated_time = self.distribution.get_value()
            self.remaining_time = self.generated_time