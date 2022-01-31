from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from pytube import YouTube
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock

#Window.size = (400, 520)

class TubeOder(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
    
        kv = Builder.load_file("welcomescreen.kv")
        kv1 = Builder.load_file("main.kv") 
        self.theme_cls.primary_palette = "Green"
        screen_manager.add_widget(kv)
        screen_manager.add_widget(kv1)
        return screen_manager
    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)
    def change_screen(self, dt):
        screen_manager.current="MainScreen"
    
    def submit(self):
        link=""
        youtube_1=YouTube(link)
        print(youtube_1.title)
        print(youtube_1.thumbnail_url)
        videos=youtube_1.streams.all()
        vid=list(enumerate(videos))
        for i in vid:
            print(i)
        print()
        strm=int(input("enter :  "))
        videos[strm].download()
        print("sucessfully")



TubeOder().run()
