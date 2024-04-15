import pyautogui
import time


# debug code for identifying positions and colors
'''
while True:
    time.sleep(0.1)
    im = pyautogui.screenshot()
    print(pyautogui.position())
    print(im.getpixel(pyautogui.position()))
'''

# for different websites
# NYT ->
# unlimited -> https://wordlegame.org/
wordle_type = 'unlimited'
if wordle_type == 'unlimited':
  positions_of_squares = [(2494,2655,2814,2960,3110), (484,626,790,949,1097,1240)]
else:
  positions_of_squares = [(2503,2652,2804,2959,3110), (674,813,968,1138,1286,1445)]


# get initial word list
import nltk
nltk.download('words')
word_list = [w.lower() for w in list(nltk.corpus.words.words()) if len(w) == 5]
#word_list = ['trace','aread','cried','dried','fried']


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
                
              except:
                pass
          else:
            if test_word[idx] == word[yellows[j]]:
              is_it_in = 1
              rows.remove(idx)

      if is_it_in == 0:
        try:
          real_word_list.remove(test_word)
        except:
          pass
    
    for j in range(0, len(greys)):
      for idx in range(0, len(test_word)):
        if idx in rows:
          if word[greys[j]] == test_word[idx]:
            try:
              real_word_list.remove(test_word)
            except:
              pass
              
while True:
  real_word_list = word_list[:]

  prev_guess = 'trace'
  pyautogui.press('enter')
  #print('trace')
  pyautogui.moveTo(3000, 1000)



  pyautogui.click()
  pyautogui.write('trace', interval=0.25)
  pyautogui.press('enter')
  time.sleep(2)
  screenshot = pyautogui.screenshot()
  ans = ''
  for i in range(0,5):
      color = screenshot.getpixel((positions_of_squares[0][i],positions_of_squares[1][0]))
      if color == (255,255,255) or color==(251,252,255):
        real_word = False
      elif color == (198,180,81) or color == (201,180,88) or color==(238,193,33):
        ans +='p'
      elif color == (113,170,97) or color == (106,170,100) or color==(127,184,74):
        ans+='y'
      elif color == (120,124,126) or color == (165,174,197):
        ans+='n'
      #pyautogui.moveTo(positions_of_squares[0][i], positions_of_squares[1][0])
      #time.sleep(0.2)
  try_num = 1
  while True:
    time.sleep(0.1)

    

    
    if ans == 'yyyyy' or try_num==6:
      break
    possible_words(prev_guess,ans)
    pyautogui.moveTo(3000, 1000)
    pyautogui.click()
    print('possible words: ', len(real_word_list))
    words_now = real_word_list[:]
    for i in range(0,len(words_now)):
      ai_guess = words_now[i]


      pyautogui.write(ai_guess, interval=0.25)
      pyautogui.press('enter')
      time.sleep(3)

      
      real_word = True
      ans = ''        

      im = pyautogui.screenshot("pic.png")
      if im.getpixel((2974,726)) == (249,184,0):
        time.sleep(1)
        pyautogui.press('enter')
        ans = 'yyyyy'
        break

      for i in range(0,5):
        
        color = im.getpixel((positions_of_squares[0][i], positions_of_squares[1][try_num]))
        
        if color == (255,255,255) or color==(251,252,255):
          real_word = False
        elif color == (198,180,81) or color == (201,180,88) or color==(238,193,33):
          ans +='p'
        elif color == (113,170,97) or color == (106,170,100) or color==(127,184,74):
          ans+='y'
        elif color == (120,124,126) or color == (165,174,197):
          ans+='n'
        #pyautogui.moveTo(positions_of_squares[0][i], positions_of_squares[1][try_num])
        #time.sleep(0.2)
      if real_word:
        break
      for i in range(0,5):
        pyautogui.moveTo(3000, 1000)
        pyautogui.click()
        pyautogui.press('backspace')
        
        time.sleep(0.1)
      real_word_list.remove(ai_guess)
      word_list.remove(ai_guess)

    prev_guess= ai_guess
    try_num+=1
  time.sleep(1)

