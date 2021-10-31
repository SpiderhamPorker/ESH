import os
import pathlib


def main():
    def lang_en():
        str1 = 'ESH >'
        str2 = os.getcwd()
        str3 = '< $ '
        comline = f'{str1}{str2}{str3}'

        cmdline = input(comline)

        if cmdline[0] == 'c' and cmdline[1] == 'd' and cmdline[2]== ' ':
                cdpath = cmdline.removeprefix('cd ')
                if os.path.exists(cdpath) == True:
                    os.chdir(cdpath)
                    lang_en()    
                else:
                    print('Path not found. Please, try again.')
                    lang_en()
        
        if cmdline == 'lang':
            main()

        if cmdline == 'dir':
            dir = os.listdir(str2)
            print(dir)
            lang_en()

        if cmdline == 'ls':
            currentDirectory = pathlib.Path('.')
            for currentFile in currentDirectory.iterdir():
                print(currentFile)
            lang_en()
    
        if cmdline == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            lang_en()

        if cmdline == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            lang_en()

        if cmdline == 'write':
            text = input('What do you want to write?\n')
            archive = input('Write the path to the file: ')

            with open(archive, 'w') as f:
                f.write(text)
            lang_en()

        if cmdline == 'man'or cmdline == 'help':
            print('\n"cd" changes the current directory of the terminal.\nNOTE: do not use cd <path> or it won´t work. Just write cd and hit Enter.\n\n"ls" shows the files on the current directory using os.listdir() method. \n"dir" shows the files on the current directory using the pathlib module. \n\n"clear" or "cls" clears all the text on the terminal.\n\n"lang" lets you change the language of the terminal.\n\n"man" or "help" prints this. \n\n"exit" or "quit" exits the terminal. \n\nFor more information, visit https://esh.daymons.ga\n')
            lang_en()

        if cmdline == 'exit' or cmdline=='quit':
            quit()

        else:
            print('Command not recognized. Please try again or execute "man" for help.')
            lang_en()
    
    def lang_es():
        str1 = 'ESH >'
        str2 = os.getcwd()
        str3 = '< $ '
        comline = f'{str1}{str2}{str3}'

        cmdline = input(comline)

        if cmdline[0] == 'c' and cmdline[1]=='d' and cmdline == ' ':
            cdpath=cmdline.removeprefix('cd ')
            if os.path.exists(cdpath) == True:
                os.chdir(cdpath)
                lang_es()
            else:
                print('Ruta no encontrada. Por favor, pruebe de nuevo.')
                lang_es()

        if cmdline == 'lang':
            main()

        if cmdline == 'dir':
            dir = os.listdir(str2)
            print(dir)
            lang_es()

        if cmdline == 'ls':
            currentDirectory = pathlib.Path('.')
            for currentFile in currentDirectory.iterdir():
                print(currentFile)
            lang_es()
    
        if cmdline == 'clear' or cmdline == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            lang_es()

        if cmdline == 'write':
            text = input('¿Que desea escribir?\n')
            archive = input('Escriba la ruta al archivo: ')

            with open(archive, 'w') as f:
                f.write(text)
            lang_es()

        if cmdline == 'man' or cmdline == 'help':
            print('\n"cd" cambia el actual directorio de la terminal.\nNOTA: no use cd <ruta> o no funcionará. Solo escriba "cd" y presione Enter.\n\n"write" escribe (IMPORTANTE: SOBREESCRIBE TODO EL ARCHIVO) el texto que quiera.\nSolo escriba "write", presione Enter, y escriba el texto y la ruta al archivo.\n\n"ls" muestra los archivos del directorio actual usando el método os.listdir. \n"dir" muestra los archivos del directorio actual utilizando el módulo pathlib. \n\n"clear" o "cls" quita tpdp el texto de la terminal.\n\n"lang" te permite cambiar el idioma de la terminal.\n\n"man" o "help" muestra este menú de ayuda. \n\n"exit" o "quit" cierra la terminal. \n\nPara más información, visite https://esh.daymons.ga\n')
            lang_es()


        if cmdline == 'exit' or cmdline=='quit':
            quit()

        else:
            print('Comando no reconozido. Ejecute "man" para ver todos los comandos.')
            lang_es()

    lang_selection = input('Choose your language (es/en): ')
    if lang_selection == 'es':
        lang_es()

    elif lang_selection == 'en':
        lang_en()
    
    else:
        print('Choose a correct option!')
        main()
    
if __name__ == '__main__':
    main()
