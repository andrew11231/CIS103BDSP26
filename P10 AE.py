#Andrew Espinoza
def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(thetext)

# ---------------------------------
    print('Lenght:',len(thetext))
    stptext = thetext.strip()
    print('No spaces:',len(stptext))
    counttext = thetext.count('the') or thetext.count('The')
    print('Count of "the" :',counttext)
    if 'little' in thetext:
        print('The word "little" was found')
    else:
        print('The word "little" was Not found')
    
    if 'titan' in thetext:
        print('The word "titan" was found')
    else:
        print('The word "titan" was Not found')
    apos = thetext.find('appl')
    print('appl position is at:',apos)
    thetext2 = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    pyreplace = thetext2.replace('Python','PYTHON')
    print('Replace:',pyreplace)
    return
main()