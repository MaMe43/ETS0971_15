# section-B
# string : 
it is a sequence of characters enclosed within quotes. It is one of the most commonly used data types and used to represent textual data.
strings can be enclosed in single quotes (''),double quote ("") or triple quote
conclusion : strings are versatile and essential for handling textual data in python program.
# string method 
there are many built in methods that are used to manipulate strings in python.
# str.lower() method
it is used to convert all uppercase letters in string to lowercase.it does not modify or change the form of the original stting but returns anew string with all characters in lowercase. this method only affects uppercase letters. lowercase letters and non alphabetic characters remain unchanged. 
# str .upper() method 
it is used to convert all lowercase letters in string to uppercase. this method also dose not modify the orginal string but returns a new string with all characters in uppercase. it only affects lowercase letters other characters remain the same. 
# str . title()
it is used to convert a string so that each word starts with an uppercase letter and the rest of the letters are in lowercase. simply it is used to capitallize the first letter of each word. it makes all other letters lower case even if the original text had a mixing casing.
# str.capitalize()
this string method is used for changing the first character of the string to uppercase and the rest to lowercase. here if the string starts with non alphabetic character it remains the same . this string method can be used for formatting names anad titles.
# str.swapcase()
this string method is used for swapping the case of all characters in the string . it changes the uppercase to lowercase and the lowecase to uppercase. here also the non alphabetic characters remains the same and it does not modify th original string.
# str.isupper()
this string method is used to check if the alphabets inside the string are all in uppercase.
it has a true and false return value.this method also ignors non alphabetic characters. when the alphabets inside the string are uppercase it returns true value .otherwise if the alphabets are lowercase it returns false value .
# str.islower()
this string method is used to check if the alphabets inside the string are all in lowercase. it has a true and false return value . this method also ignores non alphabetic characters. when the alphabets inside the string are lowercase it returns true value otherwise it returns false value.
# str.strip()
this string type is used for removing leading and trailing whitespaces or specified characters from the string. the whitespace refers to the invisible characters that creates empty space in the text. this method also does not modify the orginal characters.
# str.lstrip()
used for removing the leading whitespace or specified character from the string.
# str.rstrip()
used for removing the trailing whitespace or specified chracter fom the string.
# str.replace()
this method is used for replacing occurrance of a substring with another substring inside the string .  this string method is different from the others because it modifies the original string . this method is also case sensetive .
# str.split()
this method is used for dividing string into a list of substring based on a specified separator.
# str.join()
this method is the inverse of str.split(). it is used for making the list strings or iterable strings into single string by combininf them.
 # str.find() 
 this method is used for searching for a substring within a string and returns a lowest index where it is found . this string method is also case sensetive . if it does not found the substring it returns -1.
 # str.index()
 thid method is the same with str.find(). but it raises a value error when substring is not found rather than returning -1.
 # str.count()
 this strin gmethod is used for determinig the number of substrings in a given string . this method also is case sensetive and it allows to specify search boundaries. it returns 0 if it the specified string not found.
 # str.startswith()
 this method is used check if a string begins with a specified substring and returns True or False value . It's useful for validation and  filtering.
 # str.endswith()
 this method is used for checking if a string ends with a specified substring and returns true or false . it is the opposite of str.startswith . this method deals with the suffix whereas the later deals with prefix.
 # str.isalpha()
 we use this string method inorder to check if all characters inside the string are alphabetic . if all the characters are alphabetic it returns true value otherwise false value. this method only returns true if every single character is letter doesn't accept whitespace , numbers and other symbols .
 # str.isdigit()
 we use this string method in order toc check is all charcters inside the string are digits .
 # str.isalnum()
 this method checks if all characters in a string are alphanumeric letteror digits and the string contains at least one character.it will return true if all characters are letters and numbers otherwise it returns false value . empty string also has false value .
 # str.isspace()
this method is used to check if all the characters in a string are whitespace characters. It returns True if the string contains only whitespace characters and is not empty, otherwise, it returns False.
# str.zfill()
pads a numeric string  with leading zeros  until it reaches the specified width. If the string starts with a sign (+ or -), the zeros are inserted after the sign. width here represents the total length of the returned string after padding
# str.format()
 is used for string formatting, allowing us to insert values into placeholders ({}) in a string dynamically. 
 # str.center()
 this string method  returns a centered string of a specified width, padded with a given fillchar. width here represents the total length of the returned string.
 fillcar represents caracter that used for padding. 
 # str.ljust()
 returns a left-justified string padded with a specified fillchar.
 # str.rjust()
 returns a right-justified string padded with a specified fillchar.
 # str.expandtabs()
 is used to replace tab characters (\t) in a string with spaces. This is particularly useful for formatting text with consistent indentation or aligning columns of data.
 # str.encode()
 thid method converts a string into a bytes object using a specified encoding. This is essential when we need to Store strings in binary format , Send strings over networks, Work with files or databases that require byte data .
 # len() >>> function
 this  function returns the number of items in an object, including the length of strings.