from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model='llama3.2')

template = '''you are an expert in answering question about a pizza restutrent 

Here are some relevant reviews: {reviews}

Here is the question to answer: {Question}
'''
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print('\n\n--------------------------------------')
    Question = input('Askyour Question (q to quit): ')
    print('\n\n')
    if Question == 'q':
        break
    
    reviews = retriver.invoke(Question)
    result = chain.invoke({'reviews': [], 'Question':'what is the best pizza place in the town'})
    print(result)