import streamlit as st

# --- App setup ---
st.set_page_config(page_title="Learning Platform Prototype", layout="centered")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Courses", "My Progress"])

# --- Sample data ---
courses = {
    "Python Basics": [
        {"title": "Introduction to Python", "content": "Learn what Python is, why it's used, and how to install it."},
        {"title": "Variables and Data Types", "content": "Understand numbers, strings, lists, and dictionaries."},
        {"title": "Control Flow", "content": "Learn about if statements, loops, and logical operators."}
    ],
    "Data Analysis": [
        {"title": "Intro to Pandas", "content": "Pandas is a library for data analysis and manipulation."},
        {"title": "Working with CSV files", "content": "Learn to read and write data using pandas.read_csv()."}
    ]
}

# --- State tracking ---
if "progress" not in st.session_state:
    st.session_state.progress = {course: [False] * len(lessons) for course, lessons in courses.items()}

# --- Pages ---
if page == "Home":
    st.title("🎓 Simple Learning Platform")
    st.write("Welcome to this prototype learning platform built with Streamlit.")
    st.info("Use the sidebar to explore courses and track your progress.")

elif page == "Courses":
    st.title("📘 Available Courses")
    course_choice = st.selectbox("Select a course", list(courses.keys()))

    lessons = courses[course_choice]
    st.subheader(course_choice)

    for i, lesson in enumerate(lessons):
        with st.expander(f"Lesson {i+1}: {lesson['title']}"):
            st.write(lesson["content"])
            if not st.session_state.progress[course_choice][i]:
                if st.button(f"Mark '{lesson['title']}' complete", key=f"{course_choice}_{i}"):
                    st.session_state.progress[course_choice][i] = True
                    st.success("Lesson marked complete ✅")
            else:
                st.success("Completed ✅")

elif page == "My Progress":
    st.title("📊 Your Progress")
    for course, lessons in st.session_state.progress.items():
        completed = sum(lessons)
        total = len(lessons)
        percent = (completed / total) * 100
        st.subheader(course)
        st.progress(percent / 100)
        st.write(f"{completed}/{total} lessons completed ({percent:.0f}%)")
