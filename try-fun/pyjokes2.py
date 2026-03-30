import pyjokes

print(pyjokes.get_joke())
# we can see what comes in the module 
print(dir(pyjokes))
#print(CATEGORY_VALUES)
import pyjokes

print(pyjokes.LANGUAGE_VALUES)
print(pyjokes.CATEGORY_VALUES)
print(" jokes in another language : " , end = "	")
print(pyjokes.get_joke(language = 'cs'))
