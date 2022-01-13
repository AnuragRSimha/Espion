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


https://user-images.githubusercontent.com/53004679/149343971-fd6909cf-69c2-4a5c-b119-101f07ae1a53.mp4


### Part B: After cloning the repository
Before proceeding, be certain to be a super user (root) to use Espion. Also install the keyboard module in python [`pip install keyboard`].
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

![Designating the machines](https://i.ibb.co/DpY9VGJ/Attacker-Victim.jpg)


https://user-images.githubusercontent.com/53004679/149384965-7a17cf9d-c533-4c15-80d6-69541743fed5.mp4


### Contents of the keylogger file
![Contents of the keylogger file](https://user-images.githubusercontent.com/53004679/149384403-47b8eeab-289c-48a7-a194-b44775c7c947.PNG)

Since the shift key was pressed for a long duration, the duplicate entries are perspicuous.

## Uses
1. Monitor user activity on a local network.
2. Record usernames and passwords (for legal purposes only).

## Additional Information
1. Designed and developed by Anurag.R.Simha.
2. Made in Karnataka.
3. Designed with python.
4. Concept(s) used: Socket Programming in Python.

## Notice
Espion is not OS-specific.

All the details are stored in a keystroke log file on the same directory
where espion.py program was running. Remember to terminate the execution
of that program before browsing the log file. It's titled as 
'Keystroke log file (current date).txt'.

## Consequences of Illegal/Unauthorised Use
Only a few points are listed here:
### The Indian Law
As per the Indian law, the accused can also be jailed under the following (suitable) sections:
#### IT ACT
1. Sec. 73: Publishing False Digital Signature Certificates.
2. Sec. 65: Tampering with Computer Source Documents.
3. Sec. 72: Breach of Confidentiality and Privacy.

#### IPC (Indian Penal Code)
1. Sec. 463: Forgery of Electronic Records.
2. Sec. 420: Bogus Websites & Cyber Fraud.

### The British Law
The cyber security laws that are normally applied in case of cyber attacks are as follows (as per the British law):
1. The Privacy and Electronic Communications Regulations 2003 (PECR)
2. Computer Misuse Act 1990 (CMA)
4. Investigatory powers Act 2016 (IPA)
5. Fraud Act 2006
6. Theft Act 1968
7. Theft Act 1978
8. Forgery and Counterfeiting Act 1981
9. Proceeds of crime act 2002 (POCA)
10. Data protection act 2018 (DPA)
11. Official Secrets Act 1989

