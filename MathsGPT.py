import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler



#GROQ_API_KEY="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"
#api_key=GROQ_API_KEY
#llm=ChatGroq(groq_api_key=api_key,model="Gemma-7b-It")


## streamlit app set up
st.set_page_config(page_title="Text to Maths Problem Solver And Data Search Assistant")
st.title("Text to Math Problem Solver Using Google Gemma 2")

GROQ_API_KEY="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"
groq_api_key=st.sidebar.text_input(label="GROQ_API_KEY",type="password")

if not groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

llm = ChatGroq(model="Gemma2-9b-It",groq_api_key="GROQ_API_KEY")

## Initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find the various information on the topic mentioned"

)

## Initialized the Math Tool

math_chain = LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tools for answering math related questions. Only input mathematical expression needs to be provided"

)
prompt='''
You are a agent tasked for solving users mathematical questions. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question : {question}
Answer:
'''

prompt_template=PromptTemplate(
    input_variables = ["question"],
    template=prompt
)

## Combine all the tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## Initialized the agents

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a Math chatbot who can answer all your maths questions"}
    ]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## function to generate the response
def generate_response(question):
    response=assistant_agent.invoke({'input':question})
    return response

## Let's start the Interactions
question=st.text_area("Enter your question:","ax+by+c=0")
if st.button("find my answer"):
    if question:
        with st.spinner("Generate response...."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({'role':'assistant','content':response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")



"""
I have 5 bananas and 7 grapes, I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples
and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces 
of fruits do I have at the end?
"""