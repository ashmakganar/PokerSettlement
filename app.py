# Poker Settlement App – Improved Streamlit Version

```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Poker Settlement", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }

    .stTextInput input {
        border-radius: 12px;
        padding: 10px;
    }

    .stNumberInput input {
        border-radius: 12px;
    }

    .player-card {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 16px;
        margin-bottom: 12px;
        border: 1px solid #333;
    }

    .result-box {
        background-color: #1a2e1a;
        padding: 15px;
        border-radius: 15px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🃏 Poker Settlement App")
st.write("Easy Hinglish poker हिसाब system")

# -----------------------------
# Number of Players
# -----------------------------

num_players = st.number_input(
    "Kitne players hai?",
    min_value=2,
    max_value=20,
    step=1,
)

players = []
boot_amounts = {}
final_amounts = {}

st.divider()

# -----------------------------
# Player Details
# -----------------------------

st.subheader("👥 Players Details")

for i in range(num_players):
    st.markdown(f"### Player {i+1}")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            f"Player {i+1} ka naam",
            key=f"name_{i}",
            placeholder="Naam likho...",
        )

    with col2:
        boot = st.number_input(
            f"{name if name else 'Player'} ne bank se kitna boot liya?",
            min_value=0,
            step=10,
            key=f"boot_{i}",
        )

    if name:
        players.append(name)
        boot_amounts[name] = boot

st.divider()

# -----------------------------
# Final Amounts
# -----------------------------

st.subheader("💰 Match Khatam Hone Ke Baad")

st.write("Har player ke paas abhi total kitna amount hai?")

for player in players:
    final_amounts[player] = st.number_input(
        f"{player} ke paas abhi kitna amount hai?",
        min_value=0,
        step=10,
        key=f"final_{player}",
    )

st.divider()

# -----------------------------
# Udhar Section
# -----------------------------

st.subheader("🤝 Udhar Entries")

num_loans = st.number_input(
    "Kitne udhar transactions hue?",
    min_value=0,
    max_value=50,
    step=1,
)

loans = []

for i in range(num_loans):
    st.markdown(f"### Udhar {i+1}")

    col1, col2, col3 = st.columns(3)

    with col1:
        giver = st.selectbox(
            "Kisne paise diye?",
            players,
            key=f"giver_{i}",
        )

    with col2:
        receiver = st.selectbox(
            "Kisne udhar liya?",
            players,
            key=f"receiver_{i}",
        )

    with col3:
        amount = st.number_input(
            "Kitna amount?",
            min_value=0,
            step=10,
            key=f"amount_{i}",
        )

    loans.append((giver, receiver, amount))

st.divider()

# -----------------------------
# Calculation
# -----------------------------

if st.button("📊 Final Hisaab Nikalo"):

    settlement = {}

    for player in players:
        settlement[player] = final_amounts[player] - boot_amounts[player]

    # Udhar Adjustments
    for giver, receiver, amount in loans:
        settlement[giver] += amount
        settlement[receiver] -= amount

    st.subheader("📈 Profit / Loss")

    for player, value in settlement.items():

        if value > 0:
            st.success(f"✅ {player} ko PROFIT hua hai ₹{value}")

        elif value < 0:
            st.error(f"❌ {player} LOSS me hai ₹{abs(value)}")

        else:
            st.info(f"➖ {player} ka no profit no loss")

    st.divider()

    # -----------------------------
    # Settlement Logic
    # -----------------------------

    creditors = []
    debtors = []

    for player, amount in settlement.items():
        if amount > 0:
            creditors.append([player, amount])
        elif amount < 0:
            debtors.append([player, -amount])

    transactions = []

    i = 0
    j = 0

    while i < len(debtors) and j < len(creditors):

        debtor_name, debtor_amt = debtors[i]
        creditor_name, creditor_amt = creditors[j]

        pay_amt = min(debtor_amt, creditor_amt)

        transactions.append(
            f"💸 {debtor_name} ko {creditor_name} ko ₹{pay_amt} dene hai"
        )

        debtors[i][1] -= pay_amt
        creditors[j][1] -= pay_amt

        if debtors[i][1] == 0:
            i += 1

        if creditors[j][1] == 0:
            j += 1

    st.subheader("🧾 Final Settlement")

    if transactions:
        for t in transactions:
            st.markdown(f"### {t}")
    else:
        st.success("Sabka hisaab barabar hai 😄")

    st.divider()

    # -----------------------------
    # Summary Table
    # -----------------------------

    summary_data = []

    for player in players:
        summary_data.append(
            {
                "Player": player,
                "Boot Liya": boot_amounts[player],
                "Final Amount": final_amounts[player],
                "Net Profit/Loss": settlement[player],
            }
        )

    df = pd.DataFrame(summary_data)

    st.subheader("📋 Full Summary")
    st.dataframe(df, use_container_width=True)
```

# Important Commands

## Run Locally

```bash
python3 -m streamlit run app.py
```

## Update GitHub

```bash
git add .
git commit -m "updated poker app"
git push
```

Streamlit automatically update ho jayega.
