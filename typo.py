import curses
import os
import sys

class Typo:
   """
   Typo object
   """
   def __init__(self):
      self.screen = curses.initscr()
      self.height, self.width = self.screen.getmaxyx()
      self.screen.addstr("*"*self.width)
      self.screen.refresh()
      end_character = ""
      while '^C' not in end_character:
         self.screen.getch()
   
   def __del__(self):
      curses.endwin()