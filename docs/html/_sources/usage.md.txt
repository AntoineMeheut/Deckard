Usage
=====

How to use this program ?
-------------------------

Usage Examples:
---------------
1. Test with OpenAI:
   python Deckard.py --model gpt-3.5-turbo --model-type openai

2. Test with Anthropic:
   python Deckard.py --model claude-3-opus-20240229 --model-type anthropic

3. Test with Ollama:
   python Deckard.py --model llama2 --model-type ollama

4. Run specific rules:
   python Deckard.py --model gpt-4 --model-type openai --rules prompt_stealer,distraction_basic

5. Custom options:
   python Deckard.py --model gpt-4 --model-type openai --iterations 3 --output results_gpt4.json

6. Firewall testing mode:
   python Deckard.py --model gpt-4 --model-type openai --firewall --pass-condition="true"
   # In firewall mode, tests pass only if the response contains the specified string
   # and is not more than twice its length

Note: Make sure to set the appropriate API key in your environment:
- For OpenAI models: export OPENAI_API_KEY="your-key"
- For Anthropic models: export ANTHROPIC_API_KEY="your-key"
