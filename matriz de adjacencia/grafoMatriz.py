import os
from tkinter import messagebox
import unicodedata

def is_file_of_type(file_path, extension):
    return os.path.splitext(file_path)[1].lower() == extension.lower()

def SelectFile(Type:str):   
    import tkinter as tk
    from tkinter import filedialog
    file_path= ""
    flag=0
    
    # Function to open a file dialog and display the selected file path
    def select_file():
        globals()["file_path"] = filedialog.askopenfilename(filetypes=[("x", Type)])
        
        if is_file_of_type(  globals()["file_path"],Type):
            file_label.config(text=  globals()["file_path"])# Update label with the selected file path
            
            flag=1
            
        else:
            messagebox.showerror("Arquivo invalido!", "Escolha um Arquivo do tipo:"+Type)
    def confirmar():
        if is_file_of_type(  globals()["file_path"],Type):
         root.destroy()
            
        elif file_path== "":
            messagebox.showerror("Nenhum arquivo selecionado", "Escolha um Arquivo do tipo antes de confirmar:")
        else:
            messagebox.showerror("Arquivo invalido!", "Escolha um Arquivo do tipo:"+Type)

    # Create the main application window
    root = tk.Tk()
    root.title("File Selector")
    root.geometry("400x200")  # Set the window size

    # Create a label to display the file path
    file_label = tk.Label(root, text="No file selected")
    file_label.pack(pady=20)

    # Create a button to open the file dialog
    select_button = tk.Button(root, text="Selecionar documento", command=select_file)
    select_button2 = tk.Button(root, text="Confirmar", command=confirmar)
    select_button.pack(pady=10)
    select_button2.pack(pady=10)

    
    root.mainloop()
    return  globals()["file_path"]

def extrair_palavras(caminho_arquivo, encoding='utf-8'):
    """
    Extrai todas as palavras de um arquivo de texto, considerando acentos e outros símbolos,
    onde cada palavra está separada por uma nova linha.

    :param caminho_arquivo: O caminho para o arquivo de texto.
    :param encoding: O encoding do arquivo (padrão é 'utf-8').
    :return: Uma lista de palavras extraídas do arquivo.
    """
    palavras = []

    try:
        with open(caminho_arquivo, 'r', encoding=encoding) as arquivo:
            linhas = arquivo.readlines()

        # Processar cada linha para extrair e normalizar palavras
        for linha in linhas:
            palavra = linha.strip()  # Remove espaços em branco extras
            if palavra:  # Verifica se a linha não está vazia
                palavra_normalizada = unicodedata.normalize('NFKD', palavra)
                palavra_minuscula = palavra_normalizada.lower() 
                palavras.append( palavra_minuscula)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except UnicodeDecodeError:
        print(f"Erro ao decodificar o arquivo com o encoding: {encoding}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return palavras

def palavras():
    caminho= SelectFile(".txt")
    teste =  extrair_palavras(caminho)
    return teste  

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w]=0
            self.m = self.m - 1

    def in_degree(self, v):
        if v < 0 :
            raise ValueError("Vértice inválido")
        
        grau_entrada = 0
        for i in range(self.num_vertices):
            if self.matriz[i][v] == 1:
                grau_entrada += 1
        
        return grau_entrada
        
    def out_degree(self, v):
        if v < 0:
            raise ValueError("Vértice inválido")
        
        grau_saida = 0
        for j in range(self.num_vertices):
            if self.matriz[v][j] == 1:
                grau_saida += 1
        
        return grau_saida
    def verificar_fonte(self, v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if entrada == 0 and saida > 0 : 
            return 1 
        else: 
            return 0 
    def verificar_sorvedouro(self,v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if saida == 0 and entrada > 0 : 
            return 1 
        else: 
            return 0 
        
    def verificar_simetria(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz[i][j] != self.matriz[j][i]:
                    return 0
        return 1

    
	    
        
	    
            

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    
def CriarGrafoPorTxt():
    prin