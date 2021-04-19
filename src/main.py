from dialogue.idialogue import Dialogue
from dialogue.dialogueimpl import DialogueImpl
from language.language import Language

from argparse import ArgumentParser
from io import TextIOWrapper
from logging import error
from typing import List

def init_parser() -> ArgumentParser:
  """
  Returns: An ArgumentParser as defined in this function.
  """

  parser = ArgumentParser(
    description="A command line application that is intended to help users "
      + "memorize a script that has English and Chinese versions of lines.")

  parser.add_argument("path", type=str,
    help="The path to the script to use as input.")

  parser.add_argument("-a", "--attempts", type=int,
    default=2,
    help="The number of attempts allowed per line.")

  parser.add_argument("-l", "--language", type=str,
    default="chinese",
    help="The language of the lines you want to be quizzed on; specifically, "
      + "the lines you'll be asked to give the meaning of in the other language.")
      
  parser.add_argument("-n", "--no_display",
    action="store_true",
    help="Whether the line you're being quizzed on will be shown to you. I "
      + "recommend you do this as you're getting comfortable with the script.")

  parser.add_argument("-s", "--speakers", nargs="*", type=str,
    default="",
    help="The speakers you want to be quizzed on.")

  return parser

def read_dialogues(path: str) -> List[Dialogue]:
  """
  Parses the script at the given path and returns a list of dialogues
  corresponding with it.

  Arguments:
    - path: The path to the script.

  Returns: A corresponding list of dialogues.
  """
  dialogues: List[Dialogue] = []

  script: TextIOWrapper = open(path, "r", encoding="utf-8")
  for line in script:
    line: str = line.strip(":\n")
    if line != "":
      speaker: str = line
      english: str = script.readline().strip("\n")
      chinese: str = script.readline().strip("\n")
      dialogues.append(DialogueImpl(speaker, english, chinese))

  return dialogues

def quiz(dialogues: List[Dialogue], attempts: int, language: Language,
  speakers: List[str], no_display: bool) -> None:
  """
  Begins a quiz with the given configurations.

  Arguments:
    - dialogues: The list of dialogues.
    - attempts: The maximum amount of attempts the user is given.
    - language: The language the user will be quizzed on.
    - speakers: The list of speakers the user will be quizzed on.
    - no_display: Whether the dialogues are shown or otherwise.
  """
  filtered: List[Dialogue] = filter_dialogues(dialogues, speakers)
  attempts_left: int = attempts
  wrong: List[Dialogue] = []

  dialogue: Dialogue
  for dialogue in filtered:
    print(dialogue.get_speaker() + ":")
    if not no_display:
      print(get_dialogue(dialogue, other_language(language)))

    while attempts_left > 0:
      answer: str = input("Please input your answer for this line. You have "
        + str(attempts_left) + " " + ("attempts" if attempts_left > 1 else "attempt")
        + ".\n")
      if answer == get_dialogue(dialogue, language):
        print("Correct!\n")
        break
      else:
        attempts_left -= 1
        if attempts_left > 0:
          print("Wrong, please try again.\n")
        else:
          wrong.append(dialogue)
          print("Wrong, the correct answer was \""
            + get_dialogue(dialogue, language) + "\"\n")
    attempts_left = attempts

  print("You're done. You got", str(len(filtered) - len(wrong)), "out of",
    len(filtered), "correct.")

  print("These are the lines you got wrong. Be sure to study them.\n")
  for dialogue in wrong:
    print(dialogue.get_speaker() + ":")
    print(get_dialogue(dialogue, Language.ENGLISH))
    print(get_dialogue(dialogue, Language.CHINESE) + "\n")

def filter_dialogues(dialogues: List[Dialogue], speakers: List[str]) -> List[Dialogue]:
  """
  Filters out only the dialogues that include the given speakers. If speakers is
  an empty list, then the dialogues are returned without any changes.

  Arguments:
    - dialogues: The list of dialogues.
    - speakers: The list of speakers to filter by.

  Returns: The filtered list of dialogues.

  Errors: If the speaker results in the filter returning no dialogues.
  """
  if speakers == []:
    return dialogues
  else:
    speakers_lower: List[str] = list(
      map((lambda speaker: speaker.lower()), speakers))
    result: List[Dialogue] = list(
      filter((lambda dialogue: dialogue.get_speaker().lower() in speakers_lower),
        dialogues))
    if result == []:
      error("No lines with that speaker found. Check your arguments for typos.")
      exit(0)
    else:
      return result

def get_dialogue(dialogue: Dialogue, language: Language) -> str:
  """
  A function to retrieve the dialogue of the given language.

  Arguments:
    - dialogue: The dialogue.
    - language: The language of the dialogue to retrieve.

  Returns: The dialogue of the given language.

  Errors: If an invalid or unsupported language is given.
  """
  if language == Language.ENGLISH:
    return dialogue.get_english()
  elif language == Language.CHINESE:
    return dialogue.get_chinese()
  else:
    error("Invalid language given to get_dialogue().")
    exit(0)

def other_language(language: Language) -> Language:
  """
  A function that probably won't work out well in the long term. If the given
  language is English, this function returns Chinese and vice-versa.

  Arguments:
    - language: The language.

  Returns: The opposite language as described in this functions' description.
  """
  return Language.CHINESE if language == Language.ENGLISH else Language.ENGLISH

if __name__ == "__main__":
  parser: ArgumentParser = init_parser()
  args: vars = vars(parser.parse_args())

  path: str = args.get("path")
  attempts: int = args.get("attempts")
  language: Language = Language(args.get("language").lower())
  no_display: bool = args.get("no_display")
  speakers: List[str] = list(map(lambda speaker: speaker.lower(),
    args.get("speakers")))

  dialogues: List[Dialogue] = read_dialogues(path)
  quiz(dialogues, attempts, language, speakers, no_display)