from dotenv import load_dotenv
from typing import Annotated,List
from langgraph.graph import stateGraph,START,END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from pydantic import BaseModel,Field

# we loaded environment variables from a .env file
load_dotenv()

# initialize the chat model
llm =init_chat_model("gpt-4o")

# inital state definitionx
class State(TypedDict):
    messages:Annotated[List, add_messages]
    user_question: str | None
    google_result: str | None
    bing_result: str | None
    bing_result: str | None
    selected_reddit_urls: list[str] | None
    reddit_post_data: list | None
    google_analysis: str | None
    bing_analysis: str | None
    reddit_analysis: str | None
    final_answer: str | None



# different operations in the graph
def google_search(state: State):
    return


def bing_search(state: State):
    return


def reddit_search(state: State):
    return


def analyze_reddit_posts(state: State):
    return


def retrieve_reddit_post(state: State):
    return


def analyze_google_results(state: State):
    return


def analyze_bing_results(state: State):
    return


def analyze_reddit_results(state: State):
    return


def sythesize_analyses(state: State):
    return

# we create the graph
graph_builder = stateGraph(State)

# adding nodes to the graph
graph_builder.add_node("google_search",google_search)
graph_builder.add_node("bing_search",bing_search)
graph_builder.add_node("reddit_search",reddit_search)
graph_builder.add_node("analyze_reddit_posts",analyze_reddit_posts)
graph_builder.add_node("analyze_google_results",analyze_google_results)
graph_builder.add_node("analyze_bing_results",analyze_bing_results)
graph_builder.add_node("analyze_reddit_results",analyze_reddit_results)
graph_builder.add_node("sythesize_analyses",sythesize_analyses)


# adding edges to the graph
graph_builder.add_edge(START,"google_search")
graph_builder.add_edge(START,"bing_search")
graph_builder.add_edge(START,"reddit_search")

graph_builder.add_edge("google_search","analyze_reddit_posts")
graph_builder.add_edge("bing_search","analyze_reddit_posts")
graph_builder.add_edge("reddit_search","analyze_reddit_posts")
graph_builder.add_edge("analyze_reddit_posts","retrieve_reddit_posts")

graph_builder.add_edge("retrieve_reddit_posts","analyze_google_results")
graph_builder.add_edge("retrieve_reddit_posts","analyze_bing_results")
graph_builder.add_edge("retrieve_reddit_posts","analyze_reddit_results")


graph_builder.add_edge("analyze_google_results","synthesize_analyses")
graph_builder.add_edge("analyze_bing_results","synthesize_analyses")
graph_builder.add_edge("analyze_reddit_results","synthesize_analyses")


graph_builder.add_edge("synthesize_analyses",END)


graph=graph_builder.compile()



# it runs the graph in a loop according to the user input
def run_chat_bot():
    print("Multi-source Research Agent")
    print("Type 'exit' to quit")

    while True:
        user_input = input("Ask me anything:")
        if user_input.lower() == 'exit':
            print("bye")
            break

        state = {
            "messages": [{"role":"user","content":user_input}],
            "user_question": user_input,
            "google_result": None,
            "bing_result": None,
            "reddit_result": None,
            "selected_reddit_urls": None,
            "reddit_post_data": None,
            "google_analysis": None,
            "bing_analysis": None,
            "reddit_analysis": None,
            "final_answer": None
        }
        print("\n Starting parallel research...")
        print("Launching Google ,Bing and Reddit searches...\n")
        final_state=graph.invoke(state)

        if final_state.get("final_answer"):
            print(f"\n Final Answer: \n{final_state.get('final_answer')}\n")

        print("-"* 80)
 

if __name__== "__main__":
    run_chat_bot()


 
