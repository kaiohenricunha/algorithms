# 3. Quantos passos seriam necessários
# para realizar uma busca linear pelo número 8 no array ordenado, [2, 4, 6, 8, 10, 12, 13]?

# **Resposta:**

# Seriam necessários **4 passos** para realizar uma busca linear pelo número **8** no array ordenado `[2, 4, 6, 8, 10, 12, 13]`.

# ---

# ### **Explicação**

# A **busca linear** é um algoritmo simples que verifica cada elemento de uma lista 
# sequencialmente até encontrar o elemento desejado ou até o final da lista. 
# O número de passos depende da posição do elemento alvo no array:

# - **Melhor Caso:** O alvo é o primeiro elemento (1 passo).
# - **Pior Caso:** O alvo é o último elemento ou não está presente (n passos, onde n é o número de elementos).

# ---

# ### **Detalhamento Passo a Passo**

# Vamos analisar cada elemento do array e contar os passos:

# 1. **Passo 1:**
#    - **Índice 0:** Valor = **2**
#    - **Comparação:** 2 é igual a 8?
#    - **Resultado:** Não.

# 2. **Passo 2:**
#    - **Índice 1:** Valor = **4**
#    - **Comparação:** 4 é igual a 8?
#    - **Resultado:** Não.

# 3. **Passo 3:**
#    - **Índice 2:** Valor = **6**
#    - **Comparação:** 6 é igual a 8?
#    - **Resultado:** Não.

# 4. **Passo 4:**
#    - **Índice 3:** Valor = **8**
#    - **Comparação:** 8 é igual a 8?
#    - **Resultado:** Sim.
#    - **Conclusão:** Alvo encontrado.

# ---

# ### **Resumo**

# - **Total de Passos:** **4**
# - **Posição do Alvo:** O número 8 está na **4ª posição** (índice 3, base zero) do array.
# - **Fim da Busca:** A busca termina assim que o alvo é encontrado.

# ---

# ### **Informações Adicionais**

# - **Características da Busca Linear:**
#   - **Arrays Ordenados ou Desordenados:** A busca linear não utiliza a ordenação dos dados; funciona da mesma forma para arrays ordenados ou desordenados.
#   - **Complexidade de Tempo:** O(n), onde n é o número de elementos do array.
#   - **Casos de Uso:** Simples e eficaz para conjuntos de dados pequenos ou arrays desordenados.

# - **Comparação com Busca Binária:**
#   - **Requisito da Busca Binária:** O array precisa estar ordenado.
#   - **Passos da Busca Binária para Este Caso:**
#     - **Passo 1:** O elemento do meio (índice 3, valor 8) é comparado com o alvo.
#     - **Resultado:** Encontrado em **1 passo**.
#   - **Vantagem:** A busca binária é mais eficiente para conjuntos de dados grandes e ordenados, com complexidade de tempo O(log n).

# ---

### **Ilustração em Python**

def busca_linear(arr, alvo):
    passos = 0
    for indice, valor in enumerate(arr):
        passos += 1
        if valor == alvo:
            print(f"Alvo {alvo} encontrado no índice {indice} após {passos} passos.")
            return indice
    print(f"Alvo {alvo} não encontrado após {passos} passos.")
    return -1

# Array e alvo fornecidos
array = [2, 4, 6, 8, 10, 12, 13]
numero_alvo = 8

# Executar busca linear
busca_linear(array, numero_alvo)
