import curses
import os
import sys

class Typo:
   """
   Typo object
   """
   def __init__(self):
      self.origin_y, self.origin_x = (0, 0)
      self.cmd_h, self.cmd_w = (0, 0)
      curses.wrapper(self.entry_point)
   
   def entry_point(self, stdscr):
      # Clear the screen
      stdscr.clear()

      # Dimensions of the terminal window
      self.cmd_h, self.cmd_w = stdscr.getmaxyx()
      
      # Adding the title bar for the application
      stdscr.addstr(self.origin_y, self.origin_x, " TYPO ".center(self.cmd_w, '-'))
      stdscr.refresh()
      if len(sys.argv) > 1: stdscr.addstr(1,  self.origin_x, sys.argv[0].center(self.cmd_w,' '))
      else: stdscr.addstr(self.origin_y+1, self.origin_x, " New Buffer ".center(self.cmd_w, ' '))
      stdscr.refresh()
      stdscr.addstr(self.origin_y+2, self.origin_x, '-'*self.cmd_w)
      stdscr.refresh()

      # Adding the main screen where the editing should take place
      h = self.cmd_h - 3; w = self.cmd_w
      win = curses.newwin(self.cmd_h - 3, self.cmd_w, self.origin_y+3, self.origin_x)
      win.refresh()
      stdscr.refresh() # Adding the main screen to the overall window

      # Add the bottom bar where options for important file operations (saving, exiting the application, etc.) are displayed here
      command_bar = curses.newwin(self.cmd_h - h, self.cmd_w, self.cmd_h - 3, 0)
      command_bar.addstr(0,0, "^0 = save file")
      command_bar.addstr(1,0, "^X = exit Typo")
      command_bar.refresh()
      stdscr.refresh()

      # Program exists when any key is entered
      # MUST MODIFY THIS TO EXIT ONLY WHEN THE USER ENTERS '^O' OR '^X'
      stdscr.getkey()