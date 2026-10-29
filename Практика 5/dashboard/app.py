import os
import requests
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Электронный журнал", page_icon="📚", layout="wide")
st.title("📚 Электронный журнал")
st.caption("Успеваемость, оценки и посещаемость учащихся")
api_url = st.sidebar.text_input("Адрес API", os.getenv("JOURNAL_API_URL","http://127.0.0.1:8000/api")).rstrip("/")
def get_api(path):
    try:
        r = requests.get(f"{api_url}/{path}", timeout=5)
        r.raise_for_status()
        return r.json(), None
    except requests.RequestException as exc:
        return None, str(exc)
summary, error = get_api("summary/")
if error:
    st.error("Не удалось получить данные. Запустите Django и выполните команду seed_demo.")
    st.code(error)
    st.stop()
c1,c2,c3,c4 = st.columns(4)
c1.metric("Учеников", summary["students"])
c2.metric("Предметов", summary["subjects"])
c3.metric("Оценок", summary["grades"])
c4.metric("Средний балл", summary["average_mark"])
left,right = st.columns(2)
with left:
    st.subheader("Последние оценки")
    recent = summary.get("recent_grades", [])
    if recent:
        df = pd.DataFrame(recent)
        df = df.rename(columns={"student_name":"Ученик","subject_name":"Предмет","mark":"Оценка","date":"Дата","comment":"Комментарий"})
        st.dataframe(df[[c for c in ["Ученик","Предмет","Оценка","Дата","Комментарий"] if c in df.columns]], use_container_width=True, hide_index=True)
    else:
        st.info("Оценок пока нет.")
with right:
    st.subheader("Успеваемость")
    if recent:
        grades = pd.DataFrame(recent)
        chart = grades.groupby("mark").size().reset_index(name="Количество")
        chart["Оценка"] = chart["mark"].astype(str)
        st.bar_chart(chart.set_index("Оценка")["Количество"])
    st.metric("Отсутствия", summary["absences"])
st.divider()
st.subheader("Разделы API")
st.markdown("- `/api/students/` — ученики\n- `/api/subjects/` — предметы\n- `/api/grades/` — оценки\n- `/api/attendance/` — посещаемость\n- `/api/summary/` — сводная статистика")
