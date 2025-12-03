import streamlit as st
import random

# --- ページ設定 ---
# ページタイトルとレイアウト（ワイドに設定）
st.set_page_config(
    page_title="uprマスタークイズ", 
    page_icon="🚚",
    layout="wide"
)

# --- 1. 問題データセット（100問ストック版） ---
# 実際には100問に満たないですが、100問をストックする前提の構造です。
# 問題を増やしたい場合は、このリストに辞書形式で追加してください。

ALL_QUESTIONS = [
    # --- 基本情報 (10問) ---
    {
        "category": "基本情報",
        "question": "upr株式会社の現在の代表取締役社長は誰？",
        "answer": "酒田 義矢",
        "options": ["酒田 三男", "酒田 義矢", "石村 浩", "大庭 正信"],
        "explanation": "酒田義矢氏が代表取締役社長です。"
    },
    {
        "category": "基本情報",
        "question": "uprの創業の地であり、現在も二本社制の一翼を担う都市は？",
        "answer": "山口県宇部市",
        "options": ["東京都千代田区", "大阪府大阪市", "山口県宇部市", "福岡県福岡市"],
        "explanation": "1979年に山口県宇部市で「ウベパレット株式会社」として設立されました。"
    },
    {
        "category": "基本情報",
        "question": "uprの主力事業であり、売上の約9割を占めるビジネスモデルは？",
        "answer": "パレット・物流機器のレンタル",
        "options": ["アシストスーツの製造販売", "カーシェアリング事業", "パレット・物流機器のレンタル", "AI倉庫システム開発"],
        "explanation": "物流機器、特にパレットのレンタル事業が創業以来の柱です。"
    },
    {
        "category": "基本情報",
        "question": "uprが上場している証券市場は？",
        "answer": "東証スタンダード市場",
        "options": ["東証プライム市場", "東証グロース市場", "東証スタンダード市場", "札幌証券取引所"],
        "explanation": "2019年に東証二部に上場後、現在はスタンダード市場に区分されています。"
    },
    {
        "category": "基本情報",
        "question": "uprの企業理念である「Social Sharing Supporter」とは、何を目指す姿か？",
        "answer": "社会のインフラをシェアするupr",
        "options": ["社会のインフラをシェアするupr", "次世代技術をリードする企業", "世界の物流を支配する企業", "地域社会に貢献する企業"],
        "explanation": "「Social Sharing Supporter」は、「社会のインフラをシェアするupr」を目指すという意味です。"
    },
    {
        "category": "基本情報",
        "question": "uprがメインでレンタル提供している荷役台の名称は？",
        "answer": "パレット",
        "options": ["コンテナ", "パレット", "フォークリフト", "トラック"],
        "explanation": "物流に不可欠なパレットのレンタルが中心です。"
    },
    {
        "category": "基本情報",
        "question": "現在の東京本社の所在地がある区は？",
        "answer": "千代田区",
        "options": ["中央区", "港区", "千代田区", "新宿区"],
        "explanation": "内幸町東急ビル（千代田区）に東京本社があります。"
    },
    {
        "category": "基本情報",
        "question": "uprの創業年の西暦は？",
        "answer": "1979年",
        "options": ["1950年", "1979年", "1988年", "2007年"],
        "explanation": "1979年にウベパレット株式会社として設立されました。"
    },
    {
        "category": "基本情報",
        "question": "uprの事業セグメントのうち、売上の約9割を占めるのは？",
        "answer": "物流事業",
        "options": ["コネクティッド事業", "ICT事業", "物流事業", "カーシェアリング事業"],
        "explanation": "パレットレンタルを中心とした物流事業が中心です。"
    },
    {
        "category": "基本情報",
        "question": "uprが保有するパレットの枚数（概算）は？",
        "answer": "約510万枚",
        "options": ["約100万枚", "約510万枚", "約1,000万枚", "約5,000万枚"],
        "explanation": "2024年8月時点で約510万枚の保有枚数を誇っています。"
    },
    # --- サービス・コネクティッド事業 (10問) ---
    {
        "category": "サービス",
        "question": "物流現場の負担を軽減するuprの装着型機器の総称は？",
        "answer": "アシストスーツ",
        "options": ["パワードスーツ", "アシストスーツ", "サイボーグ", "ロボット"],
        "explanation": "「サポートジャケット」シリーズなどのアシストスーツを展開しています。"
    },
    {
        "category": "サービス",
        "question": "位置・温湿度などを遠隔監視できる物流IoTサービスの名称は？",
        "answer": "なんつい",
        "options": ["みまもりくん", "どこでもサーチ", "なんつい", "パレットファインダー"],
        "explanation": "「なんでも追跡」を略した『なんつい』は、GPS端末を活用した商品です。"
    },
    {
        "category": "サービス",
        "question": "アクティブRFIDタグを搭載し、在庫管理を自動化するパレットの名称は？",
        "answer": "スマートパレット",
        "options": ["デジパレット", "スマートパレット", "AIパレット", "ミラクルパレット"],
        "explanation": "パレットのロケーション管理を効率化するサービスです。"
    },
    {
        "category": "サービス",
        "question": "HACCP法制化に対応し、衛生管理の記録・運用をサポートするIoTパッケージの名称は？",
        "answer": "UPR HACCP",
        "options": ["HACCP Manager", "UPR Clean", "UPR HACCP", "衛生IoT"],
        "explanation": "食品衛生管理をサポートするICT事業のサービスです。"
    },
    {
        "category": "サービス",
        "question": "ビークルソリューション事業に含まれる主なサービスは？",
        "answer": "カーシェアリング事業支援",
        "options": ["ドローン配送", "自動運転システム販売", "カーシェアリング事業支援", "電気自動車のリース"],
        "explanation": "カーシェアリングシステムや鍵管理ソリューションを提供しています。"
    },
    {
        "category": "サービス",
        "question": "パレットレンタルにおける「デポ」とは何を指すか？",
        "answer": "パレットの保管場所",
        "options": ["パレットの製造工場", "パレットの保管場所", "営業拠点", "輸送用のトラック"],
        "explanation": "全国約200カ所にあるパレット保管場所です。"
    },
    {
        "category": "サービス",
        "question": "IoT事業のソリューションで、AIカメラを使って行う監視サービスは？",
        "answer": "車両入退場管理ソリューション",
        "options": ["温湿度センサーによる環境監視", "車両入退場管理ソリューション", "牛の発情検知", "パレットファインダー"],
        "explanation": "ナンバー認証による車両の入退場時間の自動把握に使われます。"
    },
    {
        "category": "サービス",
        "question": "国際間輸送中の荷物の追跡に特化したサービスは？",
        "answer": "ワールドキーパー",
        "options": ["なんつい", "パレットファインダー", "ワールドキーパー", "グローバルロジ"],
        "explanation": "世界のあらゆる場所へ輸送される荷物の位置・状態をリアルタイムで追跡できます。"
    },
    {
        "category": "サービス",
        "question": "スマートフォンでパレットを撮影するだけで枚数をカウントするアプリケーションは？",
        "answer": "パレットファインダー",
        "options": ["パレットマスター", "パレットチェッカー", "パレットファインダー", "数え郎"],
        "explanation": "カメラで色と枚数を瞬時に判別できるアプリです。"
    },
    {
        "category": "サービス",
        "question": "コネクティッド事業のセグメントに含まれないものは？",
        "answer": "アシストスーツ事業",
        "options": ["ICT事業", "ビークルソリューション事業", "アシストスーツ事業", "遠隔監視ソリューション"],
        "explanation": "アシストスーツ事業は物流事業セグメントに含まれます。"
    },
    # --- 財務・IR・歴史・その他 (10問) ---
    {
        "category": "歴史/IR",
        "question": "uprの証券コードは？",
        "answer": "7065",
        "options": ["7065", "9090", "2323", "4649"],
        "explanation": "東京証券取引所（スタンダード市場）での証券コードは「7065」です。"
    },
    {
        "category": "歴史/IR",
        "question": "uprの決算期（事業年度の末日）は何月？",
        "answer": "8月",
        "options": ["3月", "8月", "9月", "12月"],
        "explanation": "uprの決算月は8月です（毎年9月1日〜翌年8月31日）。"
    },
    {
        "category": "歴史/IR",
        "question": "現在の「ユーピーアール株式会社」へ社名が変更された西暦は？",
        "answer": "2007年",
        "options": ["1999年", "2002年", "2007年", "2014年"],
        "explanation": "2007年に「ウベパレットレンタルリーシング株式会社」から変更されました。"
    },
    {
        "category": "歴史/IR",
        "question": "創業家である酒田家の初代社長は？",
        "answer": "酒田 三男",
        "options": ["酒田 義矢", "酒田 三男", "酒田 健治", "酒田 正義"],
        "explanation": "1979年設立時に酒田三男氏が代表取締役社長に就任しました。"
    },
    {
        "category": "歴史/IR",
        "question": "uprが初めて海外法人を設立した国は？",
        "answer": "シンガポール",
        "options": ["タイ", "インドネシア", "シンガポール", "マレーシア"],
        "explanation": "2011年8月にシンガポール法人を設立しました。"
    },
    {
        "category": "歴史/IR",
        "question": "上場を果たした西暦は？",
        "answer": "2019年",
        "options": ["2015年", "2017年", "2019年", "2022年"],
        "explanation": "2019年に東京証券取引所市場第二部に上場しました。"
    },
    {
        "category": "歴史/IR",
        "question": "uprが推進する「パレットプールシステム」の環境への最大の貢献は？",
        "answer": "空車での回収輸送（空荷走行）の削減",
        "options": ["パレット製造時の電力削減", "空車での回収輸送（空荷走行）の削減", "パレットの自動修繕", "全て電気自動車で輸送"],
        "explanation": "複数社での共同利用により、パレット回収のための無駄な輸送を減らせます。"
    },
    {
        "category": "歴史/IR",
        "question": "創業時の社名「ウベパレット」の「ウベ」が指す地名は？",
        "answer": "宇部（山口県）",
        "options": ["宇部（山口県）", "上野（東京都）", "売布（兵庫県）", "宇和島（愛媛県）"],
        "explanation": "創業地である山口県宇部市に由来します。"
    },
    {
        "category": "歴史/IR",
        "question": "uprがタイに現地法人を設立した西暦は？",
        "answer": "2014年",
        "options": ["2011年", "2012年", "2014年", "2016年"],
        "explanation": "2014年にタイ現地法人UPR (Thailand) Co.,Ltdを設立しました。"
    },
    {
        "category": "歴史/IR",
        "question": "連結従業員数は、およそ何名か？（2024年8月時点）",
        "answer": "200名台",
        "options": ["50名未満", "100名台", "200名台", "500名以上"],
        "explanation": "2024年8月時点で228名（連結）です。"
    },
    # --- ストックを埋めるために同じ問題をランダムにコピー（合計100問にするための調整用） ---
    # 実際にはここにユニークな問題を増やしてください
]

# 100問に満たない場合、既存問題をランダムに複製して100問のストックを作る（テスト用）
if len(ALL_QUESTIONS) < 100:
    temp_stock = ALL_QUESTIONS[:]
    while len(temp_stock) < 100:
        temp_stock.extend(random.sample(ALL_QUESTIONS, min(len(ALL_QUESTIONS), 100 - len(temp_stock))))
    ALL_QUESTIONS = temp_stock[:100]

NUM_QUESTIONS_PER_QUIZ = 10 # 毎回出題する問題数

# --- 2. Streamlit セッション管理とロジック ---

def init_game():
    """ゲームの初期化処理（100問から10問をランダム抽出）"""
    st.session_state["score"] = 0
    st.session_state["current_q_index"] = 0
    st.session_state["finished"] = False
    st.session_state["answered"] = False # 回答済みフラグ
    st.session_state["user_choice"] = None
    
    # 100問から10問をランダムに抽出してセット
    st.session_state["questions"] = random.sample(ALL_QUESTIONS, NUM_QUESTIONS_PER_QUIZ)

# セッション状態の初期確認
if "questions" not in st.session_state or len(st.session_state["questions"]) != NUM_QUESTIONS_PER_QUIZ:
    init_game()

# --- 3. UI/デザインの制御 ---

# サイドバーにスコアと進捗を表示
with st.sidebar:
    st.image("https://www.upr-net.co.jp/common/img/logo.png", width=150)
    st.header("🚚 uprマスタークイズ")
    
    if not st.session_state["finished"]:
        # 進捗バーの表示
        current = st.session_state["current_q_index"]
        total = NUM_QUESTIONS_PER_QUIZ
        progress_ratio = current / total if total > 0 else 0
        
        st.subheader(f"進捗: {current + 1} / {total} 問")
        st.progress(progress_ratio)
        
        st.metric("現在のスコア", f"{st.session_state['score']} 点")
        
    if st.button("最初からやり直す", key="restart_btn"):
        init_game()
        st.rerun()

# --- 4. 画面表示とフロー制御 ---

# --- クイズ終了時の画面 ---
if st.session_state["finished"]:
    st.balloons()
    score = st.session_state["score"]
    total = NUM_QUESTIONS_PER_QUIZ
    
    st.markdown("<h1 style='color:#387ef5;'>結果発表！</h1>", unsafe_allow_html=True)
    st.markdown(f"## 🏆 スコア: **{total}問中 {score}問 正解**")
    
    if score == total:
        st.success("🎉 全問正解！あなたは真のuprマスターです！")
    elif score >= total * 0.7:
        st.info("👍 素晴らしい！uprの知識は完璧に近いです。")
    else:
        st.warning("🧐 あと少し！Webサイトで復習し、再チャレンジしましょう。")
    
    st.markdown("---")
    if st.button("新しい10問に挑戦する！"):
        init_game()
        st.rerun()

# --- クイズ進行中の画面 ---
else:
    idx = st.session_state["current_q_index"]
    q_data = st.session_state["questions"][idx]
    
    # 問題ヘッダー
    st.markdown(f"<span style='background-color:#E0F7FA; padding:5px 10px; border-radius:5px; font-weight:bold; color:#00BCD4;'>{q_data['category']}</span>", unsafe_allow_html=True)
    st.markdown(f"## 第 {idx + 1} 問: {q_data['question']}")
    st.markdown("---")

    # 選択肢のコンテナ
    choices_container = st.container()
    
    # 選択肢をボタンとして表示（デザイン性向上とマーク非表示の代替）
    with choices_container:
        cols = st.columns(len(q_data["options"]))
        for i, option in enumerate(q_data["options"]):
            with cols[i]:
                # 回答済みの場合、選択したボタンの色を変える
                is_selected = (st.session_state["answered"] and st.session_state["user_choice"] == option)
                
                # 回答ボタンのスタイル
                btn_style = (
                    "background-color: #387ef5; color: white;" 
                    if is_selected 
                    else "background-color: #f0f2f6; color: black;"
                )
                
                # 回答確定前のみ、ボタンを押せるようにする
                if not st.session_state["answered"]:
                    if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True):
                        # 回答確定処理
                        st.session_state["user_choice"] = option
                        st.session_state["answered"] = True
                        st.rerun()
                else:
                    # 回答後はボタンを無効化して表示
                    st.button(option, key=f"opt_{idx}_{i}", use_container_width=True, disabled=True)
    
    st.markdown("---")
    
    # --- 回答後の処理（正誤判定と解説） ---
    if st.session_state["answered"]:
        user_choice = st.session_state["user_choice"]
        
        # 判定とスコア加算
        if user_choice == q_data["answer"]:
            st.success(f"✅ 正解！ あなたの回答: **{user_choice}**")
            # スコアは正解時のみ加算（複数回押しても加算されないようinit_gameの外で制御）
            if f"q_{idx}_scored" not in st.session_state:
                st.session_state["score"] += 1
                st.session_state[f"q_{idx}_scored"] = True # この問題は採点済みとしてマーク
        else:
            st.error(f"❌ 不正解... あなたの回答: **{user_choice}**")
        
        # 解説表示
        st.markdown(f"#### 正解は **{q_data['answer']}** でした。")
        st.markdown(f"**💡 解説:** {q_data['explanation']}")
        
        st.markdown("---")
        
        # 次へボタン
        if idx + 1 >= NUM_QUESTIONS_PER_QUIZ:
            if st.button("🎉 結果を見る", use_container_width=True):
                st.session_state["finished"] = True
                st.rerun()
        else:
            if st.button("▶️ 次の問題へ進む", use_container_width=True):
                st.session_state["current_q_index"] += 1
                st.session_state["answered"] = False # 回答フラグをリセット
                st.session_state["user_choice"] = None # 選択肢をリセット
                st.rerun()