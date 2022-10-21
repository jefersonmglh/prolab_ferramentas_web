def volume():
    massamolar, densidade, pureza = acido_variaveis()
    volume_final = volume_solucao()
    concentracao = concentracao_solucao()
    calculo_acido(massamolar, concentracao, volume_final, pureza, densidade)


def acido_variaveis():
    acido = selecionar_acido()
    if acido == 1:
        massamolar = 98.079
        densidade = 1.83
        pureza = 98
        print('Você selecionou o Ácido Sulfúrico.\n')
        return massamolar, densidade, pureza
    elif acido == 2:
        massamolar = 36.458
        densidade = 1.18
        pureza = 37
        print('Você selecionou o Ácido Clorídrico.\n')
        return massamolar, densidade, pureza
    elif acido == 3:
        massamolar = 63.01
        densidade = 1.51
        pureza = 65
        print('Você selecionou o Ácido Nítrico.\n')
        return massamolar, densidade, pureza


def selecionar_acido():
    acido = int(input('\nDigite o número correspondente ao ácido utilizado no preparo da solução:'
                '\n1 - Ácido Sulfúrico. \n2 - Ácido Clorídrico. \n3 - Ácido Nítrico.\n'))
    return acido


def volume_solucao():
    volume_final = float(input('Qual o volume desejado da solução final (em Litros)? '))
    return volume_final


def concentracao_solucao():
    concentracao = float(input('Qual é a concentração dessa solução (em mol/L)? '))
    return concentracao


def calculo_acido(massamolar, concentracao, volume_final, pureza, densidade):
    v = ((100 * massamolar * concentracao * volume_final) / (pureza * densidade))
    print(f'Para fazer {volume_final} litros da solução, você precisará de %.2f' % v + 'mL do ácido desejado')


if __name__ == '__main__':
    volume()
