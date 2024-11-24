def count_odd_books(book_ids):
    """
    Counts the number of books with odd ID numbers in the given queue.
    
    Parameters:
        book_ids (list): A list of integers representing book ID numbers.
        
    Returns:
        int: The total number of books with odd ID numbers.
    """
    # Use a list comprehension to filter odd IDs and count them.
    return sum(1 for book_id in book_ids if book_id % 2 != 0)

# Example usage
books_queue = [101, 202, 303, 404, 505]
odd_books_count = count_odd_books(books_queue)
print(odd_books_count)  # Output: 3

# Explicação:
# Entrada: A função aceita uma lista de números inteiros (`book_ids`), representando a fila de números de ID dos livros.
# Filtrando IDs Ímpares: A condição `book_id % 2 != 0` verifica se um ID é ímpar.
# Contagem: A função `sum()` itera sobre os IDs filtrados e conta quantos satisfazem a condição.
# Saída: Retorna o total de livros com IDs ímpares.
