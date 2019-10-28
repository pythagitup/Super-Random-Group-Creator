''' Module used to work with .json roster files. '''

import json

def load_roster(period):
    ''' Load and return a period's roster. '''
    filename = f'{period.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    return roster

def add_name(period,name):
    ''' Add name to roster. '''
    filename = f'{period.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    roster.append(name)
    with open(filename, 'w') as f:
        json.dump(roster,f)

def remove_name(period,name):
    ''' Remove name from roster. '''
    filename = f'{period.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    if name in roster:
        roster.remove(name)
    with open(filename, 'w') as f:
        json.dump(roster,f)

def edit_name(period,wrong,right):
    ''' Edit name of student in roster. '''
    filename = f'{period.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    if wrong in roster:
        roster[:] = [right if x == wrong else x for x in roster]
    with open(filename, 'w') as f:
        json.dump(roster,f)
