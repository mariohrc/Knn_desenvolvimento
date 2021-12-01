def calc_dist(lista_noclass = [], lista_class = []):
    result = []
    result_matri = []
    for i in range(len(lista_noclass)):
        for j in range(len(lista_class)):
            x1, y1, z1, w1 = lista_noclass[i][2]
            x2, y2, z2, w2 = lista_class[j][2]
            dist = ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2+(w2-w1)**2)**0.5
            result.append([lista_class[j][1], dist])
        result_matri.append(result)
        result = []
    return result_matri
