from abc import abstractmethod, ABC, ABCMeta

class Dialogue(ABC):
  """
  An interface representing a generic line of dialogue with a speaker, plus
  English and Chinese versions.
  """
  __metaclass__ = ABCMeta

  @abstractmethod
  def get_speaker(self) -> str:
    """
    Returns: The speaker of this dialogue.
    """
    return ""

  @abstractmethod
  def get_english(self) -> str:
    """
    Returns: This dialogue in English.
    """
    return ""

  @abstractmethod
  def get_chinese(self) -> str:
    """
    Returns: This dialogue in Chinese.
    """
    return ""