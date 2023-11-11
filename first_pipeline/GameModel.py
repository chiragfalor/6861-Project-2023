class TextToCode:
    def __init__(self, description, ppl_code) -> None:
        self.text = description
        self.code = ppl_code

    def __repr__(self) -> str:
        return f"Text: {self.text}\nCode: {self.code}"

class GameModel(TextToCode):
    def __init__(self, name, description, ppl_code) -> None:
        super().__init__(description, ppl_code)
        self.name = name

    def __repr__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.text}\nCode: {self.code}"

class GameEvent(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

class GameQuery(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

