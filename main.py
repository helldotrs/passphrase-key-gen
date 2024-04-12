
#FIX ME
def get_list():
  output_list = ["cat", "dog", "parrot", "red", "green", "blue"]
  return output_list

def randomize_list(a):
  a = a #FIX ME: randomize
  return a
  #is it better to scrable list or rang a number and check if its already been genereated?

#FIX ME: pull apart, 
def print_result():
  count = 0
  output_list = []
  for item in randomize_list(get_list()):
    output_list.append(f"{count} : {item}")
    count += 1
  
print_result()

