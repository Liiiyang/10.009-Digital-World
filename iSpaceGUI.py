from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button 
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder
from kivy.graphics import Rectangle
from firebase import firebase

import time

token="P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z"
url="https://my-awesome-project-2fdd3.firebaseio.com/"
firebase=firebase.FirebaseApplication(url,token)

class MyLabel(Label):
    def __init__(self,**kwargs):
        Label.__init__(self,**kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding=(20,20)

class ShowClock(Label):
    def update(self, *args):
        self.text = time.asctime()

class StartScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        self.title=BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 0.6})
        self.btn=BoxLayout(size_hint=(None, None), height=50, pos_hint={'top': 0.5})
        self.quit = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'right': 1})
        title = MyLabel(text="iSpace",color=(1,1,1,1),font_size=24,halign='center',valign='middle')
        self.title.add_widget(title)
        btn_settings = Button(text="Start",on_press=self.change_to_loading, font_size=24)
        self.btn.add_widget(btn_settings)
        btn_quit = Button(text="Quit",on_press=self.quit_app,font_size=24)
        self.quit.add_widget(btn_quit)
        self.add_widget(self.title)
        self.add_widget(self.btn)
        self.bind(center=self.btn.setter('center'))
        self.add_widget(self.quit)

    def change_to_loading(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current= 'loadingscreen'
        # Simulate the searching of the user's car through gps
        self.pb = ProgressBar(max = 500)
        Clock.schedule_interval(self.heavyFunc,1/60.)
        progress_bar = Popup(title = 'Searching Your Car...Please Wait...', content=self.pb, size_hint= (0.7,0.3))
        progress_bar.open()
        progress_bar.bind(on_open=self.dismiss_pg)
    
    # Sets the timing for the progress bar to load
    def heavyFunc(self, dt):
        self.pb.value += 1
        print self.pb.value
        if self.pb.value >= 500:
            Clock.unschedule(self.heavyFunc)
            # Tells the user that the search is complete and allows the user to go to the menu screen to choose parking space
            btn_to_menu = Button(text ="Find a Parking Space", on_press= self.change_to_menu, size_hint=(0.5,0.5))
            msg = Popup(title = 'Search Complete. Car Detected in SUTD', content = btn_to_menu,size_hint= (0.7,0.3))
            msg.open()
            msg.bind(on_open=self.dismiss_msg)

    # Removes the popup after the progress bar is done
    def dismiss_pg(self,instance):
        Clock.schedule_once(instance.dismiss,9)
    # Removes the popup after the user is taken to the menu screen
    def dismiss_msg(self,instance):
        Clock.schedule_once(instance.dismiss,1.5)

    def change_to_menu(self,value):
        self.manager.transition.direction = 'left'
        self.manager.current= 'menu'
                
    def quit_app(self, value):
        App.get_running_app().stop()

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        #self.background = Image(source='ParkingLot1.png')
        #self.add_widget(self.background)


# Allows the User to select the feeds that he wants to see and choose the slot that he wants his car to park at 
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        self.title_time = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})
        self.title = BoxLayout(size_hint=(1,0.2), height=50, pos_hint={'top': 1})
        self.area = BoxLayout(size_hint=(1,0.2), height=50, pos_hint={'top': 0.95})
        self.feed_selection = BoxLayout(size_hint=(1,0.1), height=50, pos_hint={'top': 0.80})
        self.quit = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'right': 1})
        theclock = ShowClock()
        Clock.schedule_interval(theclock.update, 1)
        self.title_time.add_widget(theclock)
        label1 = Label(text="SUTD")
        self.title.add_widget(label1)
        choose_area=Label(text="Choose Area")
        self.area.add_widget(choose_area)
        feed1=Button(text='Area One',on_press=self.change_to_area_one,font_size= 15)
        self.feed_selection.add_widget(feed1)
        feed2=Button(text='Area Two',on_press=self.change_to_area_two,font_size=15)
        self.feed_selection.add_widget(feed2)
        btn_quit = Button(text="Quit",on_press=self.quit_app,font_size=24)
        self.quit.add_widget(btn_quit)
        self.add_widget(self.title_time)
        self.add_widget(self.title)
        self.add_widget(self.area)
        self.add_widget(self.quit)
        self.add_widget(self.feed_selection)


    def change_to_area_one(self,value):
        self.manager.transition.direction = 'left'
        self.manager.current= 'areaone'

    def change_to_area_two(self,value):
        self.manager.transition.direction = 'left'
        self.manager.current= 'areatwo'

    def quit_app(self, value):
        App.get_running_app().stop()


 
class AreaOne(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #Window.clearcolor = (0.2, 0.2, 0.2, 1)
        self.title_time = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})
        self.title = BoxLayout(size_hint=(1,0.2), height=50, pos_hint={'top': 1})
        self.feed_selection = BoxLayout(size_hint=(1,0.1), height=50, pos_hint={'top': 0.90})
        self.slot_selection = BoxLayout(size_hint=(1,0.1), height=50, pos_hint={'top': 0.85})
        self.slot = FloatLayout()
        self.quit = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'right': 1})
        self.status = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'top':0.4,'right': 0.35})
        self.back = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'left': 1})
        theclock = ShowClock(color=(0,0,0,1))
        Clock.schedule_interval(theclock.update, 1)
        self.title_time.add_widget(theclock)
        label1 = Label(text="SUTD",color=(0,0,0,1))
        self.title.add_widget(label1)
        areaone = Label(text = "Area One",color=(0,0,0,1),size_hint=(1,1))
        self.feed_selection.add_widget(areaone)
        self.view = Button(text='View Feed', on_press=self.view_feed,font_size=15,size_hint = (0.2,0.2),pos=(560,150))
        self.slot.add_widget(self.view)
        self.leave = Button(text='Leave Carpark', on_press=self.leave_carpark,font_size=15,size_hint = (0.2,0.2),pos=(370,150))
        self.slot.add_widget(self.leave)
        slotbutton = Label(text = "Please Choose Your Parking Space",color=(0,0,0,1))
        self.slot_selection.add_widget(slotbutton)
        # Periodically Checks Parking Status and Updates it
        Clock.schedule_interval(self.checkStatus,10)
        change_status = Label(text = "Status: Green = Unoccupied, Red = Occupied")
        self.status.add_widget(change_status)
        btn_back = Button(text="Back",on_press=self.change_to_menu,font_size=24)
        self.back.add_widget(btn_back)
        btn_quit = Button(text="Quit",on_press=self.quit_app,font_size=24)
        with self.canvas:
            self.bg = Rectangle(source='ParkingLot1.png', pos=(0, 0), size=(800, 600))
        self.quit.add_widget(btn_quit)
        self.add_widget(self.title_time)
        self.add_widget(self.title)
        self.add_widget(self.quit)
        self.add_widget(self.feed_selection)
        self.add_widget(self.back)
        self.add_widget(self.slot)
        self.add_widget(self.status)
        self.add_widget(self.slot_selection)

    
    # Updates firebase on the user's decision to park indicated slot 
    def p1_park(self,value):
        firebase.put('/','carpark',1)
        self.p1.background_color = (1,0,0,1)
        Clock.schedule_interval(self.parkfinish, 3)
        Clock.unschedule(self.checkStatus)
        Clock.schedule_interval(self.checkStatus,0.5)
         
         

    def p2_park(self,value):
        firebase.put('/','carpark',2)
        self.p2.background_color = (1,0,0,1)
        Clock.schedule_interval(self.parkfinish, 3)
        Clock.unschedule(self.checkStatus)
        Clock.schedule_interval(self.checkStatus,0.5) 

  
    def p3_park(self,value):
        firebase.put('/','carpark',3)
        self.p3.background_color = (1,0,0,1)
        Clock.schedule_interval(self.parkfinish, 3)
        Clock.unschedule(self.checkStatus)
        Clock.schedule_interval(self.checkStatus,0.5) 


    def p4_park(self,value):
        firebase.put('/','carpark',4)
        self.p4.background_color = (1,0,0,1)
        Clock.schedule_interval(self.parkfinish, 3)
        Clock.unschedule(self.checkStatus)
        Clock.schedule_interval(self.checkStatus,0.5) 

 
    # Informs User that his car is parked
    def parkfinish(self,value):
        if firebase.get('/done') == 'done':
           self.pop = Popup(title= 'Status (Click Anywhere to Dismiss)', content=Label(text='Your Car has been parked.'), size_hint=(None, None), size=(400, 400))
           self.pop.open()
           firebase.put('/','done','!done')

    def leave_carpark(self,value):
        firebase.put('/','carpark','leave')

    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'menu'

    # Allows the User to view a live feed of the carpark
    def view_feed(self,value):
        str = firebase.get('/image')
        fh = open("Feed.png", "wb")
        fh.write(str.decode('base64'))
        fh.close()
        self.cancel = Button(TextInput='Cancel')
        self.pop = Popup(title='View Feed (Click Anywhere to Exit)', content=Image(source="Feed.png"), size_hint=(None, None), size=(400, 400))
        self.pop.open()

    # Change a Button to a Label and disables Button if the slot is occupied while the app is running
    def checkStatus(self,value):
        self.emptyls=firebase.get('/emptylots')
        print self.emptyls
        self.slot = FloatLayout()
        if self.emptyls[0]=='Empty':
            self.p1 = Button(text='P1', font_size = 15, background_color=(0,1,0,1),on_press= self.p1_park,size_hint = (0.2,0.2),pos=(26,300))
            self.slot.add_widget(self.p1)
        elif self.emptyls[0]=='Occupied':
            self.p1 = Button(text='P1', font_size = 15, background_color=(1,0,0,0.5),size_hint = (0.2,0.2),pos=(26,300))
            self.slot.add_widget(self.p1)
            self.p1.disabled = True
            

        if self.emptyls[1]=='Empty':
            self.p2 = Button(text='P2', font_size = 15,background_color=(0,1,0,1),on_press= self.p2_park,size_hint = (0.2,0.2),pos=(225,300))
            self.slot.add_widget(self.p2)
        elif self.emptyls[1]=='Occupied':
            self.p2 = Button(text='P2', font_size = 15,background_color=(1,0,0,0.5),size_hint = (0.2,0.2),pos=(225,300))
            self.slot.add_widget(self.p2)
            self.p2.disabled = True
            

        if self.emptyls[2]=='Empty':
            self.p3 = Button(text='P3', font_size = 15,background_color=(0,1,0,1),on_press= self.p3_park,size_hint = (0.2,0.2),pos=(420,300))
            self.slot.add_widget(self.p3)
        elif self.emptyls[2]=='Occupied':
            self.p3 = Button(text='P3', font_size = 15,background_color=(1,0,0,0.5),size_hint = (0.2,0.2),pos=(420,300))
            self.slot.add_widget(self.p3)
            self.p3.disabled = True
            

        if self.emptyls[3]=='Empty':
            self.p4 = Button(text='P4', font_size = 15, background_color=(0,1,0,1),on_press= self.p4_park,size_hint = (0.2,0.2),pos=(618,300))
            self.slot.add_widget(self.p4)
        elif self.emptyls[3]=='Occupied':
            self.p4 = Button(text='P4', font_size = 15, background_color=(1,0,0,0.5),size_hint = (0.2,0.2),pos=(618,300))
            self.slot.add_widget(self.p4)
            self.p4.disabled = True
            

        self.add_widget(self.slot)

    def quit_app(self, value):
        firebase.put('/','carpark',0)
        App.get_running_app().stop()
        

class AreaTwo(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        self.title_time = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})
        self.title = BoxLayout(size_hint=(1,0.2), height=50, pos_hint={'top': 1})
        self.feed_selection = BoxLayout(size_hint=(1,0.1), height=50, pos_hint={'top': 0.90})
        self.slot_selection = BoxLayout(size_hint=(1,0.1), height=50, pos_hint={'top': 0.85})
        self.slot = FloatLayout()
        self.status = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'top':0.4,'right': 0.35})
        self.quit = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'right': 1})
        self.back = BoxLayout(size_hint=(0.2,0.1), height=50, pos_hint={'left': 1})
        theclock = ShowClock()
        Clock.schedule_interval(theclock.update, 1)
        self.title_time.add_widget(theclock)
        label1 = Label(text="SUTD")
        self.title.add_widget(label1)
        areaone = Label(text = "Area Two", size_hint=(1,1))
        self.feed_selection.add_widget(areaone)
        slotbutton = Label(text = "Please Choose Your Parking Space")
        self.slot_selection.add_widget(slotbutton)
        p1 = Button(text='P1', font_size = 15, background_color=(1,0,0,0.5),size_hint = (0.2,0.2),pos=(20,350))
        self.slot.add_widget(p1)
        p2 = Button(text='P2', font_size = 15,background_color=(0,1,0,0.5), size_hint = (0.2,0.2),pos=(220,350))
        self.slot.add_widget(p2)
        p3 = Button(text='P3', font_size = 15,background_color=(0,1,0,0.5), size_hint = (0.2,0.2),pos=(420,350))
        self.slot.add_widget(p3)
        p4 = Button(text='P4', font_size = 15, background_color=(0,1,0,0.5),size_hint = (0.2,0.2),pos=(620,350))
        self.slot.add_widget(p4)
        p5 = Button(text='P5', font_size = 15, background_color=(0,1,0,0.5),size_hint = (0.2,0.2),pos=(20,200))
        self.slot.add_widget(p5)
        p6 = Button(text='P6', font_size = 15,background_color=(0,1,0,0.5), size_hint = (0.2,0.2),pos=(220,200))
        self.slot.add_widget(p6)
        p7 = Button(text='P7', font_size = 15,background_color=(1,0,0,0.5), size_hint = (0.2,0.2),pos=(420,200))
        self.slot.add_widget(p7)
        p8 = Button(text='P8', font_size = 15, background_color=(0,1,0,0.5),size_hint = (0.2,0.2),pos=(620,200))
        self.slot.add_widget(p8)
        btn_back = Button(text="Back",on_press=self.change_to_menu,font_size=24)
        self.back.add_widget(btn_back)
        btn_quit = Button(text="Quit",on_press=self.quit_app,font_size=24)
        self.quit.add_widget(btn_quit)
        self.view = Button(text='View Feed',font_size=15,size_hint = (0.2,0.2),pos=(260,70))
        self.slot.add_widget(self.view)
        self.add_widget(self.title_time)
        self.add_widget(self.title)
        self.add_widget(self.quit)
        self.add_widget(self.feed_selection)
        self.add_widget(self.back)
        self.add_widget(self.slot)
        self.add_widget(self.slot_selection)


    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= 'menu'

    def quit_app(self, value):
        App.get_running_app().stop()

class ParkingSpaceFinder(App):
    def build(self):
        sm=ScreenManager()
        ss=StartScreen(name='start')
        ls=LoadingScreen(name='loadingscreen')
        ms=MenuScreen(name='menu')
        ao=AreaOne(name='areaone')
        at=AreaTwo(name='areatwo')
        sm.add_widget(ss)
        sm.add_widget(ls)
        sm.add_widget(ms)
        sm.add_widget(ao)
        sm.add_widget(at)
        sm.current='start'
        return sm

if __name__=='__main__':
	ParkingSpaceFinder().run()




