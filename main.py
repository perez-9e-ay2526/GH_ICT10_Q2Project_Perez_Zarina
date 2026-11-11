
from pyscript import display, document

# CONFIRM OFFICER

def confirm_officer(e):
    document.getElementById('output').innerHTML = ''
    input_first = str(document.getElementById('firstname').value) # gets the user input
    input_last = str(document.getElementById('lastname').value)

    input_full = str(input_first) + " " + str(input_last)

    input_final = input_full.title() # changes the case of the name

    officer_names = ['Zarina Perez', 'Maryam Ledesma', 'Nathan Bautista', 'Hans Baquiran', 'Aiva Suson', 'Zoey Reyes'] 

    officer_checker = input_final in officer_names # checks if user input is valid

    display_message = (f'Sorry {input_final}, your name is not on the list.', f'Congratulations {input_final}! You are now part of the Cadet Officer club.')
    
    display(display_message[officer_checker], target="output")



# ADD MEMBERS

member_names = {'Zarina Perez', 'Maryam Ledesma', 'Nathan Bautista', 'Hans Baquiran', 'Aiva Suson', 'Zoey Reyes', 'Oshri Gonzales', 'Rico Gozum', 'Renzo Madrono', 'David Valeriano', 'Jamielle Orduna', 'Alyssandra Rodriguez', 'Cyanne Leachon', 'Ramon Santiago', 'Thea Correa', 'Reign Macachor', 'Franco Garcia', 'Ethan Valerio'}

display(*sorted(member_names), target='result')
document.getElementById('total').innerHTML = len(member_names)

def confirm_member(e):
    global member_names

    document.getElementById('result').innerHTML = ''

    #turns input into a set
    input_first = str(document.getElementById('firstname').value) 
    input_last = str(document.getElementById('lastname').value)

    input_full = str(input_first) + " " + str(input_last)

    input_final = {input_full.title()}

    #unites the member names and the input
    member_names |= input_final

    display(*sorted(member_names), target ='result') 

    #displays the numnber of club members
    document.getElementById('total').innerHTML = len(member_names)



# ELEMENT CHECKER

def confirm_element(e):
    document.getElementById('output2').innerHTML = ''
    input_symbol = str(document.getElementById('symbol').value)

    symbol_var = input_symbol.title()

    #dictionary containing all details abt the element
    dict_nonmetals   = {
        'H' : ('Symbol: H', 'Element: Hydrogen', 'Atomic Mass: 1.008', 'Atomic Number: 1'),
        'He' : ('Symbol: He', 'Element: Helium', 'Atomic Mass: 4.002602', 'Atomic Number: 2'),
        'C' : ('Symbol: C', 'Element: Carbon', 'Atomic Mass: 12.011', 'Atomic Number: 6'),
        'N' : ('Symbol: N', 'Element: Nitrogen', 'Atomic Mass: 14', 'Atomic Number: 7'),
        'O' : ('Symbol: O', 'Element: Oxygen', 'Atomic Mass: 15.999', 'Atomic Number: 8'),
        'F' : ('Symbol: F', 'Element: Flourine', 'Atomic Mass: 18.998', 'Atomic Number: 9'),
        'Ne' : ('Symbol: Ne', 'Element: Neon', 'Atomic Mass: 20.180', 'Atomic Number: 10'),
        'P' : ('Symbol: P', 'Element: Phosphorus', 'Atomic Mass: 30.974', 'Atomic Number: 15'),
        'S' : ('Symbol: S', 'Element: Sulfur', 'Atomic Mass: 32.06', 'Atomic Number: 16'),
        'Cl' : ('Symbol: Cl', 'Element: Chlorine', 'Atomic Mass: 35.45', 'Atomic Number: 17'),
        'Ar' : ('Symbol: Ar', 'Element: Argon', 'Atomic Mass: 39.948', 'Atomic Number: 18'), 
        'Se' : ('Symbol: Se', 'Element: Selenium', 'Atomic Mass: 78.971', 'Atomic Number: 34'), 
        'Br' : ('Symbol: Br', 'Element: Bromine', 'Atomic Mass: 79.904', 'Atomic Number: 35'), 
        'Kr' : ('Symbol: Kr', 'Element: Krypton', 'Atomic Mass: 83.798', 'Atomic Number: 36'), 
        'I' : ('Symbol: I', 'Element: Iodine', 'Atomic Mass: 126.90', 'Atomic Number: 53'), 
        'Xe' : ('Symbol: Xe', 'Element: Xenon', 'Atomic Mass: 131.29', 'Atomic Number: 54'), 
        'Rn' : ('Symbol: Rn', 'Element: Radon', 'Atomic Mass: 222', 'Atomic Number: 86'),
    }

    dict_nonmetals2 = ['H', 'He', 'C', 'N', 'O', 'F', 'Ne', 'P', 'S', 'Cl', 'Ar', 'Se', 'Br', 'Kr', 'I', 'Xe', 'Rn']

    nonmetal_checker = symbol_var in dict_nonmetals2 #checks if element is in the list

    element_details = dict_nonmetals.get(symbol_var, ('', '', '', '')) #gets dictionary values
    
    display_message = (
        ('Sorry! Your input is not a non-metal. Try again.', '', ''), (element_details)) #boolean based responses

    display(*display_message[nonmetal_checker], target='output2') #displays message



# MEET CREATOR PAGE

#interests are displayed
document.getElementById('interests').innerHTML = ''

interests_var = ['1. Fictional Books/Movies/Shows', '2. Musicals', '3. K-POP', '4. Science', '5. Math']

display(*interests_var, target='interests')

#hobbies are displayed
document.getElementById('hobbies').innerHTML = ''

hobbies_var = ['1. Reading Books', '2. Binge-watching', '3. Creative Writing', '4. Oil Pastel Painting','5. Bonding with loved ones']

display(*hobbies_var, target='hobbies')