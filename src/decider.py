# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Anton Relin"

from PIL import Image, ImageTk
import Tkinter as tk
from os import listdir
import os
from random import choice
import sys
import pygame
try:
    from urllib.parse import urljoin
    from urllib.request import pathname2url
except ImportError: # Python 2
    from urlparse import urljoin
    from urllib import pathname2url

    
alien_extension = "extra/alienhi.png"    
dir = "/home/user/Pictures/"
ext2conttype ={"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "gif": "image/gif"}  

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.configure(background='black')
        master.bind('<Escape>',self.toggle_geom)
        self.do_actions(master)
       
        #self.play_sound(sound_file)  
            
    def path2url(self, path):
        return urljoin('file:', pathname2url(os.path.abspath(path)))     
    
    def do_actions(self, master):
        """find photos, create buttons, do setup"""
        photo1, photo2 = self.random_file(dir)
        photo_list = [photo1, photo2]
        print photo_list
        photo_solution = choice(photo_list)
        sound_file = self.get_sound(photo_solution)
        button_photo_temp1 = Image.open(dir+photo1)
        button_photo_temp2 = Image.open(dir+photo2)
        button_photo1 = ImageTk.PhotoImage(button_photo_temp1)
        button_photo2 = ImageTk.PhotoImage(button_photo_temp2)
        first.image2 = alien_image
        first.image = button_photo1
        second.image = button_photo2
        first.config(image = button_photo1, command=lambda: self.check_solution(photo1, photo_solution, second, master, 1))
        second.config(image = button_photo2, command=lambda: self.check_solution(photo2, photo_solution, first, master, 2))
        first.pack(side = tk.RIGHT, padx=300, pady=5)
        second.pack(side = tk.RIGHT, padx=100, pady=5)
        print sound_file
        sound_file_new = self.path2url(sound_file)
        sounda= pygame.mixer.Sound(sound_file_new)
        sounda.play()
        
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
     
    def get_sound(self, filename):
        """ gets the sound file for the correct solution """
        barename = os.path.splitext(filename)
        prefinal = ''.join(barename[0])
        return dir+prefinal+".aac"        
        
    def isimage(self, filename):
        """true if the filename's extension is in the content-type lookup"""
        filename = filename.lower()
        return filename[filename.rfind(".")+1:] in ext2conttype
    
    def random_file(self, dir):
        """returns the filename of a randomly chosen image in dir"""
        images = [f for f in listdir(dir) if self.isimage(f)]
        image1 = choice(images)
        image2 = image1
        while(image2 == image1):
            image2 = choice(images)            
        return image1, image2
    
    def play_wrong(self):
        wrong = pygame.mixer.Sound(dir+"wrong.aac")
        wrong.play()
    
    def play_right(self):
        right = pygame.mixer.Sound(dir+"right.aac")
        right.play
    
    def check_solution(self, given, actual, other_button, window, identifier):
        if(given != actual):
            #if(identifier == 1):
            #    first.flash()
            #else:
            #    second.flash()
            #print "flashing"
            self.play_wrong
            self.do_actions(window)
 
        else:
            self.play_right
            self.do_actions(window)

  
        
root=tk.Tk()
pygame.mixer.init(44100, -16, 2, 2048)
alien_photo_temp = Image.open(dir+alien_extension)
alien_image = ImageTk.PhotoImage(alien_photo_temp)
first=tk.Button(root,justify = tk.RIGHT)
second=tk.Button(root,justify = tk.RIGHT)
tk.Label(root, image=alien_image, background='black').pack(side=tk.LEFT)
app=FullScreenApp(root)
root.mainloop()