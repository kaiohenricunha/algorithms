from collections import deque

class ServiceQueue:
    def __init__(self):
        # Initialize an empty deque to manage the customer queue.
        self.queue = deque()

    def add_customer(self, name):
        """
        Adds a customer to the end of the line.
        
        Parameters:
            name (str): The name of the customer.
        """
        self.queue.append(name)
        print(f"Customer {name} added to the queue.")

    def serve_customer(self):
        """
        Removes the customer from the front of the line and displays their name.
        
        Returns:
            str: The name of the customer being served, or a message if the queue is empty.
        """
        if self.queue:
            customer = self.queue.popleft()
            print(f"Serving customer: {customer}")
            return customer
        else:
            print("No customers to serve.")
            return "No customers to serve."

    def queue_length(self):
        """
        Returns the number of customers remaining in the line.
        
        Returns:
            int: The number of customers in the queue.
        """
        length = len(self.queue)
        print(f"Number of customers in the queue: {length}")
        return length

# Example usage
service_queue = ServiceQueue()

service_queue.add_customer("Alice")
service_queue.add_customer("Bob")
service_queue.queue_length()  # Output: Number of customers in the queue: 2

service_queue.serve_customer()  # Output: Serving customer: Alice
service_queue.queue_length()  # Output: Number of customers in the queue: 1

service_queue.serve_customer()  # Output: Serving customer: Bob
service_queue.serve_customer()  # Output: No customers to serve.

# Explicação:
# __init__: Inicializa uma fila vazia usando `deque` do módulo `collections` para operações eficientes de adição e remoção.
# add_customer(name): Adiciona o nome do cliente ao final da fila e imprime uma mensagem de confirmação.
# serve_customer():
# - Se a fila não estiver vazia, remove e retorna o cliente no início da fila.
# - Se a fila estiver vazia, retorna uma mensagem indicando que não há clientes para atender.
# queue_length(): Retorna e imprime o número de clientes atualmente na fila.
