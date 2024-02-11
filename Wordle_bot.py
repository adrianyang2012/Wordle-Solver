import pyautogui
import time
'''
while True:
    time.sleep(0.1)
    im = pyautogui.screenshot()
    print(im.getpixel(pyautogui.position()))
'''
positions_of_squares = [(2492,2658,2821,2991,3155),(549,712,877,1047,1218,1390)]


import nltk
nltk.download('words')
word_list = [w.lower() for w in list(nltk.corpus.words.words()) if len(w) == 5]
word_list = ['trace','aread','cried','dried','fried']
real_word_list = word_list[:]
def possible_words(word, answer):
  global real_word_list
  greens = []
  yellows = []
  greys = []
  for i in range(0, len(answer)):
    if answer[i] == 'y':
      greens.append(i)
    elif answer[i] == 'p':
      yellows.append(i)
    else:
      greys.append(i)
  for i in range(0, len(word_list)):

    rows = [0,1,2,3,4,5]
    test_word = word_list[i]

    for idx in range(0, len(greens)):
     
      if not word[greens[idx]] == test_word[greens[idx]]:
        try:
          real_word_list.remove(test_word)
          
        except:
          pass
      else:
        rows.remove(greens[idx])
    
    for j in range(0, len(yellows)):
      is_it_in = 0
      for idx in range(0, len(test_word)):
        
        if idx in rows:
          
          if yellows[j] == idx:
            if test_word[yellows[j]] == word[yellows[j]]:
              try:
                real_word_list.remove(test_word)
                rows.remove(idx)
                
              except:
                pass
          else:
            if test_word[idx] == word[yellows[j]]:
              rows.remove(idx)
              is_it_in = 1
      if is_it_in == 0:
        try:
          real_word_list.remove(test_word)
        except:
          pass
      else:
        rows.remove(yellows[j])
    
    for j in range(0,len(greys)):
      for idx in range(0,len(test_word)):
        print(rows,i,j,idx)
        if greys[j] in rows:
          if word[greys[j]] == test_word[idx]:
            try:
              real_word_list.remove(test_word)
            except:
              pass
              
    
prev_guess = 'trace'
print('trace')
pyautogui.moveTo(3000, 1000)
pyautogui.click()
pyautogui.write('trace', interval=0.25)
pyautogui.press('enter')
time.sleep(2)
screenshot = pyautogui.screenshot()
ans = ''
for i in range(0,5):
    color = screenshot.getpixel((positions_of_squares[0][i],positions_of_squares[1][0]))
    if color == (255,255,255):
      real_word = False
    elif color == (198,180,81) or color == (201,180,88):
      ans +='p'
    elif color == (113,170,97) or color == (106,170,100):
      ans+='y'
    elif color == (120,124,126):
      ans+='n'
    pyautogui.moveTo(positions_of_squares[0][i],positions_of_squares[1][0])
    time.sleep(0.1)
try_num = 1
while True:
  if ans == 'yyyyy' or try_num==6:
    break
  possible_words(prev_guess,ans)
  pyautogui.moveTo(3000, 1000)
  pyautogui.click()
  for i in range(0,len(real_word_list)):
    ai_guess = real_word_list[i]
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
      elif color == (198,180,81) or color == (201,180,88):
        ans +='p'
      elif color == (113,170,97) or color == (106,170,100):
        ans+='y'
      elif color == (120,124,126):
        ans+='n'
    
    if real_word:
      break
    for i in range(0,5):
      pyautogui.moveTo(3000, 1000)
      pyautogui.click()
      pyautogui.press('backspace')
      
      time.sleep(0.1)

  prev_guess= ai_guess
  try_num+=1
print(ans,real_word_list,try_num)
