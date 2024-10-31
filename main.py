from funcs import is_monster_bio_start
from class_names import class_names_from_num

import json, os, math

if not os.path.exists('db'):
    os.mkdir('db', 0o666)

manual = open('monster_manual.txt', 'r', encoding='utf8').read()
monster_lines = []
monster_nums_names = []

for line in manual.split('\n'):
    is_start_of_bio = is_monster_bio_start(line, len(line.split(' ')[0]))
    
    if is_start_of_bio['b']:
        number = is_start_of_bio['num']

        if is_start_of_bio['check_for_0']:
            number = f'{number}0'
        
        name = line.split(f'{number} ')[1]

        monster_lines.append(f'{number} {name}')
        monster_nums_names.append([number, name])

monster_bio_db = {}
cur_db = []

i = -1
for line in manual.split('\n')[4:]:
    
    if i == len(monster_lines) - 1:
        continue

    cur_db.append(line)
    
    if monster_lines[i + 1] == line:
        name = monster_nums_names[i][1]

        monster_bio_db[name] = cur_db

        cur_db = []

        i += 1

for num_name in monster_nums_names:
    num = num_name[0]
    name = num_name[1]

    db = monster_bio_db[name]

    class_value = class_names_from_num[int(math.floor(float(num) - 1))]

    i = 0

    for line in db:
        split = line.split(':')

        if i == 3 or len(split) == 1:
            break
        
        key = split[0][2:].strip()
        value = split[1].replace(',', '').strip()

        if value != '∞' and key == 'dps' or key == 'hp':
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    assert 'Value Error'

        if key == 'dps': 
            dps_value = value
        elif key == 'hp':
            hp_value = value
        elif key == 'drops':
            drops_value = value
            

        i += 1

    wiki_content = f"""{{{{Monster
|Class = {class_value}
|Region = 
|DPS = {dps_value}
|HP = {hp_value}
|Drops = {drops_value}
}}}}"""
 
    print(f'saving db for {name}')
    with open(f'db/{name}.txt', 'w', encoding='utf-8') as f:
        f.write(wiki_content)
        
print('Done!')