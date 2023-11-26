class TextToCode:
    def __init__(self, text, ppl_code) -> None:
        self.text = text
        self.code = ppl_code

    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        self._code = value

    def __repr__(self) -> str:
        return f"Text: {self.text}\nCode: {self.code}"

class GameModel(TextToCode):
    def __init__(self, name, description, ppl_code, code_file_path=None) -> None:
        super().__init__(description, ppl_code)
        self.name = name
        if code_file_path:
            self.code_file_path = code_file_path
    
    @property
    def description(self):
        return self.text
    @description.setter
    def description(self, value):
        self.text = value

    def __repr__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCode: {self.code}"

class GameEvent(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

class GameQuery(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

