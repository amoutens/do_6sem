from typing import List
from typing import Callable

class Option():
    text: str
    key: str
    action: Callable[[], any]
    
    def __init__(self, text: str, key: str, action: Callable[[], any]):
        self.text = text
        self.key = key
        self.action = action

class Menu():
    header: str
    options: dict[str, 'Option']
    
    def __init__(self, header: str, options: List[Option]):
        self.header = header
        self.options = options
            
    def display(self):
        print(self.header)
        print()
        for option in self.options:
            print(option.text)
        
    def listenKey(self):
        while True:
            key = input()
            if key in [option.key for option in self.options]:
                return key
            print("Invalid option. Please try again.")
    
    def useOption(self, key: str):
        for option in self.options:
            if option.key == key:
                return option.action()