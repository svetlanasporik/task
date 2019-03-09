word = input("Write your word:")
list = {}
feminine = {'а', 'я'}
neutral = {'о', 'е'}
last_letter = word[-1:]
ending_2last_letters = word[-2:]
if last_letter in feminine or ending_2last_letters == 'ка' or ending_2last_letters == 'жь' or ending_2last_letters == 'шь' or ending_2last_letters == 'чь' or ending_2last_letters == 'щь' or ending_2last_letters == 'ия' or ending_2last_letters == 'га' or ending_2last_letters == 'бь' or ending_2last_letters == 'вь' or ending_2last_letters == 'дь' or ending_2last_letters == 'зь' or ending_2last_letters == 'сь' or ending_2last_letters == 'ть':
    print("This word ends in" + " " + last_letter)
    print("The word " + " " + word + " is feminine")
elif last_letter in neutral:
    print("This word ends in" + " " + last_letter)
    print("The word " + " " + word + " is neutral")
else:
    print("This word ends in" + " " + last_letter)
    print("The word " + " " + word + " is masculine")

#print("This word ends in"+" "+last_letter)
#print( "The word is"+" " +  word)
