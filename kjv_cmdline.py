#!/usr/bin/python
from __future__ import print_function
#Python 2x version
import sqlite3
import sys
import os
import textwrap
#adding colorama module support, removes the need for external driver. 09/17/2013
from colorama import init
init()


class bcolors:
	HEADER = '\x1B[0;33;40m'
	OKBLUE = '\x1B[1;34;40m'
	OKGREEN = '\x1B[1;32;40m'
	WARNING = '\x1B[1;33;40m'
	FAIL = '\x1B[1;31;40m'
	ENDC = '\x1B[0m'

##	def disable(self):
##	    self.HEADER = ''
##	    self.OKBLUE = ''
##	    self.OKGREEN = ''
##	    self.WARNING = ''
##	    self.FAIL = ''
##	    self.ENDC = ''


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def search_words(text, search):
    new_search = []
    for i in search:
        new_search.append(i.lower())
    
    text = text.lower().replace('[','').replace(']','').replace(';','').replace(':','').replace(',','').replace('.','').split(' ')
    return(set(new_search).intersection(set(text)) == set(new_search))


def Show_Verse_Reference(search_ref):
    search_elms = search_ref.replace(':',' ').split(' ')
    if (len(search_elms) == 3) and (search_elms[0] in bible_abr):
        cur.execute("SELECT * FROM Bible where BookAbr=? and Chapter=? and Verse=?",(search_elms[0],search_elms[1],search_elms[2]))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            else:
                if TSK_toggle == False:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]
                elif TSK_toggle ==True:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]+bcolors.OKGREEN+" TSK>"+row[6]+bcolors.ENDC
                new_text = textwrap.fill(verse_text,60)
                print(new_text)
    elif ' '.join(search_elms[:-2]) in bible_books:
        book_x = ' '.join(search_elms[:-2])
        chap_x = search_elms[-2:][0]
        vers_x = search_elms[-2:][1]
        cur.execute("SELECT * FROM Bible where BookName=? and Chapter=? and Verse=?",(book_x,chap_x,vers_x))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            else:
                if TSK_toggle == False:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]
                elif TSK_toggle ==True:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]+bcolors.OKGREEN+" TSK>"+row[6]+bcolors.ENDC
                new_text = textwrap.fill(verse_text,60)
                print(new_text)

def Show_Verse_Word(search_word, BOOK_ans):
    if search_word in ('',' '):
     #   continue
        return
    else:
        if OT_toggle == True:
            cur.execute("SELECT * FROM Bible WHERE BookID in ('1','2','3','4','5','6','7','8','9',\
                        '10','11','12','13','14','15','16','17','18','19','20','21','22','23','24',\
                        '25','26','27','28','29','30','31','32','33','34','35','36','37','38','39')")
        elif NT_toggle == True:
            cur.execute("SELECT * FROM Bible WHERE BookID in ('40','41','42','43','44','45','46','47','48','49',\
                        '50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66')")
        else:
            cur.execute("SELECT * FROM Bible")
        if BOOK_toggle == True:
            while True:
                if ((BOOK_ans in bible_abr) or (BOOK_ans in bible_books)):
                    cur.execute("SELECT * FROM Bible where BookAbr=? or BookName=?",(BOOK_ans, BOOK_ans))
                    break
                else:
                    clear_screen()
                    BOOK_ans = raw_input("INVALID book name or abreviation, try again!  ")
                    
        if BOOK_toggle == True and ((BOOK_ans in bible_abr) or (BOOK_ans in bible_books)):
            cur.execute("SELECT * FROM Bible where BookAbr=? or BookName=?",(BOOK_ans, BOOK_ans))
            
        refs = ''
        count = 0
        while True:
            verse_text = ''
            new_text = ''
            row = cur.fetchone()
            if row == None:
                break
            elif search_word[:1] == "+" and search_word[1:] in row[5]:
                search_word = search_word.strip("+")
                count += 1
                if count % 5 == 0:
                    key_press = raw_input("Press <ENTER> to continue...")
                    if key_press in ('x','X'):
                        clear_screen()
                        key_press = ''
                        break
                if TSK_toggle == False:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]
                elif TSK_toggle == True:
                    verse_text = bcolors.WARNING+row[1]+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]+bcolors.OKGREEN+" TSK>"+row[6]+bcolors.ENDC
                new_text = textwrap.fill(verse_text,60)
                print(new_text)
                refs += row[1]+str(row[3])+":"+str(row[4])+" "
            elif search_words(row[5],search_word.split(' ')):
                count += 1
                if count % 5 == 0:
                    key_press = raw_input("Press <ENTER> to continue...")
                    if key_press in ('x','X'):
                        clear_screen()
                        key_press = ''
                        break
                if TSK_toggle == False:
                    verse_text = bcolors.WARNING+row[1]+" "+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]
                elif TSK_toggle == True:
                    verse_text = bcolors.WARNING+row[1]+str(row[3])+":"+str(row[4])+bcolors.ENDC+" "+row[5]+bcolors.OKGREEN+" TSK>"+row[6]+bcolors.ENDC
                new_text = textwrap.fill(verse_text,60)
                print(new_text)
                refs += row[1]+str(row[3])+":"+str(row[4])+" "
                
    new_refs = textwrap.fill(refs,60)
    print()
    print(bcolors.OKBLUE+new_refs+bcolors.ENDC)
    print("### {0} found in {1} verses.".format(search_word, count))



bible_books = []
bible_abr = []

TSK_toggle = False
OT_toggle = False
NT_toggle = False
BOOK_toggle = False

db_Book = "KJV-PCE-TSK.db"

con = None
try:
    con = sqlite3.connect(db_Book)
    cur = con.cursor()
    cur2 = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()

    clear_screen()
    
    print(bcolors.WARNING+"SQLite version: {0}\n".format(data[0]))
    print(bcolors.ENDC)
    print("Testing database by executing a query to find the text and cross references for Romans 8:14.")
    print("""query=> SELECT VText, TSK from Bible where Book='Ro' and Chapter=8 and Verse=14""")
    cur.execute("SELECT VText, TSK from Bible where BookAbr='Ro' and Chapter=8 and Verse=14")
    for i in cur:
        print('Ro 8:14 '+i[0]+'\n'+"TSK>"+i[1])
    print()
    print("""Welcome to the Commandline KJV Bible program, PCE edition.
Copyright (c) Bill Allen 2012
Released under MIT license, see LICENSE.txt found in the
distribution archive for more information.

""")
    key_press = raw_input("Press <ENTER> to continue...")



    help_text = """\nThis program can search for any single word or words in
series (case sensitive), ex: Enoch  ex: save his people
It can also search a single verse reference, ex:  Es 8 9 or
Esther 8 9.  Treasury of Scriptural Knowledge (TSK)
references are also available.  This program is best viewed
at a commandline or in a large or full window terminal screen.

Available commands:
W = Word Search
R = Verse Reference Search
O = Old Testament search range, toggle
N = New Testament search range, toggle
B = Book to search, toggle with book name or abreviation
T = Disply TSK (Treasury of Scriptural Knowledge) references
Q = Quit the program
NOTES:
1)At any "Press <ENTER> to continue..." displayed
during a verse listing as the result of a search one may
hit x or X and then <ENTER>.  This will cause the curent
verse listing to cease and return you to the main menu.
2)Toggles are flags that store the current state of the
program concerning Old Testament, New Testament and Book
search ranges.  Also stored as a toggle is the TSK flag
which controls if the TSK references are displayed.  The
Toggle Bar appears in the program like this:
Toggles = OT False, NT False, BOOK False, TSK False
3)By default, the entire Bible is the defined search range
and the TSK is off.  Use the Toggles to change the behavior
of the program with regard to these search ranges being on
or off or whether to display the TSK.
4)SEARCHING: Adding "+" to the beginning of a word or phrase
causes the search to be case sensitive.  It also causes multi-
ple words to be treated as a single phrase to be searched for.
Without the "+" the search is not case sensitive and miltiple
words are used generally so that if all the words appear any-
where in a verse, the search will return results.

Bible book name abbreviations:\n"""

    
    cur.execute("SELECT DISTINCT BookAbr from Bible")
    books = ''        
    for i in cur:
        books += i[0].ljust(5,' ')
        bible_abr.append(i[0])

    cur2.execute("SELECT DISTINCT BookName from Bible")
    for j in cur2:
        bible_books.append(j[0])

    book_names = textwrap.fill(books,30)
    clear_screen()

    print(help_text + book_names)
    print()
    key_press = raw_input("Press <ENTER> to continue...")
    clear_screen()
    
    search_word = ''
    search_ref = ''
    search_ans = ''
    BOOK_ans = ''

    while search_ans not in ('Q','q'):
        print()
        print(bcolors.HEADER + "Toggles = OT {0}, ".format(bcolors.WARNING+str(OT_toggle)) + bcolors.HEADER + \
          "NT {0}, ".format(bcolors.WARNING+str(NT_toggle)) + bcolors.HEADER + \
          "BOOK {0}, ".format(bcolors.WARNING+str(BOOK_toggle))+ bcolors.HEADER +
          "TSK {0}, ".format(bcolors.WARNING+str(TSK_toggle)) +bcolors.ENDC)
        search_ans = raw_input("Search for a [W]ord or [R]eference, [T]SK on/off, [O]ld Testament on/off, \n[N]ew Testament on/off, [B]ook on/off, [Q]uit, [H]elp:  ")

        if search_ans in ('W','w','Word','word','WORD','word'):
            search_word = raw_input("Enter a word to search for in the Bible:  ")
            clear_screen()
            print()
            Show_Verse_Word(search_word, BOOK_ans)
            
        elif search_ans in ('R','r','Reference','reference','Ref','ref','REF','ref'):
            search_ref = raw_input("Enter a Bible reference:  ")
            clear_screen()
            print()
            Show_Verse_Reference(search_ref)
            
        elif search_ans in ('H','h'):
            clear_screen()
            print(help_text + book_names)
            key_press = raw_input("Press <ENTER> to continue...")
            clear_screen()
            
        elif search_ans in ('T','t'):
            clear_screen()
            if TSK_toggle == False:
                TSK_toggle = True
                print("TSK is ON")
                clear_screen()
            elif TSK_toggle == True:
                TSK_toggle = False
                print("TSK is OFF")
                clear_screen()
                
        elif search_ans in ('O','o'):
            clear_screen()
            if OT_toggle == False:
                OT_toggle = True
                NT_toggle = False
                BOOK_toggle = False
                print("OT SEARCH is ON")
                clear_screen()
            elif OT_toggle == True:
                OT_toggle = False
                print("OT SEARCH is OFF")
                clear_screen()
                
        elif search_ans in ('N','n'):
            clear_screen()
            if NT_toggle == False:
                NT_toggle = True
                OT_toggle = False
                BOOK_toggle = False
                print("NT SEARCH is ON")
                clear_screen()
            elif NT_toggle == True:
                NT_toggle = False
                print("NT SEARCH is OFF")
                clear_screen()
                
        elif search_ans in ('B','b'):
            clear_screen()
            if BOOK_toggle == False:
                BOOK_toggle = True
                OT_toggle = False
                NT_toggle = False
                print("BOOK SEARCH is ON")
                BOOK_ans = raw_input("Book name or abreviation?  ")
                clear_screen()
            elif BOOK_toggle == True:
                BOOK_toggle = False
                OT_toggle = False
                NT_toggle = False
                print("BOOK SEARCH is OFF")
                clear_screen()
                
        elif search_ans in ('',' ','\t','\n'):
            clear_screen()

except sqlite3.Error as e: 
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:  
    if con:
        con.close()
        
        
        

        
