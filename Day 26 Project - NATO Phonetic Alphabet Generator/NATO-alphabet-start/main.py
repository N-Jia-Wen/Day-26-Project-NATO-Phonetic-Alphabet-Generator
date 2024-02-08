import pandas

generate_alphabet = True
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

while generate_phonetic is True:
    try:
        input_text = input("Enter a word: ").upper()
        output_list = [alphabet_dict[letter] for letter in input_text]
        print(output_list)
    except KeyError:
        print("Please only input letters in the alphabet please.")
    else:
        generate_phonetic = False
