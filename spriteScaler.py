import pygame
import tkinter as tk
from tkinter import filedialog
import os.path as op
from os import walk


class ColorChanger():
	pygame.init()
	def __init__(self):		
		
		self.master = tk.Tk()
		self.master.geometry("384x128")
		self.master.title("Sprite scaler by Ashardalon78")

		tk.Label(self.master,text="Widht ratio:").grid(row=0,column=0)
		self.T1 = tk.Text(self.master,height=1,width=5)
		self.T1.grid(row=0,column=1)
		self.T1.insert(tk.END,0.2)
		tk.Label(self.master,text="Height ratio:").grid(row=1,column=0)
		self.T2 = tk.Text(self.master,height=1,width=5)
		self.T2.grid(row=1,column=1)
		self.T2.insert(tk.END,0.2)
		tk.Label(self.master,text="Rotation angle:").grid(row=2,column=0)
		self.T3 = tk.Text(self.master,height=1,width=5)
		self.T3.grid(row=2,column=1)
		self.T3.insert(tk.END,0.0)		
		
		tk.Button(self.master, text="Start", command=self.read_files).grid(row=3, column=0)		

		self.master.mainloop()				
		
	def read_files(self):				
		x_factor = float(self.T1.get('1.0',tk.END))
		y_factor = float(self.T2.get('1.0',tk.END))
		rot_ang = float(self.T3.get('1.0',tk.END))
		
		path = filedialog.askdirectory()
		if not path:
			return
	
		for root, subdirs, files in walk(path):			
			for name in files:
				if name.endswith(".png"):	
					print("Prosessing: " + str(op.join(root,name)))											
					sprite = pygame.image.load(op.join(root,name))
					sprite_scaled = self.scale_sprite(sprite, x_factor, y_factor, rot_ang)
					pygame.image.save(sprite_scaled, op.join(root,name))
					
	def scale_sprite(self, img, x_factor, y_factor, rot_ang):				
		width = int(x_factor * img.get_width())
		height = int(y_factor * img.get_height())

		return pygame.transform.rotate(pygame.transform.scale(img, (width, height)),rot_ang)
	
CC = ColorChanger()