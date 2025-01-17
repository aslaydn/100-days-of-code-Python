import pandas

{"A": "Alfa", "B": "Bravo"}
import pandas
data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}      

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)    

generate_phonetic()