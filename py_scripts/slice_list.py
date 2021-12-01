def slice_list(k = 5, lista = []):
    sliced_list = []
    for valor in lista:
        sliced_list.append(valor[:k])
    return sliced_list