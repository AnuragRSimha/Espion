# Espion: A Mini-Keylogger
![Espion: A Mini-Keylogger](https://i.ibb.co/VQr8J8S/Logo.jpg)
## Warning
The use of this tool is strictly for only benevolent or educational purposes. Any malevolent intention or misuse of Espion could certainly put your life at risk. Henceforth, use this tool cautiously.
## Introduction
### About Espion
Espion (Spy in French) is a bijou keylogger tool to capture any key that the user on a target machine presses on his/her keyboard. Espion supports 1:M connection. 1:M is a notation for one server and many clients.
### About Keyloggers
Keyloggers are spyware tools (hence the name, Espion) that capture 'keystrokes' on a target computer and reflect the captured data in real-time and/or keep it stored in a log file.
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
2. On the attacker machine, run the generator program first (`python generator.py`).
3. Enter all the details asked for into the prompt.
4. Remember the IP address and the port number that's designated.
5. Once again, on the attacker machine, run the listener program (`python espion.py <IP> <PORT>`).
6. Now, head to the victim machine.
7. Run the program titled 'victim.py' on the victim machine (`python victim.py`).
8. Type anything on the target machine(s). Then monitor/observe the output received on the attacker machine
(Optional: Connect another victim to the attacker machine.).
## Additional Information
1. Designed and developed by Anurag.R.Simha.
2. Made in Karnataka.
3. Designed with python.
4. Concept(s) used: Socket Programming in Python,

## Notice
Espion is not OS-specific.

All the details are stored in a keystroke log file on the same directory
where espion.py program was running. Remember to terminate the execution
of that program before browsing the log file. It's titled as 
'Keystroke log file (current date).txt'.
