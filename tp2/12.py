class HashTable:
    def __init__(self, size):
        """
        Initialize the hash table with a given size.
        
        Parameters:
            size (int): The initial size of the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Compute the hash value for a given key.
        
        Parameters:
            key: The key to hash.
            
        Returns:
            int: The hash value (index) for the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Parameters:
            key: The key to insert.
            value: The value to associate with the key.
        """
        index = self._hash(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, add the new key-value pair
        self.table[index].append([key, value])

    def fetch(self, key):
        """
        Retrieve the value associated with a given key.
        
        Parameters:
            key: The key to retrieve the value for.
            
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        """
        Remove a key and its associated value from the hash table.
        
        Parameters:
            key: The key to remove.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False

# Example usage
hash_table = HashTable(10)

# Insert key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")

# Fetch values
print(hash_table.fetch("name"))  # Output: Alice
print(hash_table.fetch("age"))   # Output: 25

# Remove a key
hash_table.remove("age")
print(hash_table.fetch("age"))   # Output: None

# Handle collisions
hash_table.insert(1, "One")
hash_table.insert(11, "Eleven")  # Collision with key 1
print(hash_table.fetch(1))       # Output: One
print(hash_table.fetch(11))      # Output: Eleven

# Explicação:
# Função de Hash:

# O método `_hash` calcula o índice tomando o módulo da função `hash` do Python com o tamanho da tabela.
# Encadeamento Separado:

# Cada índice na tabela hash contém uma lista para armazenar múltiplos pares chave-valor em caso de colisões.
# Inserção:

# Se a chave já existir na cadeia, atualize seu valor.
# Caso contrário, adicione um novo par chave-valor à lista.
# Busca:

# Itere pela cadeia no índice calculado para encontrar a chave.
# Retorne o valor associado ou `None` se a chave não for encontrada.
# Remoção:

# Encontre e remova o par chave-valor da cadeia no índice calculado.
