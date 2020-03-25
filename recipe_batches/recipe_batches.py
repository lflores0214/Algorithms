#!/usr/bin/python

import math
'''
receives two dictionaries
compare the values of the recipe and ingredients
if you don't have an ingredient called for in the recipe return 0
if the ingredient value is less than the corresponding recipe value return 0
divide // the value of ingredients by the value of recipes to get the number of batches you'll be able to make
'''
def recipe_batches(recipe, ingredients):
  total_batches = float('inf')
  for i in recipe:
    # if the recipe calls for something not in the ingredients return 0
    if ingredients.get(i) == None:
      return 0
    # if the recipe calls for more than whats available in ingredients
    if recipe[i] > ingredients[i]:
      return 0
    # this has to be down here because the fn will break if there is no ingredient[i] so it has to go through the check first
    current_batches = ingredients[i] // recipe[i]
    # if the current number of batches is less than the total_batches
    if current_batches < total_batches:
      # reassign total_batches to current_batches
      total_batches = current_batches
  return total_batches


print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))