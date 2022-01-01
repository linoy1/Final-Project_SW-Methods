# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
import mysql.connector
from db_connection import cursor, cnt
from user import User
import base64
import sys

person = User(305365455, 'Bob', 'Daniels', 'Bobbyboo', '0501231345', 'bob@gmail.com', 'bob123456', 'Manager')
# person.registerUser()

person.loginUser()

#
# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1
#
#         self.inside = GridLayout()
#         self.inside.cols = 2
#
#         self.inside.add_widget(Label(text="id: "))
#         self.id = TextInput(multiline=False)
#         self.inside.add_widget(self.id)
#
#         self.inside.add_widget(Label(text="itemId: "))
#         self.item = TextInput(multiline=False)
#         self.inside.add_widget(self.item)
#
#         self.inside.add_widget(Label(text="date: "))
#         self.date = TextInput(multiline=False)
#         self.inside.add_widget(self.date)
#
#         self.add_widget(self.inside)
#
#         self.submit = Button(text="Submit", font_size=40)
#         self.submit.bind(on_press=self.pressedButton)
#         self.add_widget(self.submit)
#
#     def pressedButton(self, instance):
#         id = self.id.text
#         item = self.item.text
#         date = self.date.text
#
#         print("id: ", id, "item: ", item, "date: ", date)
#         self.id.text = ""
#         self.item.text = ""
#         self.date.text = ""
#
# class myApp(App):
#     def build(self):
#         return MyGrid()
#
# if __name__ == '__main__':
#     myApp().run()