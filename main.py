from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.layout import Layout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.widget import Widget

import random
from file_fill import generate
from randomiser import Randomiser

# color = [None] * 5
# color[0] = [33/255, 121/255, 108/255, 1]
# color[1] = [157/255, 180/255, 245/255, 0.1]
# color[2] = [216/255, 215/255, 225/255, 1]
# color[3] = [115/255, 120/255, 130/255, 1]
# color[4] = [118/255, 125/255, 140/255, 1]

size_x, size_y = Window.size[1], Window.size[0]
# Window.size = (size_x*.8, size_y)
print(Window.size[1])
Window.clearcolor = [216/255, 215/255, 225/255, 1]
font = size_x/10

class AppGrid(Widget):

    # def build(self):
    #     self.icon = '123.png'
    #     icon_close = Button(text='X',
    #         bold = True,
    #         font_size = font,
    #         background_color = color[2],
    #         background_normal = '',
    #         color = color[4],
    #         size_hint = [0.2, 0.2])
    #     icon_close.bind(on_press=self.btn_stop_press)

    #     self.ep_label = Label(text='0',
    #         font_size = font*1.6,
    #         # size_hint_y = 0.8,
    #         color = color[4],
    #         bold = True,
    #         halign = 'center')

    #     self.ep_input = TextInput(multiline=False,
    #         input_filter = 'int',
    #         halign = 'center',
    #         hint_text = 'Ep. Num',
    #         font_size = font,
    #         background_color = color[2])
    #     self.ep_input.bind(focus=self.on_focus,
    #         on_text_validate=self.on_enter,
    #         text=self.on_text)

    #     btn_rtn = Button(text='Remove',
    #         font_size = font/2,
    #         background_color = color[1],
    #         color = color[3])
    #     btn_add = Button(text='Add',
    #         font_size = font/2,
    #         background_color = color[1],
    #         color = color[3],
    #         size_hint_x = 0.7)
    #     self.btn_rand = Button(text='Roll the\nDice!',
    #         font_size = font/2,
    #         halign = 'center',
    #         background_color = color[1],
    #         color = color[3])
    #     # btn_stop = Button(text='Exit',
    #     #     font_size = font,
    #     #     background_color = color[1],
    #     #     color = color[3],)
    #     #     size_hint_y = 0.4)
    #     btn_rtn.bind(on_press=self.btn_rtn_press)
    #     btn_add.bind(on_press=self.btn_add_press)
    #     self.btn_rand.bind(on_press=self.btn_rand_press)
    #     # btn_stop.bind(on_press=self.btn_stop_press)

    #     layout_main = BoxLayout(orientation = 'vertical')
    #     layout_icons = BoxLayout(orientation = 'vertical',
    #         spacing = size_x/10)
        
    #     layout_box = BoxLayout(orientation = 'vertical',
    #         padding = [font*0.6, 0, font*0.6, font*0.6],
    #         spacing = font/2)
    #     layout_row_2 = BoxLayout(orientation = 'horizontal',
    #         spacing = font/2,
    #         size_hint_y = 0.5)
    #     layout_anch = AnchorLayout(anchor_x = 'right',
    #         anchor_y = 'top',
    #         size_hint_y = 0.3,
    #         padding = [0, font/2, 0, 0])

    #     # layout_icons.add_widget(icon_close)
    #     # layout_icons.add_widget(icon_reboot)
    #     layout_anch.add_widget(icon_close)
    #     layout_row_2.add_widget(btn_rtn)
    #     layout_row_2.add_widget(btn_add)

    #     layout_box.add_widget(self.ep_label)
    #     layout_box.add_widget(self.ep_input)
    #     layout_box.add_widget(layout_row_2)
    #     layout_box.add_widget(self.btn_rand)
    #     # layout_box.add_widget(btn_stop)
    #     layout_main.add_widget(layout_anch)
    #     layout_main.add_widget(layout_box)

    #     self.ep_label.font_size = font/2
    #     self.ep_label.text = rand.clean()
    #     return layout_main

    # def __init__(self):
    #     self.state_add = False
    #     self.state_rtn = False

    def btn_rtn_press(self):
        # if self.ids.btn_rtn.state == 'normal':
        #     print('down')
        # else:
        #     print('normal')
        try:
            int(self.ids.ep_input.text)
            self.ids.ep_label.font_size = font/2
            self.ids.ep_label.text = rand.remove(self.ids.ep_input.text)
        except ValueError:
            print('rtn')
        finally:
            self.ids.ep_input.text = ''

    def btn_add_press(self): 
        # if not value == 'normal':
        #     print('down')
        # else:
        #     print('normal')
        try:
            int(self.ids.ep_input.text)
            self.ids.ep_label.font_size = font/2
            self.ids.ep_label.text = rand.add(self.ids.ep_input.text)
            self.ids.ep_input.text = ''
        except ValueError:
            print('add')
        finally:
            self.ids.ep_input.text = ''

    def btn_rand_press(self):
        self.ids.ep_label.font_size = font*3
        self.ids.ep_label.text, reset_state = rand.run()
        if reset_state:
            # self.btn_rand.text = 'Сброс\nсписок'
            self.ids.ep_label.font_size = font/2
            msg = rand.reset_list()
            self.ids.ep_label.text = msg
        self.ids.ep_input.text = ''

    def btn_stop_press(self, *largs):
        print('====Exit====')
        rand.save_data()
        app.get_running_app().stop()


    def on_focus(self, instance, value):
        print('Focus')
        return

    def on_text(self):
        print(self.ids.ep_input.text)
        return

    def on_enter(self):
        if self.ids.btn_rtn.state == 'down':
            print('rtn!!')
            self.btn_rtn_press()
        elif self.ids.btn_add.state == 'down':
            print('Add!!')
            self.btn_add_press()          
        else:
            print('No btts')
            return
        print(f'User entered {self.ids.ep_input.text}')
        self.ids.ep_input.text = ''
        # self.ids.ep_label.text, self.ids.ep_input.text = self.ids.ep_input.text, ''
        return
    
    def on_stop(self):
        print('====Exit====')

class RandEpApp(App):
    def build(self):
        icon: '123.png'
        return AppGrid()
    
if __name__ == '__main__':
    rand = Randomiser()
    app = RandEpApp()
    app.run()