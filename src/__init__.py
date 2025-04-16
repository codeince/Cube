from time import time
from string import punctuation
punctuation = punctuation.replace('#', '')
from random import choice, randint, seed

def capitalize(text: str) -> str:
    return text[0].upper() + text[1:]

class Answer:
    def __init__(self, question: str, answer: str):
        question = question.strip(' \n\t\r')
        self.question = capitalize(question if question.endswith('?') else f'{question}?')
        self.answer = capitalize(answer)
    
    def to_str(self, formatting: str = 'Question: {question}\nAnswer: {answer}') -> str:
        return formatting.format(question=self.question, answer=self.answer)
    
    def __dict__(self) -> dict:
        return {'question': self.question, 'answer': self.answer}
    
class Cube(list[Answer]):
    def __init__(self, lang_build: dict, answers: dict, seed_: int = None):
        super().__init__()
        self.lang = lang_build
        self.answers = answers
        self.seed = seed_ if isinstance(seed_, int) else int(time())
        seed(self.seed)
        self.init_txt()

    def init_txt(self):
        print(self.lang.get('init_text'))
        print(self.lang.get('model_text').format(seed=self.seed))

    def ask(self, question: str) -> str:
        if len(question.translate(str.maketrans('', '', punctuation+'#'))) == 0: return ''
        answer = self._generate_answer(question)
        self.append(answer)
        return answer.answer
    
    def _generate_answer(self, question: str) -> str:
        q = question.lower().translate(str.maketrans(' ', ' ', punctuation))

        for answer_type in self.answers.values():
            if True in [True for word in q.split() if word in answer_type.get('masks')]:
                result = capitalize(choice(answer_type.get('answers')))
                break
        else:
            result = capitalize(choice(self.answers.get('default').get('answers')))
        
        if result.find("%rand%") != -1:
            result_list = result.split('%rand%')
            result = result_list[0]
            for i in result_list[1:]:
                result = str(randint(0, 100)).join((result, i))

        return Answer(question, result)

    def to_str(self, formatting: str = 'Question: {question}\nAnswer: {answer}') -> str:
        return '\n\n'.join(answer.to_str(formatting) for answer in self)