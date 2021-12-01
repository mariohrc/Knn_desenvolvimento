def organize_list(lista = [], reverse = True):
    if reverse == True:
            sorted_list_part = []
            sorted_list = []
            for valor in lista:
                sorted_list_part = sorted(valor, key=lambda x: x[1])
                sorted_list.append(sorted_list_part)
            return sorted_list
        
    elif reverse == False:
            sorted_list_part = []
            sorted_list = []
            for valor in lista:
                sorted_list_part = sorted(valor, key=lambda x: x[0])
                sorted_list.append(sorted_list_part)
            return sorted_list