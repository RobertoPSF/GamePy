from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade=dificuldade)

    print('Informe o resultado para seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo ? (1 - Sim ou 0 - Não): '))

    if continuar:
        jogar(pontos=pontos)
    else:
        print(f'Você terminou com {pontos} ponto(s). Até a próxima!')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
