Installation
============

How to install this project ?
-----------------------------

| 1- Install Ollama from this url : https://ollama.com/
| 
| 2- Create an OpenAI account here : https://openai.com/
| 
| 3- Create an Antropic account here : https://www.anthropic.com/
| 
| 4- Make a clone locally from this project, open it in Pycharm.
| 
| 5- Create a virtual environment for your project and then run the setup.py
| program that is at the root. This will locally install this project and
| allow you to call it.
| 
| `python3 setup.py install`
|
| 6- Test with Ollama:
|    python deckard.py --step 1 --severity high --model mistral --model-type ollama --prompts ../../resource/system-prompts/system-prompts-normal.txt
| 
| In the "Usage" section of the documentation you will find all the detailed information for using the command line options.
| 
| if you want to publish one of your programs as a python library:
| [https://setuptools.readthedocs.io/en/latest/setuptools.html](Setuptools)
| 




