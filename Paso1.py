# -*- coding: utf-8 -*-
import pandas as pd
import os

path ="D:\Documentos Usuario\Desktop\Python_Def\Preguntas.xlsx"
xlsheet="Hoja1"
df = pd.read_excel(io=path,sheet_name=xlsheet)
rnd_d_df = []
Continu = True
Estado =0
Cant_preg=1
xlsheet_H="Historico"
Puntaje=0    #parametro que se pasa la funcion puntaje como resultado :)
Nombre=""
Faux=0

def clr_console():
    os.system(" cls" if os.name == "nt" else "clear")

def pregunta_aleatoria(K):
    Filtro_df = df.query("Categoria == @K") #FIltro por categoria
    rnd_d_df  = Filtro_df.sample() #Seleccion pregunta aleatoria 
    return rnd_d_df

def puntaje(cant_p,resultado):
    resultado = resultado + (cant_p**2)
    return resultado

def pregunta_mostrar(rnd_d_df,cant,resultado):
    resultado = puntaje(cant,resultado)
    print("\n","Nivel:",cant,"\t","Puntaje Actual",resultado,"\n") 
    print(rnd_d_df['Pregunta'].values[0])
    print ("a)",rnd_d_df['a'].values[0])
    print ("b)",rnd_d_df['b'].values[0])
    print ("c)", rnd_d_df['c'].values[0])
    print ("d)",rnd_d_df['d'].values[0])
    return resultado

def validacion (cant):
    print ("\n","Desea continuar jugando ...","\t","presione 1 para seguir","\n")
    Respuesta = input("Ingrese respuesta >" )
    if Respuesta == "1":
        clr_console()
        Continu = True
        return Continu
    else:
        clr_console()
        print ("Gracias por jugar con nosotros","\n") 
        Continu = False
        return Continu  

def Resp ():
    Estado =0
    while Estado == 0:     # Validacion error de respuesta a b c d
            opcion = input("Responda la pregunta >" )
            if ((opcion != "a") and (opcion != "b") and (opcion != "c") and (opcion != "d")) :
                    clr_console()
                    Pu=pregunta_mostrar(rnd_d_df,Cant_preg,Puntaje)  
                    print ("\n",opcion, ", no es opcion no valida intente de nuevo")
            else:
                    if opcion == rnd_d_df['Marca'].values[0]:
                        print ("opcion correcta")
                        i=1
                        Estado = 1
                        return Estado,i
                    else:
                        print("\n","No es la opcion correcta")
                        i=0
                        Estado = 2
                        return Estado ,i

def Historico(Nombre,puntaje,faux):
    pathH ="D:\Documentos Usuario\Desktop\Python_Def\Historic.xlsx"
    xlsheet_H="Historico"
    df = pd.read_excel(io=pathH,sheet_name=xlsheet_H)
    [f,c]=df.shape
    if f+faux==0:
        print("Felicidades, eres el primer jugador!")
        print (f)
    else:
        print("\n","PUNTAJES ALCANZADOS")
        jugador={'Jugador ':[Nombre], 'Puntaje':[puntaje]}
        df2=pd.DataFrame(jugador, index= [f] )                                  #
        df3=pd.concat([df, df2], axis=0)                                        #concatena dataframes    
        df3=df3.sort_values(by=['Puntaje'],ascending=False, ignore_index=True)  #Ordena Valores de historico
        df3= df3.head(7)                                                        # toma solo los primeros 7 
        df3 = df3.query("Puntaje > 0")                                          #Filtro por puntaje
        df3.to_excel(excel_writer=pathH,sheet_name=xlsheet_H,index=False)       #Escritura registro en EXCEL
        print (df3)                                                                                 

Historico(Nombre,Puntaje,Faux)
while (Continu == True) and (Cant_preg < 6):
        if Cant_preg ==1:
                print("\n")
                Nombre=input("Ingresa tu nombre >" )
                Faux=1
                rnd_d_df = pregunta_aleatoria(Cant_preg)
                Pu=pregunta_mostrar(rnd_d_df,Cant_preg,Puntaje)         #Mostrar pregunta y opciones de respuesta
                [Estado, i] = Resp()
                if Estado == 1:
                        Cant_preg = Cant_preg + i
                        clr_console() 
                        print ("\n","opcion correcta")
                else: 
                        clr_console()
                        print("Respondiste mal Byeee","\n")
                        break                    
        else:
                rnd_d_df = pregunta_aleatoria(Cant_preg)
                Pu=pregunta_mostrar(rnd_d_df,Cant_preg,Puntaje)          #Mostrar pregunta y opciones de respuesta    
                [Estado, i] = Resp()
                if Estado == 1:
                        Cant_preg = Cant_preg + i 
                        Continu = validacion (Cant_preg)
                else: 
                        print("Respondiste mal Byeee","\n") 
                        break
print(Nombre , ", Tu puntaje final fue de:",Pu)
Historico (Nombre,Pu,Faux)