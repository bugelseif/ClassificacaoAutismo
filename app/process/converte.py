def conversao(dados):
    # convertido = []
    convertido = ''

    for i in dados:
        if i == 'Sempre':
            convertido += '3'
            # convertido.append('3')
        elif i == 'Quase Sempre':
            # convertido.append('2')
            convertido += '2'
        elif i == 'Raramente':
            # convertido.append('1')
            convertido += '1'
        elif i == 'Nunca':
            # convertido.append('0')
            convertido += '0'
        elif i == 'Masculino':
            # convertido.append('0')
            convertido += '0'
        elif i == 'Feminino':
            # convertido.append('1')
            convertido += '1'

    return convertido