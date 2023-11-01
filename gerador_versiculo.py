import json
import pandas as pd

'''Gerador de Versiculos'''

#Função para extrair versiculos
def extrair_versiculos(livros_abrev, capitulos):

    
    lista_de_versiculos= []
    
    #Numerando os livros da Bíblia
    for indice_do_livro, capitulo_do_livro in enumerate(capitulos):
        
        #Numerando os capitulos dos livros da Bíblia
        for indice_do_capitulo, versiculo_por_capitulo in enumerate(capitulo_do_livro):
            numero_versiculo = 1
            
            #Numerando e distribuindo versiculos referente a cada livro e capitulo da Bíblia
            for numero_versiculo, versiculo in enumerate(versiculo_por_capitulo, start = 1):
                lista_de_versiculos.append((livros_abrev[indice_do_livro], indice_do_capitulo + 1, numero_versiculo, versiculo))
                numero_versiculo += 1
     
    return lista_de_versiculos


#função para formartar versiculo
def formatar_versiculo(linha):
    return f' ❝{linha["vers"]}❞ \n ∾ ⁕ {linha["livro"]} {linha["cap"]}:{linha["n_vers"]} ⁕ ∾ '


# testamento
def velho_Testamento(liv):
    velho_testamento= []
    for indice, livro in enumerate(liv):
        if indice < 39:
            velho_testamento.append(livro)
    return velho_testamento

def novo_Testamento(liv):
    novo_testamento= []
    for indice, livro in enumerate(liv):
        if indice >= 39:
            novo_testamento.append(livro)
    return novo_testamento
        

#Arquivo biblia
try: 
    with open ("C:\\Users\\janyy\\Downloads\\biblia\\acf.json", 'r', encoding= 'utf-8-sig') as file:
        biblia= json.load(file)        
except FileNotFoundError:
    print(" O arquivo JSON não foi encontrado.")  
except ValueError as erro:
    print(f' Erro ao ler o arquivo JSON: {erro}')
    

#Separando livro, capitulo e versiculos
livros = [livro ["abbrev"].capitalize() for livro in biblia]
capitulos = [cap ["chapters"] for cap in biblia]
versiculos= extrair_versiculos(livros, capitulos)


novo_testamento= novo_Testamento(livros)
velho_testamento= velho_Testamento(livros)

#DataFrame Biblia
biblia_df= pd.DataFrame(versiculos, columns= ['livro', 'cap', 'n_vers', 'vers'])

livros_escolhidos= str(input(f'''Escolha os livros que você deseja?
\nVelho Testamento:\n
{' - '.join(velho_testamento)}

\033[1mNovo Testamento:\n
{' - '.join(novo_testamento)}

--> ''')).capitalize()

lista_livros = [livro.strip() for livro in livros_escolhidos.split(',')]

quantidade_versiculo= int(input(f'''Informe a quantidade de versículo
desejado dos livros escolhidos, "{livros_escolhidos}": '''))


versiculos_aleatorios= biblia_df[biblia_df['livro'].isin(lista_livros)].sample(n= quantidade_versiculo)
versiculos_aleatorios= versiculos_aleatorios.apply(formatar_versiculo, axis=1)
nome_arquivo= input('Digite o nome do arquivo: ')
versiculos_aleatorios.to_excel(nome_arquivo + '.xlsx', index= False, engine='openpyxl')





