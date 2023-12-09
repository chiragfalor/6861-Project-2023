import pandas as pd

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
    

class GameEvent(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

class GameQuery(TextToCode):
    def __init__(self, description, ppl_code) -> None:
        super().__init__(description, ppl_code)

class GameModel(TextToCode):
    def __init__(self, name, description, ppl_code, code_file_path=None) -> None:
        super().__init__(description, ppl_code)
        self.name = name
        if code_file_path:
            self.code_file_path = code_file_path
            self.tag = self.code_file_path.split('/')[-1].split('.')[0]
    
    @property
    def description(self):
        return self.text
    @description.setter
    def description(self, value):
        self.text = value

    def process_queries(self):
        df = self.queries_df
        def process_query(row) -> dict:
            all_moves = row['language_full']
            query = row['question_sentence']
            query_code = row['question_code']
            answer = row['answer']
            lang_phrase_list = []
            code_phrase_list = []
            query_list = []
            N_LANG_PHRASES = len(list(filter(lambda col_name: "language_phrase_" in col_name, df.columns)))
            N_CODE_PHRASES = len(list(filter(lambda col_name: "code_phrase_" in col_name, df.columns)))
            N_PHRASES = min(N_LANG_PHRASES, N_CODE_PHRASES)
            for i in range(1, N_PHRASES+1):
                lang_phrase = row[f'language_phrase_{i}']
                code_phrase = row[f'code_phrase_{i}']
                if pd.isna(lang_phrase):
                    break
                lang_phrase_list.append(lang_phrase)
                code_phrase_list.append(code_phrase)
                query_list.append(GameQuery(lang_phrase, code_phrase))
            return {'all_moves': all_moves,
                    'query': query,
                    'query_code': query_code,
                    'answer': answer,
                    'lang_phrase_list': lang_phrase_list,
                    'code_phrase_list': code_phrase_list,
                    'query_list': query_list}
        self.tasks = [process_query(row) for i, row in df.iterrows()]

    def __repr__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCode: {self.code}"


