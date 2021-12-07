### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # it should be == 
      return True
    else #missing the : after else
      return False
   
# typo bellow, should be def 
  dif highest_card(self, card1 card2): #Comma missing after card1
  if card1.value > card2.value: # if and else not indented 
    return card #should return card1 
  else:
    return card2
  
  #def is not indented 
def cards_total(self, cards): 
  total # total should be assigned a value i.e. total = 0
  for card in cards: 
    total += card.value
    return "You have a total of" + total #it will be unable to concatenate string and int
    # the return should not be inside the for loop
  
```
