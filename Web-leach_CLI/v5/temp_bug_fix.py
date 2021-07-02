
import curses

from math import acos
from threading import Thread
from random import choice
from time import sleep
from queue import Queue, Empty


commandQueue = Queue()

stdscr = curses.initscr()
stdscr.keypad(True)

upperwin = stdscr.subwin(2, 80, 0, 0)
lowerwin = stdscr.subwin(2,0)

def outputThreadFunc():
    outputs = ["So this is another output","Yet another output","Is this even working"] # Just for demo
    while True:
        upperwin.clear()
        upperwin.addstr(f"{choice(outputs)}")
        try:
            inp = commandQueue.get(timeout=0.1)
            if inp == 'exit':
                return
            else:
                upperwin.addch('\n')
                upperwin.addstr(inp)
        except Empty:
            pass

        upperwin.refresh()
        sleep(1)
        


def inputThreadFunc():
    while True:
        global buffer

        lowerwin.addstr("->")

        command = lowerwin.getstr()

        if command:
            command = command.decode("utf-8")
            commandQueue.put(command)
            lowerwin.clear()

            lowerwin.refresh()
            if command == 'exit':
                return

            
        


# MAIN CODE
outputThread = Thread(target=outputThreadFunc)
inputThread = Thread(target=inputThreadFunc)
outputThread.start()
inputThread.start()
outputThread.join()
inputThread.join()

stdscr.keypad(False)
curses.endwin()
print("Exit")

