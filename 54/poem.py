INDENTS = 4
# part of William Shakespeare's play Hamlet
test  = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):
  lines = poem.lstrip().split('\n')
  stripped = [line.lstrip() for line in lines]
  spaced = [(" " * INDENTS) + line for line in stripped if line != '']
  print(stripped)
  pass

print_hanging_indents(test)



#['', 'To be, or not to be, that is the question:', "Whether 'tis nobler in the mind to suffer", '', 'The slings and arrows of outrageous fortune,', 'Or to take Arms against a Sea of troubles,', '']


