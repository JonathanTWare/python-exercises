#!/usr/bin/env python
# coding: utf-8

# ### 1.Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string `2`, `False` otherwise.

# In[35]:


def is_two(i):
    if i == 2 or i=='2':
        return True
    else:
        return False


# In[36]:


print(is_two('2'))
print(is_two(2))
print(is_two(3))
print(is_two('3'))





# ### 2.Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.

# In[38]:


def is_vowel(i):
    if i in ['a','e','i','o','u']:
        return True
    else:
        return False


# In[39]:


print(is_vowel('a'))
print(is_vowel('b'))


# ### 3.Define a function named `is_consonant`. It should return `True` if the passed string is a consonant, `False` otherwise. Use your `is_vowel` function to accomplish this.

# In[40]:


def is_consonant(c):
    v = ['a','e','i','o','u']
    if c not in v:
        return True
    else:
        return False


# In[41]:


print(is_consonant('a'))


# ### 4.Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[42]:


def is_word(w):
    
    v = ['a','e','i','o','u']
    
    if w and w[0].lower() not in v:
        return w.capitalize()
    else:
        return w
    
        
    


# In[43]:


print(is_word('umbrella'))
print(is_word('party'))


# #### To exclude numbers

# In[44]:


def is_word(w):
    
    w = str(w)
    
    v = ['a','e','i','o','u']
    
    for c in w:
        if c.isdigit():
             return('This is not a word.')
    
    if w and w[0].lower() not in v:
        return w.capitalize()
    else:
        return w


# In[45]:


print(is_word('umbrella'))
print(is_word('party'))
print(is_word(2))
print(is_word(22222))


# ### 5.Define a function named `calculate_tip`. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[46]:


def calculate_tip(tip_perc, bill):
    return bill *tip_perc


# In[47]:


calculate_tip(120, .2)


# ### 6.Define a function named `apply_discount`. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[48]:


def apply_discount(r_price, discount_perc):
    return r_price - ((discount_perc / 100) * r_price)


# In[49]:


apply_discount(120,20)


# ### 7.Define a function named `handle_commas`. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[50]:


def handle_commas(n):
    n = n.replace(',','')
    return int(n)


# In[51]:


handle_commas('4,000,000')


# ### 8.Define a function named `get_letter_grade`. It should accept a number and return the letter grade associated with that number (A-F).

# In[52]:


def get_letter_grade(num):
    
    
        

    if num >= 88:
        return('A')
        
        
    elif num >=80:
        return('B')
        
        
        
        
    elif num >= 67:
        return('C')
       
        
        
    elif num >= 60:
        return('D')
        
        
        
    elif num >= 0:
        return('F')
        
    


# In[53]:


print(get_letter_grade(91))
print(get_letter_grade(75))
print(get_letter_grade(25))


# ### 9.Define a function named `remove_vowels` that accepts a string and returns a string with all the vowels removed.

# In[54]:


list('aeiou')

def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return somestring.lower() in list('aeiou')
        else:
            return False
    else:
        return False


# In[55]:


def remove_vowels(vowel_word):
    
    new_word = ''
    for letter in vowel_word:
        if not is_vowel(letter):
            new_word += letter
    return new_word


# In[56]:


remove_vowels('aquamarine')


# ### 10.Define a function named `normalize_name`. It should accept a string and return a valid python identifier, that is:
#    #### * anything that is not a valid python identifier should be removed
#    #### * leading and trailing whitespace should be removed
#    #### * everything should be lowercase
#    #### * spaces should be replaced with underscores
#    ### for example:
# ####        * `Name` will become `name`
# ####        * `First Name` will become `first_name`
# ####        * `% Completed` will become `completed`

# In[57]:


def normalize_name(str):
    
    str = str.replace("$","")
    str = str.replace("%","")
    str = str.replace("!","")
    str = str.strip()
    str = str.lower()
    str = str.replace(" ", '_')
    
    return str
    
    
    
    


# In[58]:


normalize_name('Name')


# ### 11.Write a function named `cumulative_sum` that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# ####    * `cumulative_sum([1, 1, 1])` returns `[1, 2, 3]`
# ####    * `cumulative_sum([1, 2, 3, 4])` returns `[1, 3, 6, 10]`

# In[59]:


def cumulative_sum(list):
    newl = []
    i = 1
    for n in list:
        csum = sum(list[:i])
        newl.append(csum)
        i += 1
    return newl
    


# In[60]:


cumulative_sum([1,3,5,7])


# In[34]:


cumulative_sum([1,1,1])

