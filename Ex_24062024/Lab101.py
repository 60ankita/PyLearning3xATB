letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u

letters = ['a','d','f','e','s']

def filter_vowels(letter):
    vowels = ["a","e","i","o","u"]
    return letter in vowels

result = filter_vowels('p')
print(result)


filtered_words =filter(filter_vowels, letters)
print(list(filtered_words))