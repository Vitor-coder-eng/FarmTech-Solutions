import math
import subprocess

# Nome da empresa
empresa = "FarmTech Solutions"

# Dados iniciais
culturas = ["soja", "milho"]

# Insumos para Soja
insumos_soja = {
    "fertilizante": "Aumenta o rendimento da soja.",
    "herbicida": "Controla ervas daninhas.",
    "calcario": "Neutraliza a acidez do solo.",
    "inseticida": "Controla pragas na plantação.",
    "fungicida": "Previne o aparecimento de fungos."
}

# Insumos para Milho
insumos_milho = {
    "fertilizante": "Aumenta o rendimento do milho.",
    "herbicida": "Controla ervas daninhas no milho.",
    "inseticida": "Controla pragas específicas.",
    "adubo": "Melhora a nutrição do solo.",
    "fungicida": "Protege contra fungos prejudiciais."
}

# Valores padronizados de aplicação (litros ou kg/m²)
quantidade_insumos_soja = {
    "fertilizante": 0.05,  # litros/m²
    "herbicida": 0.02,  # litros/m²
    "calcario": 0.10,  # kg/m²
    "inseticida": 0.03,  # litros/m²
    "fungicida": 0.04  # litros/m²
}

quantidade_insumos_milho = {
    "fertilizante": 0.08,  # litros/m²
    "herbicida": 0.02,  # litros/m²
    "inseticida": 0.03,  # litros/m²
    "adubo": 0.12,  # kg/m²
    "fungicida": 0.05  # litros/m²
}

# Unidades de medida
unidades_insumos_soja = {
    "fertilizante": "litros",
    "herbicida": "litros",
    "calcario": "kg",
    "inseticida": "litros",
    "fungicida": "litros"
}

unidades_insumos_milho = {
    "fertilizante": "litros",
    "herbicida": "litros",
    "inseticida": "litros",
    "adubo": "kg",
    "fungicida": "litros"
}

# Vetores para armazenar os dados
dados_cultura = []
dados_area = []
dados_insumos = []


# Função para calcular a área plantada
def calcular_area(cultura):
    if cultura == "soja":
        # Retângulo: área = base * altura
        base = float(input("Informe a base do retângulo (m): "))
        altura = float(input("Informe a altura do retângulo (m): "))
        return base * altura
    elif cultura == "milho":
        # Círculo: área = pi * raio^2
        raio = float(input("Informe o raio do círculo (m): "))
        return math.pi * raio ** 2


# Função para escolher o insumo
def escolher_insumo(cultura):
    if cultura == "soja":
        print("\nEscolha um insumo para \033[1m\033[32mSoja\033[0m:\n")
        for insumo, descricao in insumos_soja.items():
            print(f"\033[1m{insumo.capitalize()}\033[0m: {descricao}\n")  # Nomes em negrito com espaçamento
        insumo_escolhido = input("Digite o nome do insumo escolhido: ").lower()
        # Aceitar "calcário" ou "calcario"
        if insumo_escolhido == "calcário":
            insumo_escolhido = "calcario"
        if insumo_escolhido in insumos_soja:
            return insumo_escolhido
        else:
            print("\033[1m\033[31mInsumo não identificado.\033[0m")
            return None
    elif cultura == "milho":
        print("\nEscolha um insumo para \033[1m\033[33mMilho\033[0m:\n")  # Amarelo para milho
        for insumo, descricao in insumos_milho.items():
            print(f"\033[1m{insumo.capitalize()}\033[0m: {descricao}\n")  # Nomes em negrito com espaçamento
        insumo_escolhido = input("Digite o nome do insumo escolhido: ").lower()
        if insumo_escolhido in insumos_milho:
            return insumo_escolhido
        else:
            print("\033[1m\033[31mInsumo não identificado.\033[0m")
            return None


# Função para calcular o manejo de insumos com valores padronizados
def calcular_manejo(cultura, area):
    if cultura == "soja":
        insumo = escolher_insumo("soja")
        if insumo:
            quantidade_padrao = quantidade_insumos_soja[insumo]  # Usa a quantidade padronizada
            unidade = unidades_insumos_soja[insumo]
            total_insumo = quantidade_padrao * area
            if unidade == "litros":
                quantidade_puro = total_insumo / 10
                quantidade_solucao = total_insumo
            elif unidade == "kg":
                quantidade_puro = total_insumo / 10
                quantidade_solucao = total_insumo
            print("\033[1m\033[32mDados inseridos com sucesso.\033[0m")
            return (quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo)
    elif cultura == "milho":
        insumo = escolher_insumo("milho")
        if insumo:
            quantidade_padrao = quantidade_insumos_milho[insumo]  # Usa a quantidade padronizada
            unidade = unidades_insumos_milho[insumo]
            total_insumo = quantidade_padrao * area
            if unidade == "litros":
                quantidade_puro = total_insumo / 10
                quantidade_solucao = total_insumo
            elif unidade == "kg":
                quantidade_puro = total_insumo / 10
                quantidade_solucao = total_insumo
            print("\033[1m\033[32mDados inseridos com sucesso.\033[0m")
            return (quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo)


# Funções para manipulação de dados
def atualizar_dados(posicao):
    cultura = input("Informe a nova cultura (Soja ou Milho): ").lower()
    if cultura in culturas:
        dados_cultura[posicao] = cultura
        dados_area[posicao] = calcular_area(cultura)
        resultados = calcular_manejo(cultura, dados_area[posicao])
        if resultados:
            quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo = resultados
            dados_insumos[posicao] = (quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo)
    else:
        print("\033[1m\033[31mCultura não identificada.\033[0m")


def deletar_dados(posicao):
    del dados_cultura[posicao]
    del dados_area[posicao]
    del dados_insumos[posicao]

def obter_previsao_tempo(cidade):
    # Executa o script R
    result = subprocess.run(['Rscript', 'weather_script.R', cidade], capture_output=True, text=True, encoding='utf-8')
    
    # Tenta decodificar corretamente com UTF-8, removendo caracteres inesperados
    output = result.stdout.encode('latin1').decode('utf-8')
    
    # Exibe o resultado corrigido
    print(output)


# Função do menu principal
def menu():
    print(f"\n\033[1m{'=' * 40}\033[0m")
    print(f"\033[1m\033[32m{empresa}\033[0m")
    print(f"\033[1m{'=' * 40}\033[0m")

    while True:
        print("\n\033[1m\033[32mMenu de Opções\033[0m")
        print("1. Registro de Cultura e Insumos")
        print("2. Relatórios de Manejo")
        print("3. Atualizar Informações")
        print("4. Deletar Informações")
        print("5. Obter Informações do Tempo")
        print("6. Finalizar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cultura = input("Informe a cultura (Soja ou Milho): ").lower()
            if cultura in culturas:
                dados_cultura.append(cultura)
                area = calcular_area(cultura)
                dados_area.append(area)
                resultados = calcular_manejo(cultura, area)
                if resultados:
                    quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo = resultados
                    dados_insumos.append((quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo))

                    # Impressão das informações
                    print(f"\n\033[1m\033[32mInformações Registradas\033[0m:")
                    print(f"Área total plantada: {area:.2f} m²")
                    print(
                        f"Quantidade a ser aplicada por m² de {insumo.capitalize()}: {quantidade_padrao:.2f} {unidade}")
                    print(f"Quantidade total de insumo puro: {quantidade_puro:.2f} {unidade}")
                    print(f"Quantidade total da solução: {quantidade_solucao:.2f} {unidade}")
            else:
                print("\033[1m\033[31mCultura não identificada.\033[0m")

        elif opcao == "2":
            print("\n\033[1m\033[32mRelatório de Manejo\033[0m:")
            if len(dados_cultura) > 0:
                for i in range(len(dados_cultura)):
                    area = dados_area[i]
                    quantidade_padrao, quantidade_puro, quantidade_solucao, unidade, insumo = dados_insumos[i]
                    cultura = dados_cultura[i]
                    print(f"\n\033[1mCultura:\033[0m {cultura.capitalize()}")
                    print(f"Área plantada: {area:.2f} m²")
                    print(
                        f"Quantidade a ser aplicada por m² de {insumo.capitalize()}: {quantidade_padrao:.2f} {unidade}")
                    print(f"Quantidade total de insumo puro: {quantidade_puro:.2f} {unidade}")
                    print(f"Quantidade total da solução: {quantidade_solucao:.2f} {unidade}")
            else:
                print("\033[1m\033[31mNenhuma informação registrada.\033[0m")

        elif opcao == "3":
            if len(dados_cultura) > 0:
                print("\n\033[1m\033[32mAtualizar Informações\033[0m:")
                for i, cultura in enumerate(dados_cultura):
                    print(f"{i + 1}. Cultura: {cultura.capitalize()} - Área: {dados_area[i]:.2f} m²")
                posicao = int(input("Escolha o número da posição para atualizar: ")) - 1
                if 0 <= posicao < len(dados_cultura):
                    atualizar_dados(posicao)
                else:
                    print("\033[1m\033[31mPosição inválida.\033[0m")
            else:
                print("\033[1m\033[31mNenhuma informação para atualizar.\033[0m")

        elif opcao == "4":
            if len(dados_cultura) > 0:
                print("\n\033[1m\033[32mDeletar Informações\033[0m:")
                for i, cultura in enumerate(dados_cultura):
                    print(f"{i + 1}. Cultura: {cultura.capitalize()} - Área: {dados_area[i]:.2f} m²")
                posicao = int(input("Escolha o número da posição para deletar: ")) - 1
                if 0 <= posicao < len(dados_cultura):
                    deletar_dados(posicao)
                else:
                    print("\033[1m\033[31mPosição inválida.\033[0m")
            else:
                print("\033[1m\033[31mNenhuma informação para deletar.\033[0m")

        elif opcao == "5":
            cidade = input("Digite o nome da cidade: ")
            if cidade:  # Verifica se o usuário inseriu uma cidade
                obter_previsao_tempo(cidade)
            else:
                print("\033[1m\033[31mVocê deve inserir um nome de cidade.\033[0m")

        elif opcao == "6":
            print("\033[1m\033[32mFinalizando o programa... FarmTech Solutions\033[0m")
            break

        else:
            print("\033[1m\033[31mOpção inválida.\033[0m")


# Executar o menu
menu()