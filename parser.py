def parser(file):
    with open(file, 'r') as f:
        lines = f.readlines()    
    with open("clear_booster.txt", 'w') as clear_booster:
        comment = False
        k = 0
        for i, line in enumerate(lines):
            k += 1
            if i < len(lines):               
                if line.isspace(): continue

            if '/*' in line:
                comment = True
                continue

            if comment == True:
                if '*/' in line:
                    comment = False
                    continue
                if '*/' not in line:
                    continue

            if '!-' in line or '//-' in line:
                continue

            if '//' in line or '! ' in line:

                new_line = ''
                for i in range(len(line)-1):
                    if line[i] + line[i+1] == '//' or line[i] + line[i+1] == '! ':
                        break
                    else:
                        new_line += line[i]

                if new_line == '':
                    continue
                else:
                    clear_booster.write(new_line+'\n')
                    continue

            if '  ' in line:
                new_line = ''
                for i in range(len(line)-1):
                    if line[i] + line[i+1] == ' ':
                        continue
                    else:
                        new_line += line[i]

                clear_booster.write(new_line+'\n')
                continue

            clear_booster.write(line)

parser('booster.madx')