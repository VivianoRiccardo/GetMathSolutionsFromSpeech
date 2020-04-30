# GetMathSolutionsFromSpeech

GMSFS is a simple script that uses online APIs from wolfram alpha and google speech recognition through
some python implemented library.

# What do you need:

- SpeechRecognition python library: https://github.com/Uberi/speech_recognition, to get speech to text
- wolframalpha python library to get text to results
- gTTS to save the results
- mplayer to reproduce the results

# The inputs:

- If the speech recognition google api can't understand properly what you say you can change the meaning
of the most accurate words you can say with what you want really say. for example if you want to tell google the word
"Laplace" but google can't understand your pronunciation but at the same time it understand always the word "house"
you can replace the word "Laplace" with "house" writing in the file substitutions.txt house;laplace

- To get accurate results you should take a look to the inputs of wolfram alpha

# The outputs

- In the manings.txt files you can tell your device how to say some carachters/words exactly as you want
