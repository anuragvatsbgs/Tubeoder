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


#Window.size = (400, 520)

class TubeOder(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        kv = Builder.load_file("welcomescreen.kv")
        kv1 = Builder.load_file("main.kv")
        kv2 = Builder.load_file("conv.kv") 
        self.theme_cls.primary_palette = "Green"
        screen_manager.add_widget(kv)
        screen_manager.add_widget(kv1)
        screen_manager.add_widget(kv2)
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        screen_manager.current="MainScreen"
    
    def submit(self):
        link=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
        if link=="":
            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error',text = "Please input a valid Link",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            youtube_1=YouTube(link)
            screen_manager.get_screen('MainScreen').ids.imagexpa.source=youtube_1.thumbnail_url
            screen_manager.get_screen('MainScreen').ids.titlexpa.text=youtube_1.title
            screen_manager.get_screen('MainScreen').ids.disabled_button.disabled = False
            self.videos=youtube_1.streams
            
            for i in self.videos:
                screen_manager.get_screen('Conv').ids.container.add_widget(OneLineListItem(text=f"{i}", on_release=self.presser))
            
                

    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
        
    def presser(self, onelinelistitem):
        sef=self.videos
        vid=list(enumerate(self.videos))
        sef1=onelinelistitem.text
        for i in self.videos:
            print(sef1)
            
            if sef1==sef:
                print("sucessfully")
            else:
                print("error")
            print(sef)   

        
        
    def download_button(self):
        videos=youtube_1.streams.all()
        vid=list(enumerate(videos))
        for i in vid:
            print(i)
        print()
        strm=int(input("enter :  "))
        videos[strm].download()
        print("sucessfully")




TubeOder().run()
