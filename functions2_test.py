#import from another file
import functions2

sentence = "All good things come to those who wait."
words = functions2.break_words(sentence)
print(words)

sorted_words = functions2.sort_words(words)
print(sorted_words)

functions2.print_first_word(words)
functions2.print_last_word(words)
print(words)

functions2.print_first_word(sorted_words)
functions2.print_last_word(sorted_words)
print(sorted_words)

functions2.print_first_and_last(sentence)
functions2.print_first_and_last_sorted(sentence)

print(sentence)
print(words)


