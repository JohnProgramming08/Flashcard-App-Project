import sqlite3

# Connect to the database
connection = sqlite3.connect("revision_app.db")
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS flashcards(
                  question_text TEXT PRIMARY KEY,
                  question_answer TEXT,
                  marks INTEGER,
                  subtopic TEXT)"""
cursor.execute(create_table)
connection.commit()

# Add all of the questions to the database
def add_question(question):
  cursor.execute("INSERT INTO flashcards (question_text, question_answer, marks, subtopic) VALUES (?, ?, ?, ?)", (question[0], question[1], question[2], question[3]))
  connection.commit()

questions = [["What is the purpose of the CPU?", "To complete the fetch-execute cycle.", 1, "1.1.1 CPU architecture"], 
             ["Give 4 common CPU components.", "Arithmetic Logic Unit, Control Unit, Cache, Registers.", 2, "1.1.1 CPU architecture"],
             ["Name 4 registers commonly found in the CPU", "Program counter, Accumulator, Memory address register, Memory data register.", 2, "1.1.1 CPU architecture"],
             ["What happens to the CPUs performance is the clock speed increases?", "The CPU will be faster.", 1, "1.1.2 CPU performance"],
             ["What happens to the clock speed if the number of cores doubles?", "The clock speed will double.", 2, "1.1.2 CPU performance"],
             ["What does the cache do?", "Stores frequently used instructions and data.", 2, "1.1.2 CPU performance"],
             ["What is an embedded system?", "A small electrical system within a larger system.", 1,"1.1.3 Embedded systems"],
             ["Give 3 chaacteristics of embedded systems?", "Small range of tasks, Low level programming language, Minimal user interface.", 2, "1.1.3 Embedded systems"],
             ["Give an example of an embedded system.", "Domestic appliances such as digital thermometers and washing machines.", 1, "1.1.3 Embedded systems"],
             ["What is primary storage used for?", "To store data and instructions that are currently being processed.", 1, "1.2.1 Primary storage"], 
             ["What is the difference between RAM and ROM?", "RAM is volatile, ROM is non-volatile.", 2, "1.2.1 Primary storage"],
             ["What is virtual memory?", "A type of secondary storage that is used to store data and instructions that are currently being processed.", 1,"1.2.1 Primary storage"], 
             ["Name 3 secondary storage devices.", "Solid state drive, Magnetic, Optical.", 3, "1.2.2 Secondary storage"], 
             ["Order the following in descending capacity capability: Magnetic, Solid state, Optical.", "Magnetic, Solid state, Optical.", 3, "1.2.2 Secondary storage"],
             ["Why are solid state drives used in smartphones?", "They are robust, fast and reliable due to no moving parts.", 2, "1.2.2 Secondary storage"], 
             ["Order these units in ascending size: Gigabyte, Kilobyte, Petabyte, Nibble.", "Nibble, Kilobyte, Megabyte, Gigabyte.", 2, "1.2.3 Units of storage"], 
             ["What is the formula for sound file size?", "file size = sample rate x bit depth x duration.", 1, "1.2.3 Units of storage"], 
             ["How many bytes are in a gigabyte?", "There are 1,000,000,000 bytes in a gigabyte.", 1, "1.2.3 Units of storage"], 
             ["What is F7 in binary?", "11110111.", 1, "1.2.4 Data storage"], 
             ["Define the term: 'character set'.", "A defined list of characters that are recognised and can be stored in a computer system.", 2, "1.2.4 Data storage"],
             ["Define the term: 'metadata'.", "A set of data that describes and gives information about other data.", 1, "1.2.4 Data storage"], 
             ["What is lossy compression?", "An the data in a file is removed and not restored to its original form after decompression.", 1, "1.2.5 Compression"], 
             ["What type of compression would be used on a text file?", "Lossless compression.", 1, "1.2.5 Compression"], 
             ["What type of compression would be used on an image file?", "Lossy compression.", 1, "1.2.5 Compression"], 
             ["Define a WAN.", "A network that covers a large geographical area.", 1, "1.3.1 Networks and topologies"], 
             ["What happens to a network if the bandwidth increases?", "The network performance will increase.", 2, "1.3.1 Networks and topologies"],
             ["What happens to a network if the number of devices increases?", "The network performance will decrease.", 2, "1.3.1 Networks and topologies"],
             ["What does HTTP stand for?", "HyperText Transfer Protocol.", 1, "1.3.2 Networks, protocols and layers"], 
             ["What is encryption?", "The process of scrambling data so that it cannot be read by unauthorised parties.", 2, "1.3.2 Networks, protocols and layers"], 
             ["What is a protocol?", "A set of rules that define how data is transferred between devices.", 1, "1.3.2 Networks, protocols and layers"], 
             ["What is malware?", "Software that is designed with malicious intent.", 1, "1.4.1 Threats to computer systems"],
             ["Describe how a DOS attack works.", "Flooding a system with too many requests, causing it to crash.", 2, "1.4.1 Threats to computer systems"], 
             ["What is the term that describes using SQL to hack a site?", "SQL injection.", 1, "1.4.1 Threats to computer systems"],
             ["Define user access levels.", "Each user only has access to fata that they need.", 1, "1.4.2 Identifying and preventing vulnerabilities"], 
             ["Is the following password strong? 'password'", "No because it is too easy to guess due to its popularity.", 2, "1.4.2 Identifying and preventing vulnerabilities"],
             ["What type of hacker would perform penetration testing?","A white hat hacker.", 1, "1.4.2 Identifying and preventing vulnerabilities"], 
             ["What is multitasking in operating systems?", "Multiple programs running at the same time.", 1, "1.5.1 Operating systems"],
             ["Why is file management important in an OS?", "So that the user can easily access files.", 1, "1.5.1 Operating systems"],
             ["Define peripheral management.","The process of managing hardware devices external to the computer.", 2, "1.5.1 Operating systems"], 
             ["Why is encryption software important?", "To protect data from unauthorised access.", 1, "1.5.2 Utility software"],
             ["What is defragmentation?", "The process of rearranging files on a hard drive so that they are in the correct order.", 2, "1.5.2 Utility software"],
             ["Define utilty software.", "Software designed to help maintain / optimise a computer system.", 1, "1.5.2 Utility software"], 
             ["Is open source software always free?","Yes, it is always free to use.", 1, "1.6.1 Impacts of technology"], 
             ["Is stealing a computer against the computer misuse act?", "No as you are not necessarily gaining access to the computers data.", 2, "1.6.1 Impacts of technology"],
             ["What law does developing malware break?", "The Computer Misuse Act.", 1, "1.6.1 Impacts of technology"],
             ["What is abstraction?", "The process of removing unnecessary detail from a problem.", 1, "2.1.1 Computational thinking"],
             ["What is decomposition?", "Breaking down a problem into smaller sub-problems.", 1, "2.1.1 Computational thinking"], 
             ["Why is decomposition important?","To make a large problem easier to solve and less intimidating.", 1, "2.1.1 Computational thinking"],
             ["What is a flowchart?", "A diagram that shows the steps in a program.", 1, "2.1.2 Designing algorithms"],
             ["What is psudocode?", "Code that is more readable but doesnt run.", 2, "2.1.2 Designing algorithms"],
             ["Why use a trace table?", "To allow programmers to trace the value of variables as each line of code is executed.", 1, "2.1.2 Designing algorithms"],
             ["Which is faster: bubble sort or merge sort?", "Merge sort.", 1, "2.1.3 Searching and sorting algorithms"],
             ["Which is faster: linear search or binary search?", "Binary search.", 1, "2.1.3 Searching and sorting algorithms"],
             ["Give a disadvantage of binary search.","It requires data to be sorted.", 2, "2.1.3 Searching and sorting algorithms"],
             ["What is iteration?", "Repeating a section of code.", 1, "2.2.1 Programming fundamentals"],
             ["What does '<=' mean?", "Less than or equal to.", 1, "2.2.1 Programming fundamentals"],
             ["What is an if statement an example of?", "Selection.", 1, "2.2.1 Programming fundamentals"],
             ["Define an integer.", "A whole number.", 1, "2.2.2 Data types"],
             ["What is a float?", "A decimal number.", 1, "2.2.2 Data types"],
             ["What data type is True?", "Boolean.", 1, "2.2.2 Data types"],
             ["What is a 2d array?","An array that contains arrays.", 1, "2.2.3 Programming techniques"],
             ["Which library is imported to allow for random numbers?", "'random'.", 1, "2.2.3 Programming techniques"],
             ["How do you open a text file?", "file = open('filename.txt', 'r').", 1, "2.2.3 Programming techniques"],
             ["What is authentication?","The process of verifying that a user is who they say they are.", 1, "2.3.1 Defensive design"],
             ["Why is commenting important?", "To make code easier to understand.", 1, "2.3.1 Defensive design"],
             ["What are biometrics an example of?", "Authentication.", 1, "2.3.1 Defensive design"],
             ["What is iterative testing?", "Testing a program as it is written.", 1, "2.3.2 Testing"],
             ["What is final testing?", "Testing a program after it has been completed.", 1, "2.3.2 Testing"],
             ["Define syntax error.", "An error in the code that prevents it from running.", 1, "2.3.2 Testing"],
             ["What is the result of 1 AND 0?", "0.", 1, "2.4.1 Boolean logic"],
             ["What is the result of 1 OR 0?", "1.", 1, "2.4.1 Boolean logic"],
             ["What is the result of NOT 0?", "1.", 1, "2.4.1 Boolean logic"],
             ["What is a high level language?", "A language that is easier for humans to understand but further from the hardware.", 1, "2.5.1 Languages"],
             ["What is machine code?", "The code that a computer understands (binary).", 1, "2.5.1 Languages"],
             ["Why are translators important?", "To convert code to machine code.", 1, "2.5.1 Languages"],
             ["What is an IDE?","An Integrated Development Environment that code can be written in.", 1, "2.5.2 IDEs"],
             ["Why is syntax highlighting usefull?", "To make code easier to read.", 1, "2.5.2 IDEs"],
             ["Why are error diagnostics important?", "To help programmers with debugging.", 1, "2.5.2 IDEs"]]
             
for i in questions:
  add_question(i)

connection.close()