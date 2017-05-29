# Python Speech Generator

## Fast and simple Google Speech Generator in Python.

Requirements:

* Python >= 2.7
* [gTTS](https://pypi.python.org/pypi/gTTS)

*Flags:*

* --help, -h: Show program usage help.
```
python speech_generator.py [--help] [-h] 
```

* --text, -t: Identify the text you want to be pronounced.
* --lang, -l: Set the speech language.
* --speed, -s: Choose the velocity of the speech, between fast and slow.
* --name, -n: Identify the output file name.

*Example:*
```
python speech_generator.py -t Hello world -l en -s fast -n hello
```
