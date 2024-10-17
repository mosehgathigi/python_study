# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
# name = “ JOHn .“ to “john”
name = " JOHn ."
new_name = name.replace(".","").strip().lower()
print((new_name)) 
# Slice the below string to get you the resulting sentence:
# a. sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# b. sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton
# forces”

sentence_one = "The Dog Breed is German Shepherd"
result_one = sentence_one[sentence_one.index("Breed"):sentence_one.index("German") + len("German")]
print(result_one)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
result_two = sentence_two[sentence_two.index("Clinton"):sentence_two.index("forces") + len("forces")]
print(result_two)  


# Split the below sentence using a semicolon i.e ; And display length of the result.
# “The lazy dog; ran so fast; it hit the wall.”
sentence = "The lazy dog; ran so fast; it hit the wall."
result = sentence.split(";")
print(result)           
print(len(result)) 

#first_name=" Joh.n" last_name=" Do,e" Clean up and display Full name i.e John Doe
first_name = " Joh.n"
last_name = " Do,e"

clean_first_name = first_name.strip().replace(".", "").capitalize()
clean_last_name = last_name.strip().replace(",", "").capitalize()

full_name = f"{clean_first_name} {clean_last_name}"
print(full_name)


# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
clean_r = r.replace('[', '').replace(']', '').replace('"', '').replace(',', '')
print(clean_r)  

