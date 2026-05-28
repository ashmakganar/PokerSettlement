import streamlit as st
import pandas as pd
import time

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Poker Settlement Pro",
    page_icon="🃏",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    color: white;
}

/* Main App Padding */
.block-container {
    padding-top: 1rem;
    padding-bottom: 3rem;
    max-width: 700px;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 22px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    margin-bottom: 18px;
}

/* Headings */
.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 25px;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 14px !important;
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 18px;
    height: 55px;
    border: none;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    color: white;
    font-size: 18px;
    font-weight: 700;
    transition: 0.3s;
    box-shadow: 0 6px 20px rgba(124,58,237,0.4);
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* Result Cards */
.result-card {
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 12px;
    font-size: 18px;
    font-weight: 600;
    animation: fadeIn 0.5s ease-in-out;
}

.profit {
    background: rgba(16,185,129,0.12);
    border: 1px solid #10b981;
}

.loss {
    background: rgba(239,68,68,0.12);
    border: 1px solid #ef4444;
}

.settlement {
    background: rgba(59,130,246,0.12);
    border: 1px solid #3b82f6;
}

/* Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

hr {
    border-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="main-title">🃏 Poker Settlement Pro</div>
    <div class="sub-title">
        Smart poker balance tracker with borrowings & settlements 💸
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# PLAYER SECTION
# ---------------------------------------------------

with st.container():

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("👥 Players Setup")

    num_players = st.number_input(
        "🎯 Number of Players",
        min_value=2,
        max_value=20,
        step=1
    )

    players = []
    boot_data = {}

    for i in range(num_players):

        st.markdown(f"### 🧑 Player {i+1}")

        col1, col2 = st.columns([2,1])

        with col1:
            player_name = st.text_input(
                "Name",
                key=f"name_{i}",
                placeholder="Enter player name"
            )

        with col2:
            boot_amount = st.number_input(
                "Boot ₹",
                min_value=0,
                step=10,
                key=f"boot_{i}"
            )

        if player_name:
            players.append(player_name)
            boot_data[player_name] = boot_amount

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# BORROWINGS SECTION (ABOVE)
# ---------------------------------------------------

if players:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("🤝 Borrowing Transactions")

    loan_count = st.number_input(
        "📌 Number of Borrowings",
        min_value=0,
        max_value=50,
        step=1
    )

    loan_entries = []

    for i in range(loan_count):

        st.markdown(f"#### 💳 Borrowing #{i+1}")

        col1, col2, col3 = st.columns([1.2,1.2,1])

        with col1:
            giver = st.selectbox(
                "Giver",
                players,
                key=f"giver_{i}"
            )

        with col2:
            receiver = st.selectbox(
                "Receiver",
                players,
                key=f"receiver_{i}"
            )

        with col3:
            amount = st.number_input(
                "₹ Amount",
                min_value=0,
                step=10,
                key=f"loan_{i}"
            )

        loan_entries.append((giver, receiver, amount))

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# FINAL AMOUNTS
# ---------------------------------------------------

if players:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("💰 Final Chip / Cash Amount")

    final_amounts = {}

    for player in players:

        final_amounts[player] = st.number_input(
            f"🎲 {player}",
            min_value=0,
            step=10,
            key=f"final_{player}"
        )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# CALCULATE BUTTON
# ---------------------------------------------------

if players:

    if st.button("🚀 Calculate Settlement"):

        with st.spinner("Calculating balances..."):

            time.sleep(1)

            balances = {}

            # Base Profit/Loss
            for player in players:
                balances[player] = (
                    final_amounts[player]
                    - boot_data[player]
                )

            # Borrowing Adjustments
            for giver, receiver, amount in loan_entries:
                balances[giver] += amount
                balances[receiver] -= amount

        # ---------------------------------------------------
        # PROFIT LOSS
        # ---------------------------------------------------

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📈 Profit / Loss")

        for player, amount in balances.items():

            if amount > 0:

                st.markdown(
                    f"""
                    <div class="result-card profit">
                    🟢 {player} is in PROFIT of ₹{amount}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif amount < 0:

                st.markdown(
                    f"""
                    <div class="result-card loss">
                    🔴 {player} is in LOSS of ₹{abs(amount)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="result-card settlement">
                    ⚖️ {player} is perfectly settled
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------
        # FINAL SETTLEMENTS BELOW
        # ---------------------------------------------------

        creditors = []
        debtors = []

        for player, amount in balances.items():

            if amount > 0:
                creditors.append([player, amount])

            elif amount < 0:
                debtors.append([player, abs(amount)])

        i = 0
        j = 0

        transactions = []

        while i < len(debtors) and j < len(creditors):

            debtor_name, debtor_amount = debtors[i]
            creditor_name, creditor_amount = creditors[j]

            settlement_amount = min(
                debtor_amount,
                creditor_amount
            )

            transactions.append(
                f"💸 {debtor_name} pays ₹{settlement_amount} to {creditor_name}"
            )

            debtors[i][1] -= settlement_amount
            creditors[j][1] -= settlement_amount

            if debtors[i][1] == 0:
                i += 1

            if creditors[j][1] == 0:
                j += 1

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🧾 Final Settlements")

        if transactions:

            for transaction in transactions:

                st.markdown(
                    f"""
                    <div class="result-card settlement">
                    {transaction}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success("✅ Everybody is settled perfectly!")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------
        # SUMMARY TABLE
        # ---------------------------------------------------

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📊 Game Summary")

        summary_data = []

        for player in players:

            summary_data.append({
                "Player": player,
                "Boot": boot_data[player],
                "Final": final_amounts[player],
                "Net": balances[player]
            })

        df = pd.DataFrame(summary_data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <br>
    <center style='color:gray; font-size:14px;'>
    Made with ❤️ for Poker Nights ♠️
    </center>
    """,
    unsafe_allow_html=True
)