import curses
import os
import sys

def typo(stdscr):
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

def main():
   # The curses.wrapper() function takes a callable object and does the
   # necessary initializations. curses.wrapper() then runs your provided callable
   # Once the callable returns, curses.wrapper() will restore the
   # original state of the terminal
   curses.wrapper(typo)

if __name__ == "__main__":
   main()
