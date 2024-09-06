def count_a_in_string(input_string):
    count = input_string.lower().count('a')
    return count

user_input = input("Digite uma string para verificar a quantidade de letras 'a': ")
count = count_a_in_string(user_input)
print(f"A letra 'a' aparece {count} vezes na string.")