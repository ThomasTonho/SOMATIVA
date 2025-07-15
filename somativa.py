minhas_compras = []

filmes = [
    "⚔️  Demon Slayer: Trem Infinito",
    "✨ Doutor Estranho no Multiverso da Loucura",
    "🚀 Guardiões da Galáxia",
    "⚡ Harry Potter e a Pedra Filosofal",
    "🕷️  Homem-Aranha: Através do Aranhaverso",
    "🕸️  Homem-Aranha: Sem Volta para Casa",
    "🌊 Luca",
    "👾 Monstros S.A.",
    "🦇 O Batman",
    "🐾 Pantera Negra",
    "🎵 Soul",
    "🏎️ Velozes e Furiosos 9",
    "🖤 Venom",
    "💎 Vingadores: Ultimato",
    "🕷️ Viúva Negra"
]

while True:
    print("------------------------------")
    print("🎬 1 - Mostrar catalogo de filmes")
    print("🎫 2 - Comprar ingressos")
    print("🛒 3 - Ver minhas compras")
    print("⭐ 4 - Dar Feedback do sistema")
    print("🚪 5 - Sair")
    print("------------------------------")
    opcao = input("👆 Escolha uma opção: (1, 2, 3, 4, 5): ")

    if opcao == "1":
        print("-------------------")
        print("🎬 Catalogo de Filmes:")
        print("-------------------")
        for i, filme in enumerate(filmes, 1):
            print(f"{i}. {filme}")

    elif opcao == "2":
        print("-------------------")
        print("🎫 Loja Ingressos:")
        print("-------------------")
        for i, filme in enumerate(filmes, 1):
            print("-------------------")
            print(f"{i}. {filme}")
        numero = input("Digite o número do filme que deseja comprar: ")
        if not numero.strip():
            print("-----------------")
            print("🚫 O campo não pode ser deixado em branco.")
            print("-----------------")
        elif not numero.isnumeric():
            print("-----------------")
            print("🔢 Só digite números")
            print("-----------------")
        else:
            numero_atualizado = int(numero)
            numeros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            if numero_atualizado in numeros_validos:
                minhas_compras.append(filmes[numero_atualizado - 1])
                print("----------------------------------------------------------------------")
                print(f"Ingresso para '{filmes[numero_atualizado - 1]}' comprado com sucesso!")
            else:
                print("-------------------------------------------")
                print("🚫 Filme ainda não disponivel no catálogo.")
                print("-------------------------------------------")

    elif opcao == "3":
        print("-------------")
        print("🛒 Suas Compras:")
        print("-------------")
        for i , filme in enumerate(minhas_compras, 1):
            print("----------------------")
            print(f"{i}. {minhas_compras}")

    elif opcao == "4":
        print("----------------------------------------")
        feedback = input("⭐ O que achou do nosso programa?: ")
        if not feedback.strip():
            print("-----------------")
            print("🚫 O campo não pode ser deixado em branco.")
            print("-----------------")
        else:
            print("💖 Obrigado por nos avaliar!")

    elif opcao == "5":
        print("---------")
        print("🚪 Saindo...")
        print("---------")
        break

    else:
        print("-------------------")
        print("❌ Opção inválida.")
        print("-------------------")

