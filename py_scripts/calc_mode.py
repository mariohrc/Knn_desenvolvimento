def calc_mode(lista = []):
    list_mode = []

    for valor in lista:
        a, b, c = [0,0,0]
        for i in range(len(valor)):
            if valor[i][0] == 'Conservador':
                a += 1
            elif valor[i][0] == 'Moderado':
                b += 1
            else:
                c += 1
        list_mode.append([[a, 'Conservador'],[b, 'Moderado'],[c, 'Agressivo']])

    return list_mode