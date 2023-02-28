  ## 1.字符串倒转
  # Reversing a string using slicing
  
  my_string = "ABCDE"
  reversed_string = my_string[::-1]
  print(reversed_string)
  
  # Output
  # EDCBA

  ## 首字母大写
  my_string = "my name is chaitanya baweja"
  
  # using the title() function of string class
  new_string = my_string.title()
  print(new_string) 
  # Output
  # My Name Is Chaitanya Baweja

  
  ## 在字符串中查找唯一元素
  my_string = "aavvccccddddeee"
  
  # converting the string to a set
  temp_set = set(my_string)
  
  # stitching set into a string using join
  new_string = ''.join(temp_set)
  
  print(new_string)

