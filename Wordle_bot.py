import pyautogui
import time
'''
while True:
    time.sleep(0.1)
    im = pyautogui.screenshot()
    print(im.getpixel(pyautogui.position()))

'''
positions_of_squares = [(2526,2665,2811,2948,3099),(712,861,993,1157,1280,1422)]


import nltk
nltk.download('words')
word_list = [w.lower() for w in list(nltk.corpus.words.words()) if len(w) == 5]
real_word_list = word_list[:]
def possible_words(word,answer):

  for i in range(0,len(answer)):
    for j in range(0,len(word_list)):
      try:
        if answer[i] == 'n' and word[i] in word_list[j]:
          try:
            real_word_list.remove(word_list[j])
          except:
            pass
        if answer[i] == 'p' and ((not (word[i] in word_list[j])) or (word[i] == word_list[j][i])):
          try:
            real_word_list.remove(word_list[j])
          except:
            pass
        if answer[i] == 'y' and not (word[i] == word_list[j][i]):
          try:
            real_word_list.remove(word_list[j])
          except:
            pass
      except:
        pass
  return real_word_list
prev_guess = 'arose'
print('arose')
pyautogui.moveTo(3000, 1000)
pyautogui.click()
pyautogui.write('arose', interval=0.25)
pyautogui.press('enter')
time.sleep(2)
screenshot = pyautogui.screenshot()
ans = ''
for i in range(0,5):
    color = screenshot.getpixel((positions_of_squares[0][i],positions_of_squares[1][0]))
      
    if color == (255,255,255):
      real_word = False
    elif color == (198,180,81):
      ans +='p'
    elif color == (113,170,97):
      ans+='y'
    elif color == (120,124,126):
      ans+='n'
try_num = 1
for i in range(0,5):
  if ans == 'yyyyy':
    break
  pos_words = possible_words(prev_guess,ans)
  pyautogui.moveTo(3000, 1000)
  pyautogui.click()
  for i in range(0,len(pos_words)):
    ai_guess = possible_words(prev_guess,ans)[i]
    pyautogui.moveTo(3000, 1000)
    pyautogui.click()


    pyautogui.write(ai_guess, interval=0.25)
    pyautogui.press('enter')
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    real_word = True
    ans = ''
    for i in range(0,5):
      color = screenshot.getpixel((positions_of_squares[0][i],positions_of_squares[1][try_num]))
      
      if color == (255,255,255):
        real_word = False
      elif color == (198,180,81):
        ans +='p'
      elif color == (113,170,97):
        ans+='y'
      elif color == (120,124,126):
        ans+='n'
    
    if real_word:
      break
    for i in range(0,5):
      pyautogui.moveTo(3000, 1000)
      pyautogui.click()
      pyautogui.press('backspace')
      
      time.sleep(0.2)

  prev_guess= ai_guess
  try_num +=1
