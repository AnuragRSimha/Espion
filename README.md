# About Espion
## Introduction
Espion (Spy in French) is a bijou keylogger tool to capture any key that the user on a target machine presses on his/her keyboard. Espion supports 1:M connection. 1:M is a notation for one server and many clients.
## Using Espion
Espion is quite an easy tool to use. If you get doubious on how to use it, on the terminal type the following command:
`python espion.py -h` OR `python espion.py --help`.
### Part A: Cloning the repository
Go as per this command flow:
1. `git clone https://github.com/AnuragRSimha/Espion.git`
2. `cd Espion`
### Part B: After cloning the repository
Follow these steps to achieve a triumphant execution:
1. Confirm the victim machine(s) and the attacker machine.
2. On the attacker machine, run the generator program first.\n
	Syntax: `python generator.py`
3. Enter all the details asked for into the prompt.
4. Remember the IP address and the port number that's designated.
5. Once again, on the attacker machine, run the listener program.
	Syntax: `python espion.py <IP> <PORT>`
6. Now, head to the victim machine.
7. Run the program titled 'victim.py' over there (on the victim machine).
	      Syntax: `python victim.py`
(Optional: Connect another victim to the attacker machine.)
8. Type anything on the target machine(s). Then monitor/observe the output received on the attacker machine.
