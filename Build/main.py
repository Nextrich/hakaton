from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Rectangle

import sqlite3

#from random import randint
news_start_point = 0
news_text = ""
news_text_static= ''
x = 0

Window.size = 320, 640
#Window.clearcolor = 244/255, 229/255, 128/255, 1
background_normal='bg.jpg'
Window.title = "Приложение"

#class Container(BoxLayout):
  #  pass
def news_update():
    global news_text
    dbn = 'data.db'
    conn = sqlite3.connect(dbn)
    cursor = conn.cursor()

    sqlite_news = """SELECT news from data"""
    cursor.execute(sqlite_news)
    record_news = cursor.fetchall()
    for row in record_news:
        news_text = row[0]
        conn.commit()
        conn.close()
        return news_text

class MyApp(App):

    def set_bg(self, *args):
        self.root_window.bind(size=self.do_resize)
        with self.root_window.canvas.before:
            self.bg = Rectangle(source='bg.jpg', pos=(0,0), size=(self.root_window.size))
    
    def __init__(self):
        super().__init__()
        #with self.canvas.before:
            #self.bg =Rectangle(pos=self.pos, size = self.size, source="bg.jpg")

    def do_resize(self, *args):
        self.bg.size = self.root_window.size

#Main buttons|| Я знаю, что можно было сделать через match, просто поздно доумался и лень переписывать
    def change_news(self,instance):
        global news_text
        global news_text_static
        global news_start_point
        self.btn_news.color = 'pink'
        self.btn_dogs.color = 'white'
        self.btn_acc.color = 'white'
        self.header.text = 'Новости:'
        if news_start_point == 0 or news_text == news_update() or news_text == news_update():
            self.message.text = news_update()
            news_start_point = 1
        else:
            print("Error")
            self.message.text = "Error"
        self.vik.opacity = 0
        self.mik.opacity = 0
        self.message.text_size=(250, 750)

    def change_dogs(self,instance):
        self.btn_news.color = 'white'
        self.btn_dogs.color = 'pink'
        self.btn_acc.color = 'white'


        self.header.text = 'Подопечные:'
        self.message.text = 'Наши животные:'
        self.vik.opacity = 1
        self.mik.opacity = 1

        self.message.text_size=(250, None)

    def change_acc(self,instance):
        self.btn_news.color = 'white'
        self.btn_dogs.color = 'white'
        self.btn_acc.color = 'pink'
        self.vik.opacity = 0
        self.mik.opacity = 0

        self.header.text = 'Аккаунт:'
        self.message.text = 'Ваши данные:'

        self.message.text_size=(250, None)
    
    def build(self):
        Clock.schedule_once(self.set_bg, 0)
        buttons_layout = GridLayout(cols=3, rows=5,row_force_default=True, row_default_height=60)

        #buttons
        
        self.btn_news = Button(text='Новости', size_hint_x=0.33, width=100, background_color=(243/255, 183/255, 48/255, 1), background_normal='btn_bg.png')
        self.btn_news.bind(on_press=self.change_news)
        buttons_layout.add_widget(self.btn_news)
        

        self.btn_dogs = Button(text='Подопечные', size_hint_x=0.33, width=100, background_color=(243/255, 183/255, 48/255, 1), background_normal='btn_bg.png')
        self.btn_dogs.bind(on_press=self.change_dogs)
        buttons_layout.add_widget(self.btn_dogs)

        self.btn_acc = Button(text='Аккаунт', size_hint_x=0.33, width=100, background_color=(243/255, 183/255, 48/255, 1), background_normal='btn_bg.png')
        self.btn_acc.bind(on_press=self.change_acc)
        buttons_layout.add_widget(self.btn_acc)

        self.vik = Button(text='Виктор', size_hint_x=1, size_hint_y=1, width=300, background_normal='2_breed.png', opacity=0)
        self.mik = Button(text='Михаил', size_hint_x=1, size_hint_y=1, width=300, background_normal='2_breed.png',opacity=0)
        
        #labels

        self.header = Label(text='', size_hint=(0.5, 0.33), color='white', bold=True)
    
        self.message = Label(text='', size_hint=(0.5, 0.33), text_size=(250, None), color='white', bold=True)    

        #matrix
        
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        buttons_layout.add_widget(self.header)
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        buttons_layout.add_widget(self.message)
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))

        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        buttons_layout.add_widget(self.vik)
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))
        buttons_layout.add_widget(self.mik)
        buttons_layout.add_widget(Label(text='', size_hint=(0.5, 0.33)))

        return buttons_layout
            
#text_size=(200, None)
        
if __name__ == '__main__':
    MyApp().run()
    
