def modify(prop, dictArr):
  return list(
    map(lambda dict: dict[prop], dictArr)
  )

if __name__ == "__main__":
  print("Hi")