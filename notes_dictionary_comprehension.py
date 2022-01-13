'''Dictionary Comprehension
forma:
new_dict = {new_key:new_value for item in list}
lo que se traduce a
new_dict es igual a
o
new_dict ={new_key:new_value for (key, value) in dict.items() if test}
'''
# Challenge: You are going to use Dictionary Comprehension to create a dictionary called result that
# that takes each word in the given sentence and calculates the number of letters in each word.
sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
new_dict ={word:len(word) for word in sentence.split()}
print(new_dict)


# TODO convert temp_C into temp_f:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {days: weather_c[days] * 9/5 +32 for (days, temp_c)  in weather_c.items()}


print(weather_f)
