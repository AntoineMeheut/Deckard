# -*- coding: utf-8 -*-
import sys
import ollama
import source.modules.utils.logger as utils
from source.modules.functions.ensure_model_exists import ensure_model_exists

__all__ = ['test_prompt']


def test_prompt(client, model: str, model_type: str, system_prompt: str, test_prompt: str) -> tuple[str, bool]:
    """
    Send a test prompt to the LLM and get the response.

    Function input:

    Function output:

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000015.

    :param : client
    :rtype: str
    :param : model
    :rtype: str
    :param : model_type
    :rtype: str
    :param : system_prompt
    :rtype: str
    :param : test_prompt
    :rtype: str
    :return: tuple
    :rtype: str,bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting send a test prompt to the LLM and get the response....')

    try:
        if model_type == "openai":
            response = client.chat.completions.create(
                model = model,
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": test_prompt}
                ]
            )
            return response.choices[0].message.content, False
        elif model_type == "anthropic":
            response = client.messages.create(
                model = model,
                max_tokens = 1024,
                messages = [
                    {
                        "role": "user",
                        "content": test_prompt
                    }
                ],
                system = system_prompt
            )
            return response.content[0].text, False
        elif model_type == "ollama":
            if not ensure_model_exists(model):
                logger.error('Exception : problem no model found for this model = %s', str(model))
                sys.exit()
            response = ollama.chat(
                model = model,
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": test_prompt}
                ]
            )
            return response['message']['content'], False
        logger.error('Exception : problem during test prompt of %s', str(model_type))
        sys.exit()
    except Exception as e:
        logger.error('Program exit on exception EXT-000015 = %s', str(e))
        sys.exit()
