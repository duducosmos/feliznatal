import time
import curses

tree0 = lambda n : [ " " *(n- i)+ "*" * (2 * i + 1) +"\n"  for i in range(n)]

tree1 = lambda n : [ " " *(n- i)+ "@" * (2 * i + 1) +"\n"  for i in range(n)]

arvore = lambda n, tree:  "".join(tree(n)) + (n-1) *" "+ "| |\n" +(n-5) *" "+	 "Feliz Natal"

i = 1
t0 = arvore(30, tree0)
t1 = arvore(30, tree1)

stdscr = curses.initscr()

time.sleep(5)

while True:
	stdscr.clear()
	if i % 2 == 0:
		tmp = t0
	else:
		tmp = t1
		
	try:
		stdscr.addstr(tmp)
		stdscr.refresh()
	except:
		pass
		
	time.sleep(0.5)
	i += 1
