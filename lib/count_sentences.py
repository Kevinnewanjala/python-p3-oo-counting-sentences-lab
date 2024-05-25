class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, stringVal):
        if isinstance(stringVal, str):
            self._value = stringVal
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Replace question marks and exclamation marks with periods
        cleaned_value = self._value.replace('?', '.').replace('!', '.')
        # Split the cleaned value into sentences based on periods
        sentences = [sentence.strip() for sentence in cleaned_value.split('.') if sentence.strip()]
        return len(sentences)
