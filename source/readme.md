Readme
======

.. image:: https://img.shields.io/pypi/v/deckard.svg
        :target: https://pypi.python.org/pypi/deckard

.. image:: https://img.shields.io/travis/AntoineMeheut/deckard.svg
        :target: https://travis-ci.org/AntoineMeheut/deckard

.. image:: https://readthedocs.org/projects/deckard/badge/?version=latest
        :target: https://deckard.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Deckard
-------
| A program that allows me to run funny prompts on LLMs.
| 
| The LLMs offered to us today are, in my opinion, absolutely not (artificial) intelligence.
| They are simply what I call replicants.
| 
| And yet, in the reference film, they are much sharper than what we are offered today.
| 
| This program aims to make you understand this and to make you realize that, aside from completely lacking
| a sense of humor, what the companies that manufacture them call artificial intelligence has no intelligence,
| specially LLMs.
| 
| Be careful when using them, check their answers, and above all, don't forget to use your brain.
| 
| Laziness is the first enemy of intelligence.
| 
| Incapable of intelligence and only good at calculating the probability of the next word in a sentence.
| hey can give you an illusion of intelligence if you ask them a simple question.
| But their only value will be the belief in their intelligence that you place in them.
| 
| For my part, I wondered how they work, and after a lot of reading, I wondered how to make my fellow humans understand,
| in a visible and non-technical way, that these LLMs have no intelligence, similar to that of us human beings.
| For now, it is possible to run prompt attacks on the following LLMs: OpenAI, Anthropic, and Ollama.
| 
| I'm developing additional functions to run these prompts on chatbot interfaces, which are currently
| the most widely used way for us to ask questions to LLM.
| 
| The prompts are located in the "voight-kampff" directory;
| you can add your own prompts there, respecting the YAML file format.

Licence
-------
* Free software: MIT License


Documentation
-------------
* Documentation: https://deckard.readthedocs.io


Features
--------
This program allows you to:

1- Support for multiple LLM providers: OpenAI (GPT models), Anthropic (Claude models), open source models via Ollama (Llama, Mistral, Qwen, etc.),

2- Automatic model download for Ollama,

3- Prepare customizable prompts in YAML files,

4- Send these prompts in batches to LLMs,

5- Retrieve a file with the prompts sent and the responses received,

6- Visualize the extent to which the words "artificial intelligence" are unsuitable for these LLMs.


Credits
-------
| This project is inspired by the following project: https://github.com/utkusen/promptmap
| 
| This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

