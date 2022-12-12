def conversao(dados):
    convertido = []
    for i in dados:
        if i == 'Sempre':
            convertido.append(3)
        elif i == 'Quase Sempre':
            convertido.append(2)
        elif i == 'Raramente':
            convertido.append(1)
        elif i == 'Nunca':
            convertido.append(0)
        elif i == 'Masculino':
            convertido.append(0)
        elif i == 'Feminino':
            convertido.append(1)
    return convertido