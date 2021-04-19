from dialogue.idialogue import Dialogue
from logging import error

class DialogueImpl(Dialogue):
  """
  A generic implementation of the Dialogue interface, which depicts the speaker,
  English, and Chinese versions of the dialogue as strings.
  """

  def __init__(self, speaker: str, english: str, chinese: str) -> None:
    """
    Constructs a DialogueImpl instance from a given speaker, and English and
    Chinese versions of the dialogue. Chinese can ultimately be any string, but
    I recommend that they are inputted in Hanzi (characters) or Pinyin
    (romanization).

    Arguments:
      - speaker: The speaker of this dialogue.
      - english: The English version of this dialogue.
      - chinese: The Chinese version of this dialogue.
    """
    self.validate_args(speaker, english, chinese)
    self.speaker: str = speaker
    self.english: str = english
    self.chinese: str = chinese

  # Helper
  def validate_args(self, speaker: str, english: str, chinese: str) -> None:
    """
    Validates the arguments for the constructor, ensuring that none of them are
    empty strings.
    
    Arguments:
      - speaker: The speaker of this dialogue.
      - english: The English version of this dialogue.
      - chinese: The Chinese version of this dialogue.
    """
    if speaker == "" or english == "" or chinese == "":
      to_print: str = ("Did not expect {} to be an empty line. Did you format "
        + "your script properly?")
      print(speaker)
      if speaker == "":
        to_print = to_print.format("the speaker")
      elif english == "":
        to_print = to_print.format("the English dialogue")
      else:
        to_print = to_print.format("the Chinese dialogue")
      error(to_print)
      exit(0)

  # Override
  def get_speaker(self) -> str:
    return self.speaker

  # Override
  def get_english(self) -> str:
    return self.english

  # Override
  def get_chinese(self) -> str:
    return self.chinese