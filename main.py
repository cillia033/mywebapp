import streamlit as st

st.set_page_config(
    page_title="MBTI F1 추천기",
    page_icon="🏎️"
)

st.title("🏎️ MBTI 기반 F1 응원 추천")
st.write("MBTI를 선택하면 어울리는 F1 선수와 팀을 추천해드립니다.")

recommendations = {
    "INTJ": ("Max Verstappen", "Red Bull Racing", "분석적이고 목표 지향적인 전략가 타입"),
    "INTP": ("Oscar Piastri", "McLaren", "논리적이고 침착하게 상황을 분석하는 타입"),
    "ENTJ": ("Lewis Hamilton", "Ferrari", "강한 리더십과 승부욕을 가진 타입"),
    "ENTP": ("Fernando Alonso", "Aston Martin", "창의적이고 예측 불가능한 전략가 타입"),

    "INFJ": ("Charles Leclerc", "Ferrari", "이상과 열정을 추구하는 타입"),
    "INFP": ("Alexander Albon", "Williams", "진정성과 성장을 중시하는 타입"),
    "ENFJ": ("Lando Norris", "McLaren", "사람들과 잘 어울리고 긍정적인 타입"),
    "ENFP": ("Daniel Ricciardo", "RB", "에너지 넘치고 자유로운 분위기의 타입"),

    "ISTJ": ("George Russell", "Mercedes", "성실하고 체계적인 타입"),
    "ISFJ": ("Carlos Sainz", "Williams", "꾸준하고 신뢰를 주는 타입"),
    "ESTJ": ("Toto Wolff", "Mercedes", "조직을 이끄는 관리자형"),
    "ESFJ": ("Pierre Gasly", "Alpine", "팀워크와 관계를 중시하는 타입"),

    "ISTP": ("Kimi Antonelli", "Mercedes", "실용적이고 냉철한 문제 해결형"),
    "ISFP": ("Yuki Tsunoda", "Red Bull Racing", "자유롭고 개성 있는 타입"),
    "ESTP": ("Liam Lawson", "Racing Bulls", "도전과 경쟁을 즐기는 타입"),
    "ESFP": ("Franco Colapinto", "Alpine", "활발하고 즐거움을 추구하는 타입")
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(recommendations.keys())
)

if st.button("🏁 추천받기"):
    driver, team, reason = recommendations[mbti]

    st.subheader("👨‍✈️ 추천 드라이버")
    st.success(driver)

    st.subheader("🏎️ 추천 팀")
    st.success(team)

    st.subheader("💡 추천 이유")
    st.write(reason)

st.divider()
st.caption("※ 재미로 보는 추천입니다.")
