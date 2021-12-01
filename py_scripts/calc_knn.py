import os
cwd = os.getcwd()
os.chdir('../')
import py_scripts.calc_dist as calc_dist
import py_scripts.organize_list as organize_list
import py_scripts.slice_list as slice_list
import py_scripts.calc_mode as calc_mode
import py_scripts.check_write as check_write

def calc_knn(k = 5, list_no_class = [], list_class = []):
    '''calc_knn(constate, lista não classificada, lista de dados)
    k = constante k para cálculo de KNN
    list_no_class = lista com dados não classificados
    list_class = lista de dados utilizados para classificação
    '''
    list_dist = calc_dist.calc_dist(list_no_class, list_class)
    organized_list = organize_list.organize_list(list_dist)
    sliced_list = slice_list.slice_list(k , organized_list)
    list_mode = calc_mode.calc_mode(sliced_list)
    classified_list = check_write.check_write(list_mode, sliced_list, organized_list, list_no_class)
    return classified_list