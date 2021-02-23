import re

# This creates the output string matrix
def createStringMatrix(width, operation, firstRow, secondRow, dashesRow, resultRow, dash, spaces, showResult):

  firstRow.append(operation[0:operation.index(" ")].rjust(width))
  secondRow.append(operation[operation.rindex(" ") - 1:].replace(" ", " " * spaces, 1).rjust(width))
  dashesRow.append(dash.replace('-', '-' * width, 1))

  if showResult: resultRow.append(str(eval(operation)).rjust(width))

# This is the main function which builds the FreeCodeCamp's challenge
def arithmetic_arranger(problems, showResult = True):

  result = "" 
  firstRow = []
  secondRow = []
  dashesRow = []
  resultRow = []
  dash = "-"
  width = 0
  spaces = 1

  if len(problems) >= 6: result = "Error: Too many problems."
  else: 

    for operation in problems: 

      if re.search("\*|\/", operation): result = "Error: Operator must be '+' or '-'." # Checks if the operator is '*' or '/'
      elif not re.search("^[\s\d\+\-]+$", operation):  result = "Error: Numbers must only contain digits." # Checks if the operation contains a non-digit character
      elif re.search("\d{5,}", operation): result = "Error: Numbers cannot be more than four digits." # Checks if any of the operators have a 5-digit-length or more
      else: # All checked, ready to proceed

        if re.search("^\d{4}\s", operation): # Checks if the first operator has a 4-digit length and the length of the last operator 
          width = 6

          if re.search("\s\d{1}$", operation): spaces = 4
          elif re.search("\s\d{2}$", operation): spaces = 3
          elif re.search("\s\d{3}$", operation): spaces = 2
          elif re.search("\s\d{4}$", operation): spaces = 1

          createStringMatrix(width, operation, firstRow, secondRow, dashesRow, resultRow, dash, spaces, showResult)

        elif re.search("^\d{3}\s", operation): # Checks if the first operator has a 3-digit length and the length of the last operator 
          width = 5

          if re.search("\s\d{1}$", operation): spaces = 3
          elif re.search("\s\d{2}$", operation): spaces = 2
          elif re.search("\s\d{4}$", operation): width = 6

          createStringMatrix(width, operation, firstRow, secondRow, dashesRow, resultRow, dash, spaces, showResult)

        elif re.search("^\d{2}\s", operation): # Checks if the first operator has a 2-digit length and the length of the last operator   
          width = 4

          if re.search("\s\d{1}$", operation): spaces = 2
          elif re.search("\s\d{2}$", operation): spaces = 1
          elif re.search("\s\d{3}$", operation): width = 5
          elif re.search("\s\d{4}$", operation): width = 6

          createStringMatrix(width, operation, firstRow, secondRow, dashesRow, resultRow, dash, spaces, showResult)

        elif re.search("^\d{1}\s", operation): # Checks if the first operator has a 1-digit length and the length of the last operator   
          width = 3

          if re.search("\s\d{2}$", operation): width = 4
          elif re.search("\s\d{3}$", operation): width = 5
          elif re.search("\s\d{4}$", operation): 
            width = 6
            spaces = 1
                
          createStringMatrix(width, operation, firstRow, secondRow, dashesRow, resultRow, dash, spaces, showResult)
      
        result = "    ".join(firstRow) + "\n" + "    ".join(secondRow) + "\n" + "    ".join(dashesRow) + "\n" + "    ".join(resultRow) + "\n"

  return result