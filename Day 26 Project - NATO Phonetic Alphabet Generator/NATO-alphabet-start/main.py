import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

input_text = input("Enter a word: ").upper()
output_list = [alphabet_dict[letter] for letter in input_text]
print(output_list)
