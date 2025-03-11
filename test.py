from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
g-dragon
"""

if __name__ == '__main__':
    print("hello LangChain!")
    
    summary_template = """
        given the information P{information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, tiktoken_model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)