# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the input text with characters in reverse order.
    
    Parameters:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the words in the given sentence.
    
    Parameters:
    	sentence (str): Input text whose words will be counted.
    
    Returns:
    	int: Number of words in the sentence, using whitespace to separate words.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32