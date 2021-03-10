from tkinter import *
from random import *
from math import *

class Table_lego:
    
	def __init__(self):
        
		self.tk=Tk()#créer la fenêtre
		
		self.canvas=Canvas(self.tk,takefocus='', width=800, height=600, bg='white')
		self.canvas.grid(column=0, row=0,rowspan=40)
		
		#création du catalogue
		self.catalogue=self.get_catalogue()
		
		#frame du matériel
		
		self.matFrame=Frame(self.tk,borderwidth=2,relief='groove')
		self.matFrame.grid(column=1,row=0)
		
		self.matcan=Canvas(self.matFrame,width=100, height=600)
		self.matcan.grid()
		
		self.liste=Label(self.matcan, text="Matériel nécessaire")
		self.liste.grid()
		
		self.plaque_lab=Label(self.matcan,text="")
		self.plaque_lab.grid()
		
		self.canvas.create_line(765,800,765,0)
		
		
		
		#frame des dimensions
		self.mainFrame =Frame(self.tk, borderwidth=2,relief='groove')
		self.mainFrame.grid()		
		
		
		self.titre=Label(self.mainFrame, text= 'MA TABLE LEGO', font='Helvetica', foreground='red')
		self.titre.grid()              
		
		"""Création de la fenêtre de demande des dimensions"""
		
		self.question = Label(self.mainFrame, text="Quel est la taille de la table ?(longueur,largeur)")
		
		self.question.grid()
		
		#demande des dimensions
		self.dimensions=StringVar()
		self.dimensions.set("25,25") 
		self.entry_dimensions=Entry(self.mainFrame, textvariable=self.dimensions)
		self.entry_dimensions.grid()
		
		#calcul
		self.taille_but=Button(self.mainFrame,text='Calcul',command=self.taille)
		self.taille_but.grid()
		
		#dessin de la table et de la plaque
		self.x=None
		self.y=None
		self.L=[]
		
		self.tk.mainloop()
		
		
		
	def taille(self):
		""""effacer le canvas précédent"""
		self.canvas.delete(self.x)
		self.canvas.delete(self.y)
		for elem in self.L:
			self.canvas.delete(elem)
		self.L=[]
		
		"""calculer les dimensions"""
		
		#échelle 32/25 tenons/cm
		#4 pixels par tenons
		
		lon,lar=self.dimensions.get().split(',')
		lon_table=int(lon)*100/32 #nombre de tenons sur la longueur
		lar_table=int(lar)*100/32
		lon_plaque=int(int(lon)*128/25-(int(lon)*128%25))
		lar_plaque=int(int(lar)*128/25-(int(lar)*128%25))
		print(lon_plaque,lon_table)
		
		# objet nécessaire
		nombre_plaque=ceil((lon_plaque*lar_plaque)/16384)
		
		self.plaque_lab.destroy()
		if nombre_plaque!=lon_plaque*lar_plaque/16384:
			self.plaque_lab=Label(self.matcan,text='x'+str(nombre_plaque)+'\n plaque de base \n DECOUPEZ LA PLAQUE')
		else:
			self.plaque_lab=Label(self.matcan,text='x'+str(nombre_plaque)+'\n plaque de base')
		self.plaque_lab.grid()
		
		self.set_img(self.canvas,'photo plaque légo.png')
		
		#dessiner la plaque
		
		"""Nombre de tenons"""
		lo=lon_plaque//4
		la=lar_plaque//4
	
		
		"""créer la table"""
		self.x=self.canvas.create_rectangle(350-lon_table,300-lar_table,350+lon_table,300+lar_table)
		self.x
		self.y=self.canvas.create_rectangle(350-lon_plaque,300-lar_plaque,350+lon_plaque,300+lar_plaque,fill='green')
		self.y
		
		"""crééer les tenons"""
		a=350-lon_plaque+4
		for i in range (lo):
			b=300-lar_plaque+4
			for j in range (la):
				point=self.canvas.create_oval(a-3,b-3,a+3,b+3)
				self.L.append(point)
				point
				b+=8
			a+=8
		
		

	def set_img(self,can,adresse):
		self.img=PhotoImage(file=adresse)
		can.create_image(795,50,image=self.img)
		
	def get_catalogue(self):
		couleurs=["noir","rouge","bleu clair","bleu foncé","jaune","orange","vert foncé","vert clair","violet","marron","blanc","gris"]
		formes=[["carré ",2,2],["rectangle horizontal ",2,4],["rectangle vertical ",4,2]]
		cata=[[0,"plaque verte",32,32,"vert",7.99]]
		i=0
		while i<len(couleurs)*len(formes):
			couleur=couleurs[i//3]
			forme=formes.copy()[i%3];
			elem=[i+1]+forme+[couleur]+[0.20]
			elem[1]+=couleur
			cata.append(elem)
			i+=1
		return cata
			
			
		
	
		

        
Table_lego()
        