
# Maths Problem Solver

Innovative Math and Data Search Assistant Using Google Gemma2. Google Gemma2 is another open source model from Google,which is quite amazing with LLM.

Whatever question you asked this GPT related to any maths Problem it should be give you a answer along with reasoning behind it.You can ask formula also e.g (What is the formula to calculate area of Square) or (What is pi r^2)

We are integrating MathGPT with Wikipedia


# Documentation 

[LLMMathChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_math.base.LLMMathChain.html)

Chain that interprets a prompt and executes python code to do math.Because LLMs have limitations when it comes to mathematics. The reasons being:

* Lack of Inherent Math Knowledge: LLMs are primarily trained on large text corpora and lack inherent mathematical knowledge. They do not have an understanding of mathematical concepts as humans do.

* Single Correct Answer Requirement: Math problems typically have a single correct answer, making it challenging for LLMs to generate accurate solutions consistently.

* Focus on Language Generation: LLMs are designed for language generation and may not inherently perform mathematical calculations. They aim to predict the next word or token in a sequence rather than solve mathematical equations.

* Need for Explicit Instructions: To make LLMs perform mathematical tasks, users often need to provide explicit instructions and frame problems in a way that LLMs can understand. 





 








## Important Libraries Used

 - [LLMMathChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_math.base.LLMMathChain.html#)
 - [Prompt Template](https://python.langchain.com/v0.1/docs/integrations/llms/deepinfra/#create-a-prompt-template)
- [ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)
 - [WikipediaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wikipedia.WikipediaAPIWrapper.html)
 - [Agent Types](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/)





## Plateform or Providers

 - [LangChain-ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)
 - [Streamlit](https://docs.streamlit.io/)

## Model

 - LLM - Gemma2-9b-It


## Installation

Install below libraries

```bash
  pip install langchain
  pip install langchain_community
  pip install streamlit
  pip install langchain-groq
  pip install wikipedia

```
    
## Tech Stack

**Client:** Python, LangChain PromptTemplate, ChatGroq

**Server:** Streamlit, LangChain,Groq


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`GROQ_API_KEY`


## Examples
Initializing the tools
```javascript
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find the various information on the topic mentioned"

)
```

## Initialized the Math Tool

```javascript
from langchain.chains import LLMMathChain,LLMChain


math_chain = LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tools for answering math related questions. Only input mathematical expression needs to be provided"

) 
```


## Input

Question asked by MathGPT:

- A box contains 2 apples, 3 mangoes, and 2 bananas. Two fruits are drawn at random. What is the probability that none of the fruits drawn is a banana
- Find the diameter of a circle whose center is (3,8) and passes through (4,9)
- I have 5 bananas and 7 grapes, I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries.Each pack of blueberries contains 25 berries. How many total pieces of fruits do I have at the end?

