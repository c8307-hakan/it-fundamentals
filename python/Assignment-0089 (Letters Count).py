sentence = input("please enter a sentence: ")
def char_frequency(sentence):
  dict ={}
  for i in sentence:
    keys = dict.keys()
    if i in keys:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict
print(char_frequency(sentence))