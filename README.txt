This archive contains the following files:  KJV-PCE-TSK.db, kjv_cmdline.py, 
TEXT-PCE-127.txt, TEXT-PCE.txt, TEXT-PCE.diff and this README.txt file.

KJV-PCE-TSK.db is an SQlite3 database containing the KJV Bible.  

Please note, that this database is not readable with SQLite2.  If you need to 
convert it to SQLite2,then please see the information at:
http://www.sqlite.org/version3.html for instructions.

kjv_cmdline.py is the Python 2.7x program that reads in the bible
database and allows for various search operations of the text. 

This database was created from the included TEXT-PCE-127.txt file.  This is my 
version of the TEXT-PCE.txt file obtained from:  http://www.bibleprotector.com.  
The difference being that the file from the website is not a pure ASCII non-
extended code file in that it uses two characters from the extended ASCII 
character set, decimal codes 146 and 151.  146 is used 1997 times in the text as 
an apostrophe and 151 is used once in Exodus 32:32 as the long dash character.  
These are actually fine and used in printed bibles, but their use as ASCII text 
for consumption by a computer program makes the coding unnecessarily complicated.   
So, I have replaced all instances of code 146 with the more commonly used code 
39, the single quote, for the apostrophe and two of code 45, the hyphen as "--", 
to represent the double dash which is also commonly used for the long dash.  This 
is commonly done in many purely ASCII bible text files and even some printings so 
I have followed this convention here.  I do not believe the TEXT-PCE.txt file as 
I received it to be in any error.  This is strictly done to cause the text to 
conform to the printable ASCII character set represented by decimal codes 32-127.  
A table of the ASCII control characters, printable characters and extended codes 
may be found at www.ascii-code.com.

To be certain that in substituting the apostrophe characters and long dash 
character I have not accidentally introduced any other changes, I compared the 
two files, TEXT-PCE.txt and TEXT-PCE-127.txt with the Unix diff utility.  TEXT-
PCE.diff is the output of this comparison process and show precisely what changes 
were made and that they were limited to the changes I have described.

I hereby release the Python code file kjv_cmdline.py, the SQLite3 database file 
KJV-PCE-TSK.db, TEXT-PCE.diff, TEXT-PCE-127.txt, and this README.txt file
under the MIT License. Please see LICENSE.txt for more details

Bill Allen 
wallenpb at gmail dot com
April 23, 2012

