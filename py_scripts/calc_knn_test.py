import os
cwd = os.getcwd()
os.chdir('../')
import py_scripts.calc_knn as calc_knn

def calc_knn_test(percent = 20, k = 5, list_dados = []):   
    
    from random import sample
    
    list_dados_copy = list_dados.copy()
    list_test = []
    list_test_noclass = []
    a = 0
    
    rand_sample = sample(range(len(list_dados_copy)), int(len(list_dados_copy)*(percent/100)))
    sorted_sample = sorted(rand_sample, reverse = True)
    
    for i in sorted_sample:
        list_test.append(list_dados_copy.pop(i))

    for valor in list_test:        
        list_test_noclass.append([valor[0], '', valor[2]])

    list_test_class = calc_knn.calc_knn(5, list_test_noclass, list_dados_copy)

    for i in range(len(list_test_class)):
        if list_test[i] == list_test_class[i]:
            a += 1

    total = (a/len(list_test_class))*100

    print(f'A função desempenhou {total}% de exatidão')
    
    return list_test, list_test_class