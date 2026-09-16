import streamlit as st
import random

st.set_page_config(
    page_title="F1 응원팀 추천기",
    page_icon="🏎️"
)

st.title("🏎️ F1 응원 선수 & 팀 랜덤 추천")
st.write("버튼을 눌러 이번 시즌 응원할 선수를 찾아보세요!")

drivers = [
    "Max Verstappen",
    "Isack Hadjar",
    "Lando Norris",
    "Oscar Piastri",
    "Charles Leclerc",
    "Lewis Hamilton",
    "George Russell",
    "Kimi Antonelli",
    "Fernando Alonso",
    "Lance Stroll",
    "Carlos Sainz",
    "Alexander Albon",
    "Pierre Gasly",
    "Franco Colapinto",
    "Esteban Ocon",
    "Oliver Bearman",
    "Nico Hulkenberg",
    "Gabriel Bortoleto",
    "Liam Lawson",
    "Arvid Lindblad",
    "Sergio Perez",
    "Valtteri Bottas"
]

teams = [
    "Red Bull Racing",
    "McLaren",
    "Ferrari",
    "Mercedes",
    "Aston Martin",
    "Williams",
    "Alpine",
    "Haas",
    "Audi",
    "Racing Bulls",
    "Cadillac"
]

team_descriptions = {
    "Red Bull Racing": "공격적인 전략과 챔피언 DNA",
    "McLaren": "최근 최상위권 경쟁팀",
    "Ferrari": "F1의 전설적인 명문팀",
    "Mercedes": "기술력과 안정성의 상징",
    "Aston Martin": "도약을 노리는 야심가",
    "Williams": "역사 깊은 명가",
    "Alpine": "프랑스 워크스 팀",
    "Haas": "미국 대표 F1 팀",
    "Audi": "새 시대를 여는 제조사",
    "Racing Bulls": "유망주 육성 명가",
    "Cadillac": "신규 참가팀"
}

if st.button("🎲 랜덤 추천 받기"):
    driver = random.choice(drivers)
    team = random.choice(teams)

    st.success("추천 완료!")

    st.subheader("👨‍✈️ 추천 선수")
    st.write(driver)

    st.subheader("🏁 추천 팀")
    st.write(team)

    st.info(team_descriptions[team])

st.divider()

st.caption("마음에 안 들면 다시 돌리세요 😎")
