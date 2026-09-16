import streamlit as st

st.set_page_config(page_title="MBTI 여행지 추천", page_icon="✈️")

st.title("✈️ MBTI 여행지 추천")
st.write("당신의 MBTI를 선택하면 어울리는 여행지를 추천해드립니다.")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

travel_recommendations = {
    "INTJ": ("아이슬란드", "조용한 자연 속에서 깊이 있는 탐험을 즐길 수 있습니다."),
    "INTP": ("일본 도쿄", "다양한 문화와 기술을 탐구하기 좋습니다."),
    "ENTJ": ("싱가포르", "효율적이고 현대적인 도시 환경을 경험할 수 있습니다."),
    "ENTP": ("뉴욕", "새로운 사람과 아이디어를 만날 기회가 많습니다."),
    "INFJ": ("스위스", "아름다운 풍경과 평화로운 분위기를 즐길 수 있습니다."),
    "INFP": ("프라하", "감성적인 분위기와 예술적 매력이 가득합니다."),
    "ENFJ": ("파리", "사람들과 교류하며 문화생활을 즐기기 좋습니다."),
    "ENFP": ("바르셀로나", "활기찬 분위기와 자유로운 여행을 즐길 수 있습니다."),
    "ISTJ": ("독일 베를린", "체계적인 여행과 역사 탐방에 적합합니다."),
    "ISFJ": ("교토", "전통과 차분한 분위기를 느낄 수 있습니다."),
    "ESTJ": ("런던", "다양한 명소를 계획적으로 둘러보기 좋습니다."),
    "ESFJ": ("서울", "맛집과 다양한 활동을 친구들과 즐기기 좋습니다."),
    "ISTP": ("뉴질랜드", "액티비티와 자연 탐험을 즐길 수 있습니다."),
    "ISFP": ("발리", "여유로운 휴식과 아름다운 풍경을 경험할 수 있습니다."),
    "ESTP": ("두바이", "역동적이고 화려한 경험을 즐길 수 있습니다."),
    "ESFP": ("하와이", "즐거운 분위기와 다양한 레저 활동이 가능합니다.")
}

selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("여행지 추천받기"):
    place, reason = travel_recommendations[selected_mbti]

    st.success(f"추천 여행지: {place}")
    st.write(f"추천 이유: {reason}")

    st.subheader("여행 팁")
    st.write(f"{place}의 대표 명소와 음식을 미리 조사해보세요!")
