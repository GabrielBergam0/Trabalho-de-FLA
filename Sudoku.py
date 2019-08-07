#______________________Sudoku_____________________
print('______________________Sudoku_____________________')
print ("            Seja bem-vindo ao Sudoku!")
print('___________________________')
casa = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
fixos = [[True,True,False,False,True,False,False,False,False],  #Retorna True se caso a casa escolhida seja fixa
         [True,False,False,True,True,True,False,False,False],
         [False,True,True,False,False,False,False,True,False],
         [True,False,False,False,True,False,False,False,True],
         [True,False,False,True,False,True,False,False,True],
         [True,False,False,False,True,False,False,False,True],
         [False,True,False,False,False,False,True,True,False],
         [False,False,False,True,True,True,False,False,True],
         [False,False,False,False,True,False,False,True,True]]
mapa = {          
   'A-1': (0, 0),     #Mapa funciona como um "tradutor"
   'A-2': (0, 1),     #Traduzindo o que foi digitado pelo usuário, no formato A-1
   'A-3': (0, 2),     #Para o valor da casa(tupla), no caso (0, 0)
   'A-4': (0, 3),
   'A-5': (0, 4),
   'A-6': (0, 5),
   'A-7': (0, 6),
   'A-8': (0, 7),
   'A-9': (0, 8),
   'B-1': (1, 0),
   'B-2': (1, 1),
   'B-3': (1, 2),
   'B-4': (1, 3),
   'B-5': (1, 4),
   'B-6': (1, 5),
   'B-7': (1, 6),
   'B-8': (1, 7),
   'B-9': (1, 8),
   'C-1': (2, 0),
   'C-2': (2, 1),
   'C-3': (2, 2),
   'C-4': (2, 3),
   'C-5': (2, 4),
   'C-6': (2, 5),
   'C-7': (2, 6),
   'C-8': (2, 7),
   'C-9': (2, 8),
   'D-1': (3, 0),
   'D-2': (3, 1),
   'D-3': (3, 2),
   'D-4': (3, 3),
   'D-5': (3, 4),
   'D-6': (3, 5),
   'D-7': (3, 6),
   'D-8': (3, 7),
   'D-9': (3, 8),
   'E-1': (4, 0),
   'E-2': (4, 1),
   'E-3': (4, 2),
   'E-4': (4, 3),
   'E-5': (4, 4),
   'E-6': (4, 5),
   'E-7': (4, 6),
   'E-8': (4, 7),
   'E-9': (4, 8),
   'F-1': (5, 0),
   'F-2': (5, 1),
   'F-3': (5, 2),
   'F-4': (5, 3),
   'F-5': (5, 4),
   'F-6': (5, 5),
   'F-7': (5, 6),
   'F-8': (5, 7),
   'F-9': (5, 8),
   'G-1': (6, 0),
   'G-2': (6, 1),
   'G-3': (6, 2),
   'G-4': (6, 3),
   'G-5': (6, 4),
   'G-6': (6, 5),
   'G-7': (6, 6),
   'G-8': (6, 7),
   'G-9': (6, 8),
   'H-1': (7, 0),
   'H-2': (7, 1),
   'H-3': (7, 2),
   'H-4': (7, 3),
   'H-5': (7, 4),
   'H-6': (7, 5),
   'H-7': (7, 6),
   'H-8': (7, 7),
   'H-9': (7, 8),
   'I-1': (8, 0),
   'I-2': (8, 1),
   'I-3': (8, 2),
   'I-4': (8, 3),
   'I-5': (8, 4),
   'I-6': (8, 5),
   'I-7': (8, 6),
   'I-8': (8, 7),
   'I-9': (8, 8),
}
#______________________________Imprimindo__tabuleiro_________________________________
#Temos a função "imprime_tabuleiro", com uma matriz 9x9, permitindo que o tabuleiro
#seja impresso no decorrer do código, de forma atualizada a cada jogada.
#Com um total de 81 casas, sendo 30 fixas, e 51 vazias.
def imprime_tabuleiro():
   print('    1 2 3   4 5 6   7 8 9')                             
   print("---------------------------")
   print('A','|',casa[0][0],casa[0][1],casa[0][2]if casa[0][2]!=0 else ' ','|',casa[0][3]if casa[0][3]!=0 else ' ',casa[0][4],casa[0][5]if casa[0][5]!=0 else ' ','|',casa[0][6]if casa[0][6]!=0 else ' ',casa[0][7]if casa[0][7]!=0 else ' ',casa[0][8]if casa[0][8]!=0 else ' ','|')
   print('B','|',casa[1][0],casa[1][1]if casa[1][1]!=0 else ' ',casa[1][2]if casa[1][2]!=0 else ' ','|',casa[1][3],casa[1][4],casa[1][5],'|',casa[1][6]if casa[1][6]!=0 else ' ',casa[1][7]if casa[1][7]!=0 else ' ',casa[1][8]if casa[1][8]!=0 else ' ','|')
   print('C','|',casa[2][0]if casa[2][0]!=0 else ' ',casa[2][1],casa[2][2],'|',casa[2][3]if casa[2][3]!=0 else' ',casa[2][4]if casa[2][4]!=0 else' ',casa[2][5]if casa[2][5]!=0 else' ','|',casa[2][6]if casa[2][6]!=0 else' ',casa[2][7],casa[2][8]if casa[2][8]!=0 else' ','|')  
   print("----------+-------+--------")
   print('D','|',casa[3][0],casa[3][1]if casa[3][1]!=0 else ' ',casa[3][2]if casa[3][2]!=0 else ' ','|',casa[3][3]if casa[3][3]!=0 else ' ',casa[3][4],casa[3][5]if casa[3][5]!=0 else ' ','|' ,casa[3][6]if casa[3][6]!=0 else ' ',casa[3][7]if casa[3][7]!=0 else ' ',casa[3][8],'|')
   print('E','|',casa[4][0],casa[4][1]if casa[4][1]!=0 else ' ',casa[4][2]if casa[4][2]!=0 else ' ','|',casa[4][3],casa[4][4]if casa[4][4]!=0 else ' ',casa[4][5],'|',casa[4][6]if casa[4][6]!=0 else ' ',casa[4][7]if casa[4][7]!=0 else ' ',casa[4][8],'|')
   print('F','|',casa[5][0],casa[5][1]if casa[5][1]!=0 else ' ',casa[5][2]if casa[5][2]!=0 else ' ','|',casa[5][3]if casa[5][3]!=0 else ' ',casa[5][4],casa[5][5]if casa[5][5]!=0 else ' ','|',casa[5][6]if casa[5][6]!=0 else ' ',casa[5][7]if casa[5][7]!=0 else ' ',casa[5][8],'|')
   print("----------+-------+--------")
   print('G','|',casa[6][0]if casa[6][0]!=0 else ' ',casa[6][1],casa[6][2]if casa[6][2]!=0 else ' ','|',casa[6][3]if casa[6][3]!=0 else ' ',casa[6][4]if casa[6][4]!=0 else ' ',casa[6][5]if casa[6][5]!=0 else ' ','|',casa[6][6],casa[6][7],casa[6][8]if casa[6][8]!=0 else ' ','|')
   print('H','|',casa[7][0]if casa[7][0]!=0 else ' ',casa[7][1]if casa[7][1]!=0 else ' ',casa[7][2]if casa[7][2]!=0 else ' ','|',casa[7][3],casa[7][4],casa[7][5],'|',casa[7][6]if casa[7][6]!=0 else ' ',casa[7][7]if casa[7][7]!=0 else ' ',casa[7][8],'|')
   print('I','|',casa[8][0]if casa[8][0]!=0 else ' ',casa[8][1]if casa[8][1]!=0 else ' ',casa[8][2]if casa[8][2]!=0 else ' ','|',casa[8][3]if casa[8][3]!=0 else ' ',casa[8][4],casa[8][5]if casa[8][5]!=0 else ' ','|',casa[8][6]if casa[8][6]!=0 else ' ',casa[8][7],casa[8][8],'|')
   print("---------------------------")
imprime_tabuleiro()
cont_casa=30
#________________________________Verificando__se__a__posição__é__fixa____________________________________
#Verifica se existe uma posição no mapa igual a posição que o usuário digitou, e se a mesma é fixa ou não
def eh_fixo(casa):
   if casa in mapa: 
      pos = mapa[casa]
      lin = pos[0]
      col = pos[1]
      return fixos[lin][col]
   else:
      return True
   
#__________________Preenchendo__casa_______________
#Preenche a casa com o valor escolhido pelo usuário       
def preenche_casa(posicao, valor):
   pos = mapa[posicao]
   lin = pos[0]
   col = pos[1]   
   casa[lin][col]=int(valor)


#____________Verificando__se__tem__ganhador_________
def tem_ganhador():
   tem_ganhador = True

   
#________________Verificando__se__não__tem__número__repetido__na__Linha______________
#Verificando se a soma da linha é igual a 45
   ##print("Verificando linhas")
   for lin in casa:
      soma = sum(lin)
      ##print(soma) --> Foi feito para imprimir e assim poder verificar
      ##se as somas de linhas, colunas e quadrantes estavam sendo iguais a 45
      ##Isso foi feito para encontrarmos o erro com mais facilidade
      if soma != 45:
         tem_ganhador = False


#________________Verificando__se__não__tem__número__repetido__na__Coluna______________
#Verificando se a soma da coluna é igual a 45
   ##print("Verificando colunas")
   for c in range(9):
      soma = 0
      for l in range(9):
         soma += casa[l][c]
      ##print(soma)
      if soma != 45:
         tem_ganhador = False


#________________Verificando__se__não__tem__número__repetido__no__Quadrante___________
#Verificando se a soma do quadrante é igual a 45
   ##print("Verificando quadrantes")
   for l in range(3):
      for c in range(3):
         soma = 0
         for ll in range(l*3, (l+1)*3):
            for cc in range(c*3, (c+1)*3):
               soma += casa[ll][cc]
         ##print(soma)
         if soma != 45:
            tem_ganhador = False

   return tem_ganhador          
         
   
##__________________________Loop__principal_______________________________
while not tem_ganhador():                                             
   x=input('Escolha uma posição: ')                                       
   valor=input('Escolha um valor: ')                                      
   while eh_fixo(x) :                                                     
      x = input('A posição escolhida é inválida. Escolha outra posição: ')
                                                                          
   preenche_casa(x, valor)                                              
   cont_casa+=1                                                           
   imprime_tabuleiro()                                                    
print('*****************************************')                                                                        
print('*Parabéns, você completou o Sudoku!!!:D *')
print('*****************************************')
###########################################################################
