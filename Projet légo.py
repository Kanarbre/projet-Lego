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
		self.table=None
		self.L=[]
		
		self.tk.mainloop()
		
		
		
	def taille(self):
		""""effacer le canvas précédent"""
		self.canvas.delete(self.table)
		for elem in self.L:
			self.canvas.delete(elem)
		self.L=[]
		
		"""calculer les dimensions"""
		
		echelle=32/25
		#échelle 32/25 tenons/cm
		#4 pixels par tenons
		pixel=4
		
		lon,lar=self.dimensions.get().split(',')
		lon_table=int(int(lon)*echelle) #nombre de tenons sur la longueur
		lar_table=int(int(lar)*echelle)
		lon_plaque=ceil(lon_table/32) #nombre de plaque
		lar_plaque=ceil(lar_table/32)
	
		
		# objet nécessaire
		nombre_plaque=max(lon_plaque,lar_plaque)
		
		
		self.plaque_lab.destroy()
		if lon_table%32>1 or lar_table%32>1:
			self.plaque_lab=Label(self.matcan,text='x'+str(nombre_plaque)+'\n plaque de base \n DECOUPEZ LA PLAQUE')
		else:
			self.plaque_lab=Label(self.matcan,text='x'+str(nombre_plaque)+'\n plaque de base')
		self.plaque_lab.grid()
		
		self.set_img(self.canvas,'photo plaque légo.png')


		"""dessiner la plaque"""
		
		#calcul en pixel
		lo=lon_table*pixel
		la=lar_table*pixel
		
		"""créer la table"""
		self.table=self.canvas.create_rectangle(350-lo,300-la,350+lo,300+la,fill="green")
		self.table
		
		"""crééer les tenons"""
		a=350-lo+pixel
		for i in range (lon_table):
			b=300-la+pixel
			for j in range (lar_table):
				point=self.canvas.create_oval(a-(pixel-1),b-(pixel-1),a+(pixel-1),b+(pixel-1))
				self.L.append(point)
				point
				b+=pixel*2
			a+=pixel*2
		
		

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
			forme=formes.copy()[i%3]
			elem=[i+1]+forme+[couleur]+[0.20]
			elem[1]+=couleur
			cata.append(elem)
			i+=1
		return cata

Table_lego()