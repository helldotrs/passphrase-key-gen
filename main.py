import random

def get_list(file_path):
    with open(file_path, 'r') as my_file:
        output_list = [line_item.strip() for line_item in my_file.readlines()]
    return output_list

def randomize_list(a):
  return random.shuffle(a)
  #is it better to scrable list or rang a number and check if its already been genereated?

#FIX ME: pull apart, 
def get_result():
  count = 0
  output_list = []
  for item in randomize_list(get_list(nouns.txt)): #FIX ME: input for filepath/standard path if no output (like wordlist.txt)
    output_list.append(f"{count} : {item}")
    count += 1
  return output_list
  
def print_result():
  for item in get_result():
    print(item)

print_result()
