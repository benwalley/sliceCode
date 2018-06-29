import sys

toppings = [
    "Anchovy","Bacon", "Cheese",
    "Garlic","GreenPeppers", "Habenero", 
    "Jalapeno", "Mushrooms", "Olives", "Onions", 
    "Pineapple", "Pepperoni", "Sausage", "Tomatoes",
]

directions =  [
    ["N", -1, 0],
    ["NE", -1, 1],
    ["E", 0, 1],
    ["SE", 1, 1],
    ["S", 1, 0],
    ["SW", 1, -1],
    ["W", 0, -1],
    ["NW", -1, -1]
]

        
puzzle = [
    "SONCJ",
    "LRNOM",
    "LEJUJ",
    "APAII",
    "BPOHI",
    "TEPBUNGBAASAUNSLRUAU",
    "APHBTMPOEIJTLIPMOILO",
    "ENRMUCCAGKEJJAAGONSG",
    "MJUGEMPANGOASUPTLOTA",
    "BSLPNLRIAOPHRLKEKLRE",
    "HBAAA",
    "SGJUP",
    "TOAKS",
    "NIMNI",
    "OECGC"
]

sideOrder = ['left', 'right', 'bottom', 'back', 'top', 'front']
cube = []

##search for array of toppings
def checkWords(toppings):
    for topping in toppings:
        searchWord(topping)

##search for argument
def searchWord(topping):
    for side in cube:
        for line in side['arr']:
            for letter in line:    
                if letter == topping[0]:
                    checkWord(topping, side, line, letter)


def checkWord(topping, side, line, letter):
    lineNum = side['arr'].index(line)
    sideArr = side['arr']
    letterPos = sideArr[lineNum].index(letter)

   

#fill up the cube array with the correct values
def fillCube():
    cube.append({
        'side':'left',
        'arr': puzzle[0:5]
    })

    cube.append({
        'side':'right',
        'arr': puzzle[-5:]
    })

    cube.append({
        'side':'bottom',
        'arr': []
    })

    cube.append({
        'side':'back',
        'arr': []
    })

    cube.append({
        'side':'top',
        'arr': []
    })

    cube.append({
        'side':'front',
        'arr': []
    })
    
    cube[2]["arr"].append(puzzle[5][0:5])
    cube[2]['arr'].append(puzzle[6][0:5])
    cube[2]['arr'].append(puzzle[7][0:5])
    cube[2]['arr'].append(puzzle[8][0:5])
    cube[2]['arr'].append(puzzle[9][0:5])

    cube[3]['arr'].append(puzzle[5][5:10])
    cube[3]['arr'].append(puzzle[6][5:10])
    cube[3]['arr'].append(puzzle[7][5:10])
    cube[3]['arr'].append(puzzle[8][5:10])
    cube[3]['arr'].append(puzzle[9][5:10])

    cube[4]['arr'].append(puzzle[5][10:15])
    cube[4]['arr'].append(puzzle[6][10:15])
    cube[4]['arr'].append(puzzle[7][10:15])
    cube[4]['arr'].append(puzzle[8][10:15])
    cube[4]['arr'].append(puzzle[9][10:15])

    cube[5]['arr'].append(puzzle[5][15:])
    cube[5]['arr'].append(puzzle[6][15:])
    cube[5]['arr'].append(puzzle[7][15:])
    cube[5]['arr'].append(puzzle[8][15:])
    cube[5]['arr'].append(puzzle[9][15:])

    

def checkPuzzle(puzzle):
    fillCube()
    checkWords(toppings)


checkPuzzle(puzzle)
