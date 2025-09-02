INTEGER = "INTEGER"
FLOAT = "FLOAT"
INVALID = "INVALID"
UNDETERMINED = "UNDETERMINED"

BASE = "BASE"
EXPONENT = "EXPONENT"


class NumberState:
  def __init__(self):
    self.base_decimal_symbol = None
    self.base_exponent_symbol = None
    self.base_sign = None
    self.exponent_sign = None
    self.base_val = ""
    self.exponent_val = ""
    self.position = BASE

  def add_ch(self, ch):
    if ch in "Ee":
      if self.position != BASE:
        raise Exception("Already has exponent")
      # if self.exponent_val:
      if not self.base_val:
        raise Exception("Exponent with no base")
      self.base_exponent_symbol = ch
      self.position = EXPONENT
    elif ch in ".":
      if self.position == EXPONENT:
        raise Exception("Decimal exponent not allowed in this class")
      if self.base_decimal_symbol:
        raise Exception("Too many decimal symbols")
      self.base_decimal_symbol = ch
    elif ch in "-+":
      if self.position == EXPONENT:
        if self.exponent_sign:
          raise Exception("Too many exponent sign symbols")
        if self.exponent_val:
          raise Exception("Invalid placement of sign")
        self.exponent_sign = ch
      if self.position == BASE:
        if self.base_sign:
          raise Exception("Too many base sign symbols")
        if self.base_val or self.base_decimal_symbol:
          raise Exception("Invalid placement of sign")
        self.base_sign = ch
    elif ch not in "0123456789":
      raise Exception("Invalid character")
    elif self.position == BASE:
      self.base_val = True
    elif self.position == EXPONENT:
      self.exponent_val = True

  def is_valid(self):
    if self.base_val == "":
      return False
    if self.base_exponent_symbol and self.exponent_val == "":
      return False
    return True


class Solution:
  def isNumber(self, s: str) -> bool:
    number_state = NumberState()
    for ch in s:
      try:
        number_state.add_ch(ch)
      except Exception as e:
        print("excception", e)
        return False
    return number_state.is_valid()
