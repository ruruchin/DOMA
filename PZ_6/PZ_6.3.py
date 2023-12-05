def Index_Spiska(lsd):
    element = int(input())
    lsd = [int(input(f"Введите число{i+1}") for i in range(element))]
    K = int(input("Введите число сдвигов K: "))
    i = 0
    for i in range(K):
        first = lsd[i]
        second = lsd[i+1]
""""""
