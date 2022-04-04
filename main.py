from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from pytube import YouTube
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.storage.jsonstore import JsonStore
import requests
import os
import time
from kivy.utils import platform


if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])





class TubeOder(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        kv1 = Builder.load_file("main.kv")
        kv2 = Builder.load_file("conv.kv")
        kv3 = Builder.load_file("final.kv")
        self.theme_cls.primary_palette = "Green"
      
        screen_manager.add_widget(kv1)
        screen_manager.add_widget(kv2)
        screen_manager.add_widget(kv3)
        return screen_manager

    def on_start(self):
        url =screen_manager.get_screen('MainScreen').ids.imagexpa.source
        timeout = 10
        try:
            request = requests.get(url, timeout=timeout)
            self.alpha=1
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.alpha=0
        
        if self.alpha==0:
            cancel_btn_username_dialogue = MDFlatButton(text='Cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error',text = "Please check your internet connection",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            screen_manager.current="MainScreen"
    
    def submit(self):
        link=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
        if link=="":
            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error',text = "Please input a valid Link",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            self.youtube_1=YouTube(link)
            screen_manager.get_screen('MainScreen').ids.imagexpa.source=self.youtube_1.thumbnail_url
            screen_manager.get_screen('MainScreen').ids.titlexpa.text=self.youtube_1.title
            screen_manager.get_screen('MainScreen').ids.disabled_button.disabled = False
            self.videos=self.youtube_1.streams
            
            for i in self.videos:
                
                alp=str(i).split()
               
                tagg=alp[1]
                tagg1=tagg.split('"')
                a=tagg1[1]
                b=int(a)
                
                
                
                tpe=alp[2]
                tagg2=tpe.split('"')
                a1=tagg2[1]
                
                
                res=alp[3]
                tagg3=res.split('"')
                a2=tagg3[1]
                
                
                fpss=alp[4]
                tagg4=fpss.split('"')
                a3=tagg4[1]
                
                
                f1=b,a1,a2,a3
                
                screen_manager.get_screen('Conv').ids.container.add_widget(OneLineListItem(text=f"{f1}", on_release=self.presser))
            
                

    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
        

        
    def presser(self, onelinelistitem):
        sef=self.videos
        vid=list(enumerate(self.videos))
        sef1=onelinelistitem.text
       
        length=len(sef)
        
        alp11=sef1.split()
        
        fpss1=alp11[0]
        alp12=fpss1.split('(')
        alp13=alp12[1]
        alp14=alp13.split(',')
        alp15=alp14[0]
        matag=int(alp15)
        
        
        if platform=="android":
            download_path="/storage/emulated/0/Tubeoder"
        else:
            home = os.path.expanduser('~')
            download_path = os.path.join(home, 'Tubeoder')
            
        strmm=self.youtube_1.streams.get_by_itag(matag)
        strmm.download(download_path)
        screen_manager.get_screen('FinalScreen').ids.sucess.text="Sucessfull!"
        screen_manager.get_screen('FinalScreen').ids.sucess1.text=download_path     
        screen_manager.current="FinalScreen"
        
       
TubeOder().run()
