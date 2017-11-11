#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:25:45 2016

@author: Eden
"""

from PyQt4 import QtCore, QtGui
import re
from math import * 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 650)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 130, 20))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 540, 100, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 570, 100, 20))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 540, 180, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 570, 180, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 270, 160, 20))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 570, 130, 20))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 570, 130, 20))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 600, 130, 20))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Form) 
        self.pushButton_9.setGeometry(QtCore.QRect(20, 270, 130, 20))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(Form) 
        self.pushButton_10.setGeometry(QtCore.QRect(240, 240, 130, 20))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(Form) 
        self.pushButton_11.setGeometry(QtCore.QRect(240, 270, 130, 20))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(Form) 
        self.pushButton_12.setGeometry(QtCore.QRect(640, 600, 130, 20))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))

        self.textEdit = QtGui.QTextEdit(Form) # edit text principal
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 350, 170))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.textEdit_boolean = QtGui.QTextEdit(Form) # edit boolean
        self.textEdit_boolean.setGeometry(QtCore.QRect(420, 50, 350, 170))
        self.textEdit_boolean.setObjectName(_fromUtf8("textEdit_boolean"))

        self.textEdit_fctacces = QtGui.QTextEdit(Form) # edit fonction d'accès
        self.textEdit_fctacces.setGeometry(QtCore.QRect(20, 350, 350, 170))
        self.textEdit_fctacces.setObjectName(_fromUtf8("textEdit_fctacces"))

        self.textEdit_vect = QtGui.QTextEdit(Form) # edit vectoriel
        self.textEdit_vect.setGeometry(QtCore.QRect(420, 350, 350, 170))
        self.textEdit_vect.setObjectName(_fromUtf8("textEdit_vect"))
        
        
        
        
        self.lineEdit_3 = QtGui.QLineEdit(Form) #line edit du model booleen
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 240, 300, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        
        
        self.lineEdit_4 = QtGui.QLineEdit(Form) #line edit requete model vect
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 540, 300, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))        
        
        
        self.label = QtGui.QLabel(Form) #label req booleen
        self.label.setGeometry(QtCore.QRect(420, 240, 50, 20))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.label_1 = QtGui.QLabel(Form)  #label req vectoriel
        self.label_1.setGeometry(QtCore.QRect(420, 540, 50, 20))
        self.label_1.setObjectName(_fromUtf8("label_1"))

        self.label_2 = QtGui.QLabel(Form) #document
        self.label_2.setGeometry(QtCore.QRect(20, 20, 60, 10))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(Form) #Modèle booléen
        self.label_3.setGeometry(QtCore.QRect(420, 20, 80, 10))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(Form) #Fonctions d'accès
        self.label_4.setGeometry(QtCore.QRect(20, 320, 120, 10))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(Form) #vectoriel
        self.label_5.setGeometry(QtCore.QRect(420, 320, 80, 10))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(Form) #vectoriel
        self.label_6.setGeometry(QtCore.QRect(20, 540, 80, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.label_7 = QtGui.QLabel(Form) #vectoriel
        self.label_7.setGeometry(QtCore.QRect(20, 570, 80, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        
    
        self.pushButton.clicked.connect(afficherDocuments) 
        self.pushButton_3.clicked.connect(indexdoc)
        self.pushButton_4.clicked.connect(indexmot)
        self.pushButton_10.clicked.connect(afficherIndex)
        self.pushButton_5.clicked.connect(modeleBooleen)
        self.pushButton_7.clicked.connect(modeleVectorielCosinus)
        self.pushButton_8.clicked.connect(modeleVectorielDice)
        self.pushButton_6.clicked.connect(modeleVectorielInterne)
        self.pushButton_9.clicked.connect(afficherFichierInverse)
        self.pushButton_11.clicked.connect(afficherFichierPoids)
        self.pushButton_12.clicked.connect(modeleVectorielJaccord)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    
                 
                 
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Recherche d'information", None))
        self.pushButton.setText(_translate("Form", "Afficher les documents", None))
        self.pushButton_9.setText(_translate("Form", "Fichier inverse", None))        
        self.pushButton_10.setText(_translate("Form", "Fichier index", None)) 
        self.pushButton_11.setText(_translate("Form", "Fichier poids", None)) 
        self.pushButton_3.setText(_translate("Form", "Exécuter", None))
        self.pushButton_4.setText(_translate("Form", "Exécuter", None))
        self.pushButton_5.setText(_translate("Form", "Lancer le modèle booléen", None))
        self.pushButton_6.setText(_translate("Form", "Formule interne", None))
        self.pushButton_7.setText(_translate("Form", "Formule COS", None))
        self.pushButton_8.setText(_translate("Form", "Formule Dice", None))
        self.pushButton_12.setText(_translate("Form", "Formule Jaccord", None))
        self.label.setText(_translate("Form", "Requete:", None))
        self.label_1.setText(_translate("Form", "Requete:", None))
        self.label_2.setText(_translate("Form", "Document:", None))
        self.label_3.setText(_translate("Form", "Modèle booléen:", None))
        self.label_4.setText(_translate("Form", "Fonctions d'accès:", None))
        self.label_5.setText(_translate("Form", "Modèle vectoriel:", None))
        self.label_6.setText(_translate("Form", "Index doc:", None))
        self.label_7.setText(_translate("Form", "Index mot:", None))
        
#############################################################################
 #PREPARATION DES DOCUMENTS       
#############################################################################
    
####################################################
#index et fichier inverse
#fichier_sortie=open("sortie.txt","w")

def extraire_requetes(requetes):
    ListCar={'.',',','!','?','-',':',';','#','@','$','(',')'}
    #stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}# a compléter

    f=open("cacm\\query.text")
    liste=list(f)
    documents=[]
    doc=[]
    doc.append(liste[0])
    i=1
    while(i<len(liste)):
        if liste[i].startswith(".I "):
            documents.append(doc)
            doc=[]
            doc.append(liste[i])        
        else:
            doc.append(liste[i])
                  
        i=i+1
    while(i<len(liste)):
        doc.append(liste [i])
    documents.append(doc)
    #print(documents[0])
    requetes=[]
    requetes2=[]
    rqt=[]
    marq2=[".B\n",".A\n",".N\n",".X\n"]
    for doc in documents:
        i=1
        while ((i<len(doc)) and (doc[i]!=".W\n")):
            i=i+1
        if(i<len(doc)):
            while((i<len(doc)) and (doc[i] not in marq2)):
                rqt.append(doc[i])
                i=i+1
            requetes.append(rqt)
    
        else:
            requetes.append(['.W\n'])
        rqt=[]
    
    for rqt in requetes:
         rqt=rqt.remove(rqt[0])    
    
    for r in requetes:
        res="".join(r)
        requetes2.append(res)
        
    
    
##################
 
    requetes=requetes2
    requetes2=[]
    k=0   
    while k<len(requetes):
         requetes[k]=requetes[k].lower()
         i=0
         while(i<len(requetes[k])):
            if(requetes[k][i] in ListCar):
                requetes[k]=requetes[k].replace(requetes[k][i]," ")
            i=i+1
         a=requetes[k].split()
#         for w in a:
#            if(w in stopList and len(w)>1):
#                    a.remove(w)
         a=" ".join(a)
         requetes2.append(a)
         k+=1
    
###################"    
        
      
    requetes=requetes2
    
    
    f=open("cacm\\qrels.text")
    liste=list(f)
    doc_pert=[]
    d=[]
    cpt=1
    for ligne in liste:
        ligne=ligne.split()
        if int(ligne[0])== cpt:
            d.append(int(ligne[1]))
        else:
            doc_pert.append(d)
            d=[]
            d.append(int(ligne[1]))
            cpt+=1
    doc_pert.append(d)
        
    
    return( requetes, doc_pert)
####
my_dico={}
requetes=[] 
doc_pert=[]         
(requetes,doc_pert)=extraire_requetes(requetes)
f=open("cacm\\cacm_all.all")
liste=list(f)
documents=[]
doc=[]
doc.append(liste[0])
i=1
while(i<len(liste)):
    if liste[i].startswith(".I "):
        documents.append(doc)
        doc=[]
        doc.append(liste[i])        
    else:
        doc.append(liste[i])
              
    i=i+1
while(i<len(liste)):
    doc.append(liste [i])
documents.append(doc)
titres=[]
titre=[]
marq=[".W\n",".B\n",".A\n",".N\n",".X\n"]
for doc in documents:
    i=1
    while ((i<len(doc)) and (doc[i]!=".T\n")):
        i=i+1
    if(i<len(doc)):
        while((i<len(doc)) and (doc[i] not in marq)):
            titre.append(doc[i])
            i=i+1
        titres.append(titre)
        titre=[]
        
resumes=[]
resume=[]
marq2=[".B\n",".A\n",".N\n",".X\n"]
for doc in documents:
    i=1
    while ((i<len(doc)) and (doc[i]!=".W\n")):
        i=i+1
    if(i<len(doc)):
        while((i<len(doc)) and (doc[i] not in marq2)):
            resume.append(doc[i])
            i=i+1
        resumes.append(resume)

    else:
        resumes.append(['.W\n'])
    resume=[]

#elimination des balises
for titre in titres:
    titre=titre.remove(titre[0])
    

for resume in resumes:
     resume=resume.remove(resume[0])    
#calculer le nombre des documents
N=len(documents)
#fusion des titres avec les resumes

documents= []
chaine=""
i=0
while i<N: 
    chaine_titre=' '.join(titres[i])
    chaine_resume=' '.join(resumes[i])
    documents.append(chaine_titre+" "+chaine_resume)
    i=i+1
    


#enlever les sauts de lignes
for document in documents:
    document=re.sub('\s+',' ',document)

#on a pas enlever les stoplist des soc
####################################
k=0
freq={}
ListCar={'.',',','!','?','-',':',';','#','@','$','(',')'}
stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}# a compléter
while k<len(documents):
 #fichier_sortie.write("\n**indexe de fréquences du document ")
 #fichier_sortie.write(str(k+1) )
 #fichier_sortie.write("*****\n\n")
 documents[k]=documents[k].lower()
 i=0
 while(i<len(documents[k])):
    if(documents[k][i] in ListCar):
        documents[k]=documents[k].replace(documents[k][i]," ")
    i=i+1
    
    
 #print(documents[5])
 a=documents[k].split()
 a2=[]
 nb=len(a)
# if(k==5 or k==1):
#     print(documents[k])
#     print(a)
 cpt_w=-1
 for w in a:
    cpt_w+1
   # if(k==1 or k==5):
#         print("word courant="+w)  
    if( w not in stopList and len(w)>1):
        if((w,k) not in freq):
#            if(w=="computers"):
#                print(w)
            freq[w,k]=a.count(w)
    
    #else:
           #a.remove(a[cpt_w])
            
            

            
 k=k+1
#print(freq)
#print(freq["glossary",9])
#fichier_sortie.write("\n--------------------------------------------\n")
#fichier_sortie.write("\nle fichier inverse de la collection\n")
#fichier_sortie.write(str(freq)+" ")  
#############################################################
#poids
ni={}
for(w,d) in freq:
    if (not w in ni):
        ni[w]=1
    else:
        ni[w]=ni[w]+1
# calcul de la freq max de chaque document 
max= {}
for (w,d) in freq:
    if (not d in max):
        max[d]=freq[w,d]
    else:
        if (freq[w,d]>max[d]): 
            max[d]=freq[w,d]

# calcul du fichier inverse avec poinds tf*idf
poids= {}
for (w,d) in freq: 
    poids[w,d]=round((float(freq[w,d])/max[d])*log10((float(N)/ni[w])+1),4)


###########################################################
# fonction 1 pour un document 
def indexdoc():
    d=ui.lineEdit.text()
    d=int(d)
    d=d-1
    ui.textEdit_fctacces.clear()
    ui.textEdit_fctacces.append("l'index pondere du document "+str(d+1)+" est:\n")
    for (a,b) in freq:
        if (b==d):
            p=freq [a,d]
            p2=poids[a,d]
            ui.textEdit_fctacces.append(a+':'+str(p)+" // "+str(p2))

 ############################################################################"
def indexmot():
    ui.textEdit_fctacces.clear()
    
    w=ui.lineEdit_2.text()
    w=""+w
    ui.textEdit_fctacces.append("les fréquences du mot " +w+" dans les documents sont")
   
    for(a,b) in freq:
       if (a==w):
            p=freq[w,b]
            p2=poids[w,b]
            ui.textEdit_fctacces.append(str(b+1)+";"+str(p)+" // "+str(p2))
#############################################################################
def afficherDocuments():
    ui.textEdit.clear()
    i=0
    while(i<20):    #   while(i<len(documents)): 
        ui.textEdit.append("DOCUMENT "+str(i+1)+":")
        ui.textEdit.append(documents[i])
        ui.textEdit.append("--------------------------")
        i=i+1
    
#########################################################################""
def afficherFichierInverse():
    ui.textEdit.clear()
    ui.textEdit.append("le fichier inverse de la collection\n")
    ui.textEdit.append(str(freq)+" ")  

#####################################################################"     
def afficherIndex():
    ui.textEdit.clear()
    ui.textEdit.append("index:")
    i=0
    while i<20: # while i<len(documents):
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append("Document "+str(i+1))
        ui.textEdit.append("--------------------------------")
        for (w,k) in freq:
            if(k==i) :
                p2=poids[w,k]
                ui.textEdit.append(str(w)+" : "+str(freq[w,k])+" // "+str(p2))
        i=i+1
#####################################################################" 
def modeleBooleen():   
    ui.textEdit_boolean.clear()
    req=ui.lineEdit_3.text()
    req=""+req
    pertinents=[]
    doc=[]
    req=req.lower()
    requette=req.split()
    
    requette1=[]
    for chaine in requette:
        while chaine.startswith("("):
            chaine2=""
            indice=1
            while indice<len(chaine):
                chaine2+=chaine[indice]
                indice+=1
            requette1.append("(")
            chaine=chaine2
        if chaine!="":
            requette1.append(chaine)
    requette=requette1
    requette1=[]
    
    for chaine in requette:
        compteur=0
        while chaine.endswith(")"):
            chaine2=""
            indice=0
            while indice<len(chaine)-1:
                chaine2+=chaine[indice]
                indice+=1
            compteur+=1
            chaine=chaine2
        if chaine!="":    
            requette1.append(chaine)
        indice=0
        while indice<compteur:
            requette1.append(")")
            indice+=1
    requette=requette1
    
    requette1=[]
    for chaine in requette:
        while chaine.startswith(")"):
            chaine2=""
            indice=1
            while indice<len(chaine):
                chaine2+=chaine[indice]
                indice+=1
            requette1.append(")")
            chaine=chaine2
        if chaine!="":
            requette1.append(chaine)
    requette=requette1
    requette1=[]
    
    for chaine in requette:
        compteur=0
        while chaine.endswith("("):
            chaine2=""
            indice=0
            while indice<len(chaine)-1:
                chaine2+=chaine[indice]
                indice+=1
            compteur+=1
            chaine=chaine2
        if chaine!="":    
            requette1.append(chaine)
        indice=0
        while indice<compteur:
            requette1.append("(")
            indice+=1
    requette=requette1
    requette1=[]
    
    for chaine in requette:
        if chaine!="(" and chaine!=")" and ( "(" in chaine or ")" in chaine ) :
            indice=0
            while indice<len(chaine):
                chaine2=""
                while indice<len(chaine) and chaine[indice]!='(' and chaine[indice]!=')' :
                    chaine2+=chaine[indice]
                    indice+=1
                if chaine2!="":
                    requette1.append(chaine2)
                while indice<len(chaine) and ( chaine[indice]=='(' or chaine[indice]==')' ):
                    requette1.append(chaine[indice])
                    indice+=1
                chaine2=""
                while indice<len(chaine) and chaine[indice]!='(' and chaine[indice]!=')' :
                    chaine2+=chaine[indice]
                    indice+=1
                if chaine2!="":
                    requette1.append(chaine2)
        else:
            requette1.append(chaine)
    
    requette=requette1   
    
    i=0
    c=1
    for d in documents:
        for term in requette:
            if term not in ["and","or","not","(",")"]:
                L=d.split()       
                if term in L:
                    term="1"      
                else:
                    term="0"
                doc.append(term)
            else:
                doc.append(term)   
        exp=""        
        exp=' '.join(doc)
        doc=[]
        try:
            e=eval(exp)
            if e==1:
                pertinents.append(i+1)
        except  SyntaxError:
                if c==1 :
                    ui.textEdit_boolean.append("Erreur syntaxique dans la requête")
                    c=2
        i=i+1  
    ui.textEdit_boolean.append("la liste des documents pertinents a cette requete sont:")
    ui.textEdit_boolean.append(str(pertinents))
####################################################################" 
def afficherFichierPoids():
    ui.textEdit.clear()   
    ui.textEdit.append("Le fichier des poids:")
    ui.textEdit.append(str(poids))
#############################
def my_func(cle):
    global my_dico
    return my_dico[cle]
###################################################################
def modeleVectorielInterne(): 
    stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}
    global requetes 
    global doc_pert
    global my_dico
    my_dico={}
    sys_pert=[]
    ui.textEdit_vect.clear()
    r=ui.lineEdit_4.text()
    r=int(r)
    req=requetes[r-1]
    ui.textEdit_vect.append("Requête= "+req)
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Ordre décroissant de pertinence des documents:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    req=req.lower()
    requette=req.split()
    i=0
    for document in documents:
        i=i+1
        sim=0
        d=document.split()
        for terme in requette:
            if len(terme)>1 and terme not in stopList :  
                if terme in d: 
                    sim=sim+poids[terme,i-1]
        my_dico[i]=sim
        if(sim>0):
            sys_pert.append(i)

    ui.textEdit.clear()    
    ui.textEdit.append("Les documents pertinents à la requête numéro "+str(r)+" sont :" )
    for i in  sorted(my_dico,key=my_func,reverse=True)[:20]:
        ui.textEdit_vect.append("sim("+str(i)+",R)="+str(round(my_dico[i],4)))  
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append("Document "+str(i))
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append(documents[i-1])
        
    env_pert=doc_pert[r-1]
    cpt=0
    for d in env_pert:
        if d in sys_pert:
            cpt+=1
    if(len(env_pert)>0):
        rappel=cpt/len(env_pert)
    else:
        rappel=0
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Evaluation du système:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Rappel="+str(round(rappel,4)))
    if(len(sys_pert)):
        precision=cpt/len(sys_pert)
    else:
        precision=0
    ui.textEdit_vect.append("Précision="+str(round(precision,4)))
    
####################################################################    
def modeleVectorielCosinus():
    stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}
    global requetes 
    global my_dico
    global doc_pert
    sys_pert=[]

    my_dico={}
    ui.textEdit_vect.clear()
    r=ui.lineEdit_4.text()
    r=int(r)
    req=requetes[r-1]
    ui.textEdit_vect.append("Requête= "+req)
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Ordre décroissant de pertinence des documents:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    req=req.lower()
    requette=req.split()
    i=0
    for document in documents:
        i=i+1
        s=0
        sim=0
        sim2=1
        cpt=0
        produit=1
        d=document.split()
        for terme in requette:
            if len(terme)>1 and terme not in stopList :
                if terme in d:
                    cpt=cpt+1
                    s=s+poids[terme,i-1]*poids[terme,i-1]
                    sim=sim+poids[terme,i-1]                   
        produit=sqrt(s*cpt)    
        if produit!=0 :  
            sim2=sim/produit
            my_dico[i]=sim2 
            
            if(sim2>0):
                sys_pert.append(i)
        else:
            my_dico[i]=0  
            
    ui.textEdit.clear()    
    ui.textEdit.append("Les documents pertinents à la requête numéro "+str(r)+" sont :" )        
    for i in  sorted(my_dico,key=my_func,reverse=True)[:20]:
        ui.textEdit_vect.append("sim("+str(i)+",R)="+str(round(my_dico[i],4)))  
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append("Document "+str(i))
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append(documents[i-1])
    env_pert=doc_pert[r-1]
    cpt=0
    for d in env_pert:
        if d in sys_pert:
            cpt+=1
    if(len(env_pert)>0):
        rappel=cpt/len(env_pert)
    else:
        rappel=0
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Evaluation du système:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Rappel="+str(round(rappel,4)))
    if(len(sys_pert)>0):
        precision=cpt/len(sys_pert)
    else:
        precision=0
    ui.textEdit_vect.append("Précision="+str(round(precision,4)))
#############################################"

################
def modeleVectorielDice():
    stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}
    global requetes 
    global my_dico
    global dico_pert
    sys_pert=[]
    my_dico={}
    ui.textEdit_vect.clear()
    r=ui.lineEdit_4.text()
    r=int(r)
    req=requetes[r-1]
    ui.textEdit_vect.append("Requête= "+req)
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Ordre décroissant de pertinence des documents:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    req=req.lower()
    requette=req.split()
    i=0
    for document in documents:
        i=i+1
        s=0
        sim=0
        sim3=1
        cpt=0
        somme=0
        d=document.split()
        for terme in requette:
            if len(terme)>1 and terme not in stopList :
                if terme in d:
                    cpt=cpt+1
                    sim=sim+poids[terme,i-1]
                    s=s+poids[terme,i-1]*poids[terme,i-1]
        somme=s+cpt 
        if somme!=0 :
            sim3=2*sim/somme
            my_dico[i]=sim3
            if(sim3>0):
                sys_pert.append(i)
        else:
            my_dico[i]=0
    ui.textEdit.clear()    
    ui.textEdit.append("Les documents pertinents à la requête numéro "+str(r)+" sont :" )        
    for i in  sorted(my_dico,key=my_func,reverse=True)[:20]:
        ui.textEdit_vect.append("sim("+str(i)+",R)="+str(round(my_dico[i],4)))    
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append("Document "+str(i))
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append(documents[i-1])
    env_pert=doc_pert[r-1]
    cpt=0
    for d in env_pert:
        if d in sys_pert:
            cpt+=1
    if(len(env_pert)>0):
        rappel=cpt/len(env_pert)
    else:
        rappel=0
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Evaluation du système:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Rappel="+str(round(rappel,4)))
    if(len(sys_pert)>0):
        precision=cpt/len(sys_pert)
    else:
        precision=0
    ui.textEdit_vect.append("Précision="+str(round(precision,4)))
##############################################"       
def modeleVectorielJaccord():
    stopList={"an","and","or","a","the","that","where","is","when","how","in","on","by","to","too","for","of","about","with"}
    global requetes 
    global my_dico
    global doc_pert
    sys_pert=[]
    my_dico={}
    ui.textEdit_vect.clear()
    r=ui.lineEdit_4.text()
    r=int(r)
    req=requetes[r-1]
    ui.textEdit_vect.append("Requête= "+req)
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Ordre décroissant de pertinence des documents:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    req=req.lower()
    requette=req.split()
    i=0
    for document in documents:
        i=i+1
        s=0
        s2=0
        sim=0
        sim4=1
        cpt=0
        somme=0
        d=document.split()
        for terme in requette:
            if len(terme)>1 and terme not in stopList :
                if terme in d:
                    cpt=cpt+1
                    s=s+poids[terme,i-1]*poids[terme,i-1]
                    sim=sim+poids[terme,i-1]
        somme=s+cpt-sim 
        if somme!=0 :
            sim4=sim/somme
            my_dico[i]=sim4  
            if(sim4>0):
               sys_pert.append(i)
        else:
            my_dico[i]=0 
    ui.textEdit.clear()    
    ui.textEdit.append("Les documents pertinents à la requête numéro "+str(r)+" sont :" )
    for i in  sorted(my_dico,key=my_func,reverse=True)[:20]:
        ui.textEdit_vect.append("sim("+str(i)+",R)="+str(round(my_dico[i],4))) 
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append("Document "+str(i))
        ui.textEdit.append("--------------------------------")
        ui.textEdit.append(documents[i-1])
        
    env_pert=doc_pert[r-1]
    cpt=0
    for d in env_pert:
        if d in sys_pert:
            cpt+=1
    if(len(env_pert)>0):
        rappel=cpt/len(env_pert)
    else:
        rappel=0
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Evaluation du système:")
    ui.textEdit_vect.append("-----------------------------------------------------")
    ui.textEdit_vect.append("Rappel="+str(round(rappel,4)))
    if(len(sys_pert)>0):
        precision=cpt/len(sys_pert)
    else:
        precision=0
    ui.textEdit_vect.append("Précision="+str(round(precision,4)))
###############################################################"            
def MSG_Problem(self):
        QtGui.QMessageBox.about(None,"Critical",
                                "Données Incorrect")       
if __name__ == "__main__":

    import sys
    app= QtGui.QApplication(sys.argv)
    mainWindow=QtGui.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())