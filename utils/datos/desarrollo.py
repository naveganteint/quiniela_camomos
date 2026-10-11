

import streamlit as st





  #******************** Completa las columnas deglosadas de la quiniela de 88888888888888888


def rellena_columnas_8(entrada):
        

        col_reducidas=['aaaaaaa','aaaabbb','bbbbaaa','bbbbbbb','bbaabaa','bbaaabb','aabbbaa','aabbabb','babaaba','bababab','abababa','ababbab','baabaab','baabbba','abbaaab','abbabba']
        #col_reducidash=['aaaaaaaabbbbbbbb','aaaabbbbaaaabbbb','aabbaabbaabbaabb','bbaaaabbaabbbbaa','abababababababab','babababababababa','abbabaababbabaab']
        desglose_columnas=[]
        cont_col_red=0
      
        
        for i in range (0,32):       #El desarrollo de esta quiniela es de 32 columnas
            cont_dobles=0
            columna=''                  #columnas a completar
            linea_reducida= col_reducidas[cont_col_red]
            cont_cad_red=0
            
            #print ("*****",i,cont_col_red,linea_reducida)   
            
            for c in range (0,14):
               col=entrada[c+1]
               
              
               
               if(len(col)==2):
                  
                  cont_dobles+=1
                  if cont_dobles==8:   #introduce doble que no es reducido
                     if i<16:
                       columna+=col[0]
                     else:
                       columna+=col[1]    
                  
                  else:                                        #introduce signos reducidos   
                      #columna+=linea_reducida[cont_cad_red]
                      
                      #*****
                      if (linea_reducida[cont_cad_red]=='a'):
                          columna+=col [0]  
                      else:
                          columna+=col [1]   
                      
                      #****** 
                      
                      
                      
                      cont_cad_red+=1    
                      if cont_cad_red==7 :          
                            cont_col_red+=1
                          
                 
               
               else:                        #introduce valores simples
                  columna+=col
               
               if cont_col_red==16:
                            cont_col_red=0
            
            
            
            
            desglose_columnas.append(columna)
            

           
        return desglose_columnas

#******************** Completa las columnas deglosadas de la quiniela de 7777777777777

def rellena_columnas_7(entrada):
        

        col_reducidas=['aaaaaaa','aaaabbb','bbbbaaa','bbbbbbb','bbaabaa','bbaaabb','aabbbaa','aabbabb','babaaba','bababab','abababa','ababbab','baabaab','baabbba','abbaaab','abbabba']
        #col_reducidash=['aaaaaaaabbbbbbbb','aaaabbbbaaaabbbb','aabbaabbaabbaabb','bbaaaabbaabbbbaa','abababababababab','babababababababa','abbabaababbabaab']
        desglose_columnas=[]
        cont_col_red=0
      
        
        for i in range (0,16):       #El desarrollo de esta quiniela es de 16 columnas
            cont_dobles=0
            columna=''                  #columnas a completar
            linea_reducida= col_reducidas[cont_col_red]
            cont_cad_red=0
            
            #print ("*****",i,cont_col_red,linea_reducida)   
            
            for c in range (0,14):
               col=entrada[c+1]
               
              
               
               if(len(col)==2):
                  
                  cont_dobles+=1
                                                        #introduce signos reducidos   

                  if (linea_reducida[cont_cad_red]=='a'):
                          columna+=col [0]  
                  else:
                          columna+=col [1]   
                      
                      #****** 
                      
                      
                      
                  cont_cad_red+=1    
                  if cont_cad_red==7 :          
                            cont_col_red+=1
                          
                 
               
               else:                        #introduce valores simples
                  columna+=col
               """
               if cont_col_red==16:
                            cont_col_red=0
            """
            
            
            
            desglose_columnas.append(columna)
            

           
        return desglose_columnas


##************contar aciertos de la columana ganadora en desarrollo

def contar_aciertos(columna_ganadora, desarrollo_7):
    aciertos = [0] * 15
    print ("inicio")
    for columna in desarrollo_7:
        contador = 0

        for i in range(14):
            if columna[i] == columna_ganadora[i]:
                contador += 1
            #print ("columna_",columna,"--i:",i,"datos",columna[i],columna_ganadora[i],contador)     

        aciertos[contador] += 1

    return aciertos