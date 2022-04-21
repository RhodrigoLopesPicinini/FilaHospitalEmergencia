import datetime
import os

class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item) # adiciona o item dentro do vetor
        self.__floatUp(len(self.heap) - 1) # ...

    def get(self): #EXTRACT MAX
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1] # retorna primeiro valor raiz (root)
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] # troca as posições i e j entre elas

    def __floatUp(self, index):
        parent = index//2 # identifica o pai
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent) # troca as posições index e parent entre elas
            self.__floatUp(parent) # recursividade: ...

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Paciente:
    def __init__(self, nomeCompleto, tipoSanguineo, dataNasciamento):
        self.nomeCompleto = nomeCompleto
        self.tipoSanguineo = tipoSanguineo
        self.dataNascimento = dataNasciamento

    def __str__(self):
        return f"Paciente: {self.nomeCompleto}, de tipo sanguíneo: {self.tipoSanguineo}, nascido na data: {self.dataNascimento}"

def imprimirChamado(lista):
    lista.reverse() # inverter lista para obter os ultimos adicionados
    if len(lista) > 5:
        for i in range(0, 5):
            print(f"{i+1}: {lista[i]}") # valores dentro dos ultimos 5 adicionados
    else:
        for i in range(0, len(lista)):
            print(f"{i+1}: {lista[i]}") # valores dentro dos ultimos adicionados (< 5)


filaPrioridade = MaxHeap() 
listaAux = [] # Lista auxiliar para os pacientes já chamados
ordem = 999 # Ordem dos chamados (de forma decrescente)

while(True):

    try:
        print(
            "============================================",
            "\n1) Adicionar novo paciente",
            "\n2) Chamar próximo paciente",
            "\n3) Mostrar próximo paciente (sem chamar)",
            "\n4) Listar os 5 últimos chamados",
            "\n5) Sair",
            "\n============================================"
            )

        op = int(input("Opção: "))
        os.system('cls')

        if op == 1:

            nomePaciente = input("Nome do paciente: ")
            tipoSanguineo = input("Tipo sanguíneo do paciente: ")
            dataNascimento = input("Data de nascimento do paciente: ")
            prioridade = int(input("Prioridade do paciente: "))

            if(prioridade < 1 or prioridade > 10):
                
                print("Valor inválido para prioridade, tente novamente...")
                continue

            novoPaciente = Paciente(nomePaciente, tipoSanguineo, dataNascimento) # Novo paciente
            ticket = (prioridade, ordem, novoPaciente) # Ticket para espera

            filaPrioridade.put(ticket) # Ticket é posto dentro da fila de espera
            ordem -= 1
            
        elif op == 2:

            print(filaPrioridade.heap[1][2]) # Primeiro paciente com máxima prioridade
            listaAux.append(filaPrioridade.heap[1][2]) # Paciente adicionado na lista auxiliar
            filaPrioridade.get() # Paciente extraído da fila
            print("Paciente retirado da fila de espera")
            
        elif op == 3:

            print(filaPrioridade.heap[1][2]) # Primeiro paciente com máxima prioridade
            
        elif op == 4:

            imprimirChamado(listaAux)

        elif op == 5:

            print("Encerramento do programa")
            break

        else:
            print("Valor inválido, tente novamente...")
            continue

    except IndexError:
        os.system('cls')
        print("Fila vazia!")
    except ValueError:
        os.system('cls')
        print("Valor inválido, tente novamente...")


