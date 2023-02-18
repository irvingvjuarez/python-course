import random

finalResults = []
options = ("scissors", "paper", "stone")
results = {
  f"{options[0]} {options[1]}": "win",
  f"{options[0]} {options[2]}": "lose",
  f"{options[1]} {options[0]}": "lose",
  f"{options[1]} {options[2]}": "win",
  f"{options[2]} {options[0]}": "win",
  f"{options[2]} {options[1]}": "lose"
}

inputMsg = ""
for option in options:
  inputMsg += f"{option.capitalize()} "
  results[f"{option} {option}"] = "tie"

inputMsg += ": "
rounds = len(options)

i = 0
userOption = ""
computerOption = ""

def validResponse(i):
  if userOption in options:
    i += 1
    computerOption = random.choice(options)
    result = results[f"{userOption} {computerOption}"]
    finalResults.append(result)
    print(result)
  return i

while i < rounds or not userOption in options:
  userOption = input(inputMsg).lower()

  i = validResponse(i)

  if i == rounds:
    print("Your final results:", finalResults)
