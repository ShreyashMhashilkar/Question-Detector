from nltk.tokenize import word_tokenize

def detectQuestion(question):
    question_words = ["what", "why", "when", "where", 
                "name", "is", "how", "do", "does", 
                "which", "are", "could", "would", 
                "should", "has", "have", "whom", "whose", "don't"]

    question = question.lower()
    question = word_tokenize(question)

    if any(x in question[0] for x in question_words):
        return "This is a question!"
    else:
        return "This is not a question!"