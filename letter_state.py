class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.in_word: bool = False
        self.in_position: bool = False
        
    def __repr__(self) -> str:
        return f'[{self.character} in_word: {self.in_word} in_position: {self.in_position}]'