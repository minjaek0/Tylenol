def analyze_beverage_solubility_factors():
    """
    7가지 식용 음료(용매) 선택에 따라 용해도 영향 요인의 예시를 보여주고,
    새로운 실험 데이터를 추가할 수 있는 프로그램입니다.
    """
    
    # 1. 7가지 음료 용매 데이터베이스 구축
    solvent_database = {
        "물 (H2O)": {
            "주요_성분": "H2O",
            "용해도_특성": "극성 물질의 기준 용해도 제공",
            "영향_요인": "물의 **온도** (용해도에 가장 큰 영향)"
        },
        "우유 (Milk)": {
            "주요_성분": "칼슘, 지방, 카제인(단백질)",
            "용해도_특성": "이온 흡착, pH 완충, 에멀젼화 가능",
            "영향_요인": "칼슘 이온의 **킬레이트/침전 형성**, 지방 성분의 **지용성 용질 흡수**"
        },
        "오렌지 주스": {
            "주요_성분": "구연산(Citric Acid), 당류, 비타민 C",
            "용해도_특성": "강한 산성 환경 (낮은 pH), 높은 점도",
            "영향_요인": "**낮은 pH**로 인한 염기성 용질의 **이온화 촉진**, **당 농도**로 인한 용매 경쟁"
        },
        "사과 주스": {
            "주요_성분": "사과산(Malic Acid), 과당(Fructose)",
            "용해도_특성": "중간 산성도 (pH), 높은 당 농도",
            "영향_요인": "높은 과당 농도로 인한 **용매 유효량 감소**, **pH 변화**"
        },
        "녹차": {
            "주요_성분": "카테킨 (Polyphenols), 카페인",
            "용해도_특성": "약한 산성도, 착물 형성 가능",
            "영향_요인": "카테킨 성분의 특정 용질과의 **수소 결합/결합체 형성**"
        },
        "커피 (Black)": {
            "주요_성분": "클로로겐산(Tannins), 유기산",
            "용해도_특성": "산성 용매, 다양한 페놀성 화합물 포함",
            "영향_요인": "탄닌의 **금속 이온/염기성 약물과의 착물 형성**, **pH**"
        },
        "에너지 드링크": {
            "주요_성분": "타우린, 카페인, 인공 감미료/당류, 비타민 B군, 산성 첨가물",
            "용해도_특성": "매우 낮은 pH (강한 산성), 고농축 용질 포함",
            "영향_요인": "**매우 낮은 pH** 및 **고농도 첨가물**로 인한 **이온 강도 변화**"
        }
    }

    # 2. 사용자에게 용매 선택 옵션 제공
    print("--- 🔬 7가지 음료 용해도 영향 요인 분석 ---")
    print("분석할 음료(용매)를 선택하거나(번호), 새로운 데이터를 입력하세요(0).")
    
    solvent_list = list(solvent_database.keys())
    for i, solvent in enumerate(solvent_list):
        print(f"{i + 1}. {solvent}")
    print("0. 새로운 용매 및 실험 데이터 추가")
    print("q. 프로그램 종료")
    
    choice = input("선택 번호(1~7, 0 또는 q): ")
    
    # 3. 사용자 선택에 따른 처리
    if choice.lower() == 'q':
        print("프로그램을 종료합니다.")
        return

    try:
        choice_num = int(choice)
        
        if 1 <= choice_num <= len(solvent_list):
            selected_solvent = solvent_list[choice_num - 1]
            data = solvent_database[selected_solvent]
            
            print(f"\n--- 🔎 선택된 용매: **{selected_solvent}** 분석 결과 ---")
            print(f"  * **주요 구성 성분:** {data['주요_성분']}")
            print(f"  * **용해도 일반 특성:** {data['용해도_특성']}")
            print(f"  * **실험 영향 요인 (예시):** {data['영향_요인']}")
            
        elif choice_num == 0:
            # 새로운 데이터 추가 로직
            print("\n--- 🆕 새로운 용매 데이터 입력 ---")
            new_solvent = input("새로운 용매 이름을 입력하세요: ")
            factor = input(f"'{new_solvent}'의 핵심 영향 성분은 무엇인가요?: ")
            mechanism = input("관찰된 용해도 영향 메커니즘을 설명하세요: ")

            # 사용자 데이터베이스에 추가
            solvent_database[new_solvent] = {
                "주요_성분": "사용자 입력",
                "용해도_특성": "사용자 탐구 결과",
                "영향_요인": f"요인: {factor}, 메커니즘: {mechanism}"
            }
            print(f"\n✅ '{new_solvent}' 데이터가 데이터베이스에 추가되었습니다.")
            
        else:
            print("🚨 잘못된 번호를 선택했습니다. 프로그램을 다시 실행해주세요.")
            
    except ValueError:
        print("🚨 잘못된 형식의 입력입니다. 프로그램을 다시 실행해주세요.")

# 프로그램 실행을 원하시면 아래 주석을 해제하세요.
# analyze_beverage_solubility_factors()
