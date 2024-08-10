from Distributions import Distribution

from RequestQueue import RequestQueue
from RequestOperator import RequestOperator
from RequestProcessor import RequestProcessor
from RequestGenerator import RequestGenerator

class InfoSystem:
    
    def __init__(self, request_amount: int = 300, delta_t: float = 0.01) -> None:
        self.delta_t = delta_t
        self.request_amount = request_amount
    
    
    @staticmethod
    def find_free_operator(operators: list[RequestOperator]) -> RequestOperator:
        return next((operator for operator in operators if operator.is_not_busy()), None)
    
         
    def simulate(self, generator_dist: Distribution, operators_dist: list[Distribution], processing_times: list[int]) -> None:
        generator = RequestGenerator(generator_dist)
        queues = [RequestQueue() for _ in range(len(processing_times))]
        operators = [RequestOperator(operator_dist) for operator_dist in operators_dist]
        computers = [RequestProcessor(processing_time) for processing_time in processing_times]
        
        modeling_time = 0
        rejected, processed = 0, 0
        while processed + rejected < self.request_amount:
            modeling_time += self.delta_t
           
            generator.update_generating_time(self.delta_t) 
            if generator.is_new_request():
                free_operator = self.find_free_operator(operators)
                if free_operator:
                    free_operator.start_operating_request()
                else:
                    rejected += 1
                
            for index, operator in enumerate(operators):
                queue = queues[0] if index < 2 else queues[1]
                operator.update_operating_time(queue, self.delta_t)
                
            for index, computer in enumerate(computers):
                computer.update_processing_time(queues[index], self.delta_t)
                if computer.is_new_request():
                    processed += 1
                
        return rejected / (processed + rejected)