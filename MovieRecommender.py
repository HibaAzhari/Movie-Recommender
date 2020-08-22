import kivy
kivy.require('1.11.1')
import setup
from setup import Setup
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import  Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

Window.minimum_width, Window.minimum_height = (800, 600)

""" 
    Code for movie recommender system (production system)
    Works with either backward or forward chaining
    Takes user input and recommends accordingly

 """ 


class UI(App):
    def build(self):
        movieRecommender = Setup().system
        class StartScreen(Screen):
            pass
        class Q1(Screen):
            pass
        class Q2(Screen):
            pass
        class Q3(Screen):
            pass
        class Q4(Screen):
            pass
        class result(Screen):
            recommendation = StringProperty("")
        class pick(Screen):
            pass
        class confirm(Screen):
            attribute = StringProperty("____")
        class final(Screen):
            pass
        class goodMovie(Screen):
            pass
        class MyScreenManager(ScreenManager):
            def __init__(self,**kwargs):
                super(MyScreenManager,self).__init__(**kwargs)
                self.switchToStart()
            def switchToStart(self):
                movieRecommender.reset()
                self.current = 'start'          
            def cont(self,no):
                if no in (1,2):
                    if no == 1:
                        movieRecommender.fire(setup.light)
                    elif no == 2:
                        movieRecommender.fire(setup.intense)
                    self.current = 'Q2'
                elif no in (3,4):
                    if no == 3:
                        movieRecommender.fire(setup.before2010)
                    elif no == 4:
                        movieRecommender.fire(setup.after2010)
                    self.current = 'Q3'
                elif no in (5,6):
                    if no == 5:
                        movieRecommender.fire(setup.under2hrs)
                    elif no == 6:
                        movieRecommender.fire(setup.over2hrs)
                    self.current = 'Q4'
                elif no in (7,8):
                    if no == 7:
                        movieRecommender.fire(setup.american)
                    elif no == 8:
                        movieRecommender.fire(setup.intl)
                    
                    movieRecommender.recommend()
                    self.getRecommendation()
                    self.current = 'result'
            def getRecommendation(self):
                self.get_screen('result').recommendation = movieRecommender.recommendation
            def pick(self,no):
                movieRecommender.backward(setup.movies[no-1])
                self.get_screen('confirm').attribute = movieRecommender.movieData.pop().desc
                self.current = 'confirm'
            def conf(self,response):
                if response == 0:
                    self.current = 'final'
                elif len(movieRecommender.movieData) > 0:
                    self.get_screen('confirm').attribute = movieRecommender.movieData.pop().desc
                else:
                    self.current = 'goodMovie'
        return MyScreenManager()
    
         

if __name__ =='__main__':
    UI().run()