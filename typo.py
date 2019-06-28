import curses
import os
import sys

class Typo:
   """
   Typo object
   """
   def __init__(self):
      curses.wrapper(self.entry_point)
   
   def entry_point(self, stdscr):
      # Clear the screen
      stdscr.clear()

      cmd_h, cmd_w = stdscr.getmaxyx()
      stdscr.addstr(0,0, " TYPO ".center(cmd_w, '-'))
      stdscr.refresh()
      if len(sys.argv) > 1: stdscr.addstr(1,0, sys.argv[0].center(cmd_w,' '))
      else: stdscr.addstr(1,0, " New Buffer ".center(cmd_w, ' '))
      stdscr.refresh()
      stdscr.addstr(2,0, '-'*cmd_w)
      stdscr.refresh()

      x = 0; y = 3
      h = cmd_h - 3; w = cmd_w
      win = curses.newwin(cmd_h - 3, cmd_w, 3, 0)
      win.refresh()

      stdscr.refresh() # Adding the text to the screen

      command_bar = curses.newwin(cmd_h - h, cmd_w, cmd_h - 3, 0)
      command_bar.addstr(0,0, "^0 = save file")
      command_bar.addstr(1,0, "^X = exit Typo")
      command_bar.refresh()

      stdscr.refresh()
      stdscr.getkey()