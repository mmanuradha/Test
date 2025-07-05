import streamlit as st

# Set page title
st.set_page_config(page_title="Student Quiz App")

st.title("🎓 Student General Knowledge Quiz")

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Leo Tolstoy", "William Shakespeare", "Mark Twain", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["India", "China", "Egypt", "Mexico"],
        "answer": "China"
    }
]

# Session state to keep track
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Quiz form
with st.form("quiz_form"):
    st.write("### Answer the following questions:")
    user_answers = []
    for idx, q in enumerate(questions):
        user_answer = st.radio(q["question"], q["options"], key=idx)
        user_answers.append(user_answer)
    submitted = st.form_submit_button("Submit Answers")

# Score evaluation
if submitted and not st.session_state.submitted:
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
    st.session_state.score = score
    st.session_state.submitted = True

# Show score
if st.session_state.submitted:
    st.success("You scored {st.session_state.score} out of {len(questions)}!")
    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.submitted = False
        st.experimental_rerun()