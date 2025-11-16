import streamlit as st

# 타이레놀 용해도 및 흡수 영향 데이터 (에너지 드링크 포함)
tylenol_solvents = {
    "물": {
        "용해도": "좋음 (비이온화 상태에서 충분히 녹음)",
        "흡수": "보통",
        "권장": "안전: 일반 복용 가능"
    },
    "우유": {
        "용해도": "조금 낮음 (칼슘과 단백질 영향)",
        "흡수": "흡수 증가 가능 (지용성 흡수 약간 도움)",
        "권장": "안전: 일반 복용 가능"
    },
    "과일주스": {
        "용해도": "조금 낮음 (당류와 산 영향)",
        "흡수": "흡수 감소 가능",
        "권장": "주의: 흡수 약간 감소 가능"
    },
    "오렌지 주스": {
        "용해도": "약간 낮음 (산성 영향)",
        "흡수": "흡수 감소 가능",
        "권장": "주의"
    },
    "사과 주스": {
        "용해도": "약간 낮음 (당류와 산 영향)",
        "흡수": "흡수 감소 가능",
        "권장": "주의"
    },
    "녹차": {
        "용해도": "보통 (카테킨 영향)",
        "흡수": "보통",
        "권장": "보통"
    },
    "커피": {
        "용해도": "보통 (카페인 영향)",
        "흡수": "보통",
        "권장": "보통"
    },
    "에너지 드링크": {
        "용해도": "보통 (카페인, 당류 영향)",
        "흡수": "흡수 감소 가능",
        "권장": "주의: 카페인 주의"
    },
    "기타": {
        "용해도": "정보 없음",
        "흡수": "정보 없음",
        "권장": "확인 필요"
    }
}

# UI
st.title("타이레놀 복용 시 용매별 용해도와 흡수 확인")
st.write("타이레놀(아세트아미노펜)을 복용한다고 가정하고, 용매별 용해도, 흡수 영향, 권장 여부를 확인할 수 있습니다.")

# 사용자 입력
solvent = st.text_input("용매 이름 입력 (예: 물, 우유, 과일주스, 오렌지 주스, 에너지 드링크 등)")

if solvent:
    solvent_lower = solvent.lower()
    found = False
    for key in tylenol_solvents:
        if key.lower() == solvent_lower:
            info = tylenol_solvents[key]
            st.write(f"**{key}**에서 타이레놀 용해도: {info['용해도']}")
            st.write(f"**흡수 영향:** {info['흡수']}")
            st.write(f"**권장 여부:** {info['권장']}")
            found = True
            break
    if not found:
        st.write(f"{solvent}에 대한 정보가 없습니다. 주의해서 사용하세요.")

# 사용자 정의 용매 추가 가능
st.subheader("새 용매 정보 추가")
new_solvent = st.text_input("새 용매 이름", key="new_solvent")
new_solvent_dissolve = st.text_input("용해도 설명", key="new_dissolve")
new_solvent_absorption = st.text_input("흡수 영향", key="new_absorption")
new_solvent_recommend = st.text_input("권장 여부", key="new_recommend")

if st.button("추가"):
    if new_solvent and new_solvent_dissolve and new_solvent_absorption and new_solvent_recommend:
        tylenol_solvents[new_solvent] = {
            "용해도": new_solvent_dissolve,
            "흡수": new_solvent_absorption,
            "권장": new_solvent_recommend
        }
        st.success(f"{new_solvent} 정보가 추가되었습니다!")
    else:
        st.error("모든 정보를 입력해주세요.")
