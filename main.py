from kivy.app import App
from request import ConsultaPath
from entry_exit import SettingsTyre
import os.path
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.core.window import Window
Window.size = (430, 350)


class MyTyre(ScreenManager):
  pass

class TyreC(Screen):

  def __init__(self, **kwargs):
    super().__init__()

  def busc(self, *args):
    i = self.ids["cr"].text
    
    if len(i)>= len('21000'):
        y = os.path.exists(f'Bancod/{i}.bd')
     
        if y:
            self.ids["dados_CR"].text = ConsultaPath.seach_bd(int(i))
            self.ids["cr"].text = ''

    else:
        App.get_running_app().root.current = 'cri'

class Log(Screen):
  ...

class Cadastro(Screen):

    def insertd(self, *args):
        y = self.ids["cr"].text
        
        if len(y)>= len('21000'):
            vr = ConsultaPath.new_creat(y)
            l = self.ids["ci"].text
            i = self.ids["cy"].text
            ConsultaPath.inserir(y,l,i)

            self.ids["cr"].text = ''
            self.ids["ci"].text = ''
            self.ids["cy"].text = ''

        else:
            App.get_running_app().root.current = 'cri'
            
class CriBd(Screen):
    ...

class Actions(Screen):
  ...

class Entry_Exit(Screen):
    ...

class Saidap(Screen):
    global l
    l = []

    def criar_l(self, *args):
        verif = self.ids["li"].text
        if verif == '':
            ...
        else:
            k = self.ids["li"].text
            l.append(int(k))
            self.ids["li"].text = '' 

    def criar(self, *args):
        verif = self.ids["os"].text
        if verif == '':
            ...
        else:
            os = self.ids["os"].text
            SettingsTyre.creat_note(os, l)
            self.ids["os"].text = ''

class Entrap(Screen):
    ...

class Atualize(Screen):
    
    def buscr(self,*args):
        y = self.ids["ar"].text

        if len(y) >= len('21000'):
            a = os.path.exists(f'Bancod/{y}.bd')

            if a:
                a = self.ids["ar"].text
                b = self.ids["br"].text
                c = self.ids["cy"].text

                ConsultaPath.inserir(a,b,c)

                self.ids["ar"].text = ''
                self.ids["br"].text = ''
                self.ids["cy"].text = ''
            else:
                ...
        else:
            App.get_running_app().root.current ='cri'
        
class Tyre(App):
  def build(self):
    return MyTyre()

if __name__ == '__main__':
    Tyre().run()
