#
import csv
from openai import OpenAI
import gradio as gr
import os
import random
import pandas as pd
from datetime import datetime
from cryptography.fernet import Fernet
from huggingface_hub import Repository
from datasets import load_dataset
from hashlib import blake2b

os.system('git config --global user.name "Kevin Gold"')
os.system('git config --global user.email "klgold@bu.edu"')

MODEL = "o1-mini"

client = OpenAI(
    api_key=os.getenv('openai_key'),
)
# Dataset code follows example at:
# https://huggingface.co/spaces/julien-c/persistent-data/blob/main/app.py
DATASET_REPO_URL = "https://huggingface.co/datasets/klgold/ds110practicelogs"
DATA_FILENAME = "data.csv"
DATA_FILE = os.path.join("data", DATA_FILENAME)
HF_TOKEN=os.environ.get("HF_TOKEN")
PROFILES_URL = "https://huggingface.co/datasets/klgold/tutor_profiles"
PROMPT_PREFIX="Give me a practice problem for an introductory course in python and data science that uses the following concepts: "
prefix_length = len(PROMPT_PREFIX)
PROMPT_SUFFIX = """The first section of your response should say "PROBLEM" followed by the problem.  The second section of your response should say "SOLUTION" before the Python code that solves the problem.  The solution must be simple,
because this is practice for an exam where students will have limited time.  Additionally, all 
Python keywords, syntax, and concepts that you use in the solution must 
be drawn from the following code from lecture:"""
with open('master.py', 'r') as pythonfile:
    PROMPT_SUFFIX += pythonfile.read()
suffix_length = len(PROMPT_SUFFIX)
#Currently get error on trying to create Repository - need email?
repo = Repository(
    local_dir="data", clone_from=DATASET_REPO_URL, use_auth_token=HF_TOKEN
)
name = None

def store_transcript(is_ai: bool, transcript: str, state):
    with open(DATA_FILE, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, 
                        fieldnames=['session','is_ai','transcript', 'time'])
        writer.writerow(
            {'session': state.username + '-' + str(state.session),
             'is_ai':str(is_ai), 
             'transcript': transcript, 'time': str(datetime.now())}
        )
    # Correct for network hiccups that get git out of sync
    try:
        commit_url = repo.push_to_hub()
    except:
        repo.git_pull()
        commit_url = repo.push_to_hub()

class SessionState:
    def __init__(self):
        self.session = 0
        self.messages = []
        self.username = "unknown"
        self.problem = ""
        self.solution = ""

def continue_session(state, 
                if_checkbox,
                lists_checkbox,
                while_checkbox,
                boolean_checkbox,
                for_checkbox,
                nested_checkbox,
                function_checkbox,
                dict_checkbox,
                matplotlib_checkbox,
                numpy_checkbox,
                pandas_checkbox,
                regex_checkbox,
                files_and_exceptions_checkbox,
                oo_checkbox,
                recursion_checkbox,
                graphs_checkbox,
                request: gr.Request):
    if not state.messages:
        state.session = random.randint(1,999999)
        state.messages = [
            {"role": "user", "content": "You are writing practice programming problems for students in an introductory Python programming course.  Your primary goal is to help students study for the midterm by providing these practice problems."}
        ]
        #profile_dataset = load_dataset("csv", data_files="https://huggingface.co/datasets/klgold/tutor_profiles/raw/main/S24hashed.csv", token=HF_TOKEN)
        #profile_df = pd.DataFrame(profile_dataset['train'])
        #profile_df = profile_df.set_index('user')
        state.username = request.username

    content = PROMPT_PREFIX
    # TODO:  Set the topics
    topics = make_topics_list(if_checkbox,
                lists_checkbox,
                while_checkbox,
                boolean_checkbox,
                for_checkbox,
                nested_checkbox,
                function_checkbox,
                dict_checkbox,
                matplotlib_checkbox,
                numpy_checkbox,
                pandas_checkbox,
                regex_checkbox,
                files_and_exceptions_checkbox,
                oo_checkbox,
                recursion_checkbox,
                graphs_checkbox)
    content += topics
    content += PROMPT_SUFFIX
    state.messages.append({"role": "user", "content": content})
    store_transcript(False, topics, state)

    response = client.chat.completions.create(
        model=MODEL,
        messages=state.messages
    )
    chat_response = response.choices[0].message.content
    response = client.chat.completions.create(
        model = MODEL,
        messages = state.messages, 
        stream=True
    )
    last_message = ""
    to_display = ""
    for chunk in response:
        streamed = chunk.choices[0].delta.content
        if streamed is not None:
            last_message += streamed
        # Don't display solution while streaming
        if "SOLUTION" in last_message:
            sol_index = last_message.index("SOLUTION")
            to_display = last_message[:sol_index]
        else:
            to_display = last_message
        problem_box.value = to_display
        yield {problem_box: to_display, state_var: state}
    state.messages.append({"role":"assistant", "content": last_message})
    store_transcript(True, last_message, state)

    state.problem, state.solution = parse_reply(last_message)

    # There's no concept of a chat history in this app,
    # so we need to clear the messages history to avoid window overflow
    state.messages = []

    # DEBUG Replace transcript with state.messages for debugging
    yield {problem_box: state.problem, state_var: state}

def make_topics_list(if_checkbox,
                lists_checkbox,
                while_checkbox,
                boolean_checkbox,
                for_checkbox,
                nested_checkbox,
                function_checkbox,
                dict_checkbox,
                matplotlib_checkbox,
                numpy_checkbox,
                pandas_checkbox,
                regex_checkbox,
                files_and_exceptions_checkbox,
                oo_checkbox,
                recursion_checkbox,
                graphs_checkbox):

    topics = []
    if if_checkbox:
        topics.append("if/elif/else")
    if lists_checkbox:
        topics.append("lists")
    if while_checkbox:
        topics.append("while")
    if boolean_checkbox:
        topics.append("boolean operators")
    if for_checkbox:
        topics.append("for loops")
    if nested_checkbox:
        topics.append("nested loops")
    if function_checkbox:
        topics.append("functions")
    if dict_checkbox:
        topics.append("sets or dictionaries")
    if matplotlib_checkbox:
        topics.append("matplotlib")
    if numpy_checkbox:
        topics.append("numpy")
    if pandas_checkbox:
        topics.append("pandas")
    if regex_checkbox:
        topics.append("regular expressions")
    if files_and_exceptions_checkbox:
        topics.append("files and exceptions")
    if oo_checkbox:
        topics.append("object-oriented programming")
    if recursion_checkbox:
        topics.append("recursion")
    if graphs_checkbox:
        topics.append("graphs")

    return ",".join(topics) + '.'

def to_transcript(messages, prefix_length, suffix_length):
    transcript = ''
    for d in messages:
        if d['role'] == 'user':
            prompt = d['content']
            # Need to remove the extra prompt verbiage
            transcript += '\nUser: ' + prompt[prefix_length:-suffix_length]
        elif d['role'] == 'assistant':
            transcript += '\nAI: ' + d['content']
    return transcript

def comment_on_code(user_input, state):
    prompt = "You must must now judge whether the student's supplied answer is a Python program that correctly answered the prompt.  The prompt was:\n"
    prompt += state.problem 
    prompt += "\n\n"
    prompt += "If the student's answer works, congratulate them.  If not, point out where "
    prompt += "they went wrong and explain the relevant Python concept."
    # ...
    state.messages.append({"role": "user", "content":  prompt})
    state.messages.append({"role": "user", "content": user_input})
    store_transcript(False, user_input, state)
    response = client.chat.completions.create(
        model = MODEL,
        messages = state.messages, 
        stream=True
    )
    last_message = ""
    for chunk in response:
        streamed = chunk.choices[0].delta.content
        if streamed is not None:
            last_message += streamed
        response_box.value = last_message
        yield {response_box: last_message, state_var: state}
    state.messages.append({"role":"assistant", "content": last_message})
    store_transcript(True, last_message, state)
    yield {response_box: last_message, state_var: state}

            

def my_hash(text):
    h = blake2b()
    h.update(bytes(text,'utf-8'))
    return h.hexdigest()

def authenticate(username, password):
    # profile_dataset = load_dataset("csv", data_files="https://huggingface.co/datasets/klgold/tutor_profiles/raw/main/S25hashed.csv", token=HF_TOKEN)
    profile_dataset = load_dataset("klgold/tutor_profiles", data_files={"train":"F25hashed.csv"}, token=HF_TOKEN)
    profile_df = pd.DataFrame(profile_dataset['train'])
    profile_df = profile_df.set_index('Username')
    if not username in profile_df.index:
        return False
    hashed_pass = my_hash(password)

    return str(profile_df.loc[username, 'hash']) == str(hashed_pass)

def parse_reply(reply):
    problem_index = reply.find("PROBLEM")
    sol_index = reply.find("SOLUTION")
    # Not totally confident these parts will be delivered in the right
    # order, but starting with the problem seems very likely.
    return reply[problem_index + len('PROBLEM')+2:sol_index], \
           reply[sol_index + len('SOLUTION')+2:]

with gr.Blocks() as demo:
    state_var = gr.State(SessionState())
    transcript_var = gr.State('')
    transcript_fn_var = gr.State('')
    with gr.Accordion('Midterm 1 Topics'):
        with gr.Row():
            if_checkbox = gr.Checkbox(label='If')
            lists_checkbox = gr.Checkbox(label='Lists')
            while_checkbox = gr.Checkbox(label='While')
            boolean_checkbox = gr.Checkbox(label='Boolean Operators')
            for_checkbox = gr.Checkbox(label='For Loops')
        with gr.Row():
            nested_checkbox = gr.Checkbox(label='Nested Loops')
            function_checkbox = gr.Checkbox(label='Functions')
            dict_checkbox = gr.Checkbox(label='Sets or Dictionaries')
            matplotlib_checkbox = gr.Checkbox(label='matplotlib')
            numpy_checkbox = gr.Checkbox(label='numpy')
    with gr.Accordion('Midterm 2 Topics'):
        with gr.Row():
            pandas_checkbox = gr.Checkbox(label='pandas')
            regex_checkbox = gr.Checkbox(label='Regular Expressions')
            files_and_exceptions_checkbox = gr.Checkbox(label='Files and Exceptions')
        with gr.Row():
            oo_checkbox = gr.Checkbox(label='Object-oriented Python')
            recursion_checkbox = gr.Checkbox(label='Recursion')
            graphs_checkbox = gr.Checkbox(label='Graphs')
    response_button = gr.Button('Generate Problem')
    problem_box = gr.Textbox(lines=7, label='Problem')
    response_button.click(fn=continue_session, 
        inputs=[state_var,
                if_checkbox,
                lists_checkbox,
                while_checkbox,
                boolean_checkbox,
                for_checkbox,
                nested_checkbox,
                function_checkbox,
                dict_checkbox,
                matplotlib_checkbox,
                numpy_checkbox,
                pandas_checkbox,
                regex_checkbox,
                files_and_exceptions_checkbox,
                oo_checkbox,
                recursion_checkbox,
                graphs_checkbox],
        outputs=[problem_box, state_var])
    user_input = gr.Textbox(lines=20, label='Your Code Here')
    with gr.Row():
        submit_button = gr.Button('Try My Solution')
    response_box = gr.Textbox(lines=20, label='Feedback')
    submit_button.click(fn=comment_on_code, inputs=[user_input, state_var], 
                        outputs=[response_box, state_var])

#demo.launch()
demo.launch(auth=authenticate)
