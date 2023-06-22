import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


df = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_no():
    word = input("Enter a word: ").upper()
    try:
        output_list = [df[letter] for letter in word]
    except KeyError:
        print("sorry try with word only.")
        generate_no()

    else:
        print(output_list)
generate_no()