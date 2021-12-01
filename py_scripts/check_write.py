import os
cwd = os.getcwd()
os.chdir('../')
import py_scripts.organize_list as organize_list

def check_write(list_mode = [], sliced_list = [], organized_list = [], list_no_class = []):
    
    organized_list_moda = organize_list.organize_list(list_mode, reverse = False)
    list_result = []
    lista_total = []
    for valor in list_mode:
        lista_part = []
        for i in range(len(valor)):
            lista_part.append(valor[i][0])
        lista_total.append(lista_part)

    for i, valor2 in enumerate(lista_total):
        if valor2.count(max(valor2)) > 1:
            list_result.append([list_no_class[i][0],sliced_list[i][0][0], list_no_class[i][2]])
        else:
            list_result.append([list_no_class[i][0],organized_list_moda[i][2][1], list_no_class[i][2]])
            
    return list_result