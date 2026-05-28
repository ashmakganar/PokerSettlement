import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Poker Settlement",
    page_icon="🃏",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0a1628 0%, #0d1f0f 50%, #0a1628 100%);
}

.block-container {
    padding-top: 2rem;
    max-width: 860px;
}

h1, h2, h3 {
    font-family: 'Rajdhani', sans-serif !important;
}

.main-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #d4af37;
    text-align: center;
    letter-spacing: 3px;
    text-shadow: 0 0 30px rgba(212,175,55,0.4);
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #6b8f71;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.suits {
    text-align: center;
    font-size: 1.6rem;
    margin-bottom: 0.5rem;
    letter-spacing: 12px;
}

.section-header {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #d4af37;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-left: 3px solid #d4af37;
    padding-left: 12px;
    margin: 1.5rem 0 1rem 0;
}

.card-panel {
    background: rgba(13, 40, 24, 0.7);
    border: 1px solid rgba(212,175,55,0.2);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}

.player-tag {
    display: inline-block;
    background: rgba(212,175,55,0.1);
    border: 1px solid rgba(212,175,55,0.3);
    color: #d4af37;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.result-card {
    border-radius: 14px;
    padding: 14px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.profit-card {
    background: linear-gradient(90deg, rgba(34,85,34,0.4) 0%, rgba(20,60,20,0.2) 100%);
    border: 1px solid rgba(82,183,100,0.5);
    color: #74c69d;
}

.loss-card {
    background: linear-gradient(90deg, rgba(120,20,20,0.4) 0%, rgba(80,10,10,0.2) 100%);
    border: 1px solid rgba(220,80,80,0.5);
    color: #ff8080;
}

.even-card {
    background: rgba(30,40,50,0.4);
    border: 1px solid rgba(100,120,140,0.4);
    color: #a0b0c0;
}

.txn-card {
    background: rgba(10,25,40,0.6);
    border: 1px solid rgba(212,175,55,0.25);
    border-radius: 14px;
    padding: 14px 20px;
    margin-bottom: 10px;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #e8d5a0;
    display: flex;
    align-items: center;
    gap: 10px;
}

.amount-badge {
    background: rgba(212,175,55,0.15);
    border: 1px solid rgba(212,175,55,0.4);
    color: #d4af37;
    padding: 2px 10px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 700;
}

.stat-box {
    background: rgba(13,40,24,0.8);
    border: 1px solid rgba(212,175,55,0.2);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}

.stat-label {
    font-size: 0.72rem;
    color: #6b8f71;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 4px;
}

.stat-value {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #d4af37;
}

.divider-gold {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.4), transparent);
    margin: 1.5rem 0;
}

.stButton > button {
    background: linear-gradient(135deg, #1a4a1a 0%, #2d6a2d 100%) !important;
    color: #d4af37 !important;
    border: 1px solid rgba(212,175,55,0.5) !important;
    border-radius: 10px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    height: 48px !important;
    transition: all 0.2s !important;
    text-transform: uppercase !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2d6a2d 0%, #3a8a3a 100%) !important;
    border-color: rgba(212,175,55,0.8) !important;
    box-shadow: 0 0 20px rgba(212,175,55,0.2) !important;
}

.stNumberInput input, .stTextInput input, .stSelectbox select {
    background: rgba(10,25,15,0.8) !important;
    border: 1px solid rgba(212,175,55,0.2) !important;
    border-radius: 8px !important;
    color: #e8d5a0 !important;
}

.stNumberInput input:focus, .stTextInput input:focus {
    border-color: rgba(212,175,55,0.6) !important;
    box-shadow: 0 0 0 2px rgba(212,175,55,0.1) !important;
}

label {
    color: #95a88f !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.5px !important;
}

.stDataFrame {
    border: 1px solid rgba(212,175,55,0.2) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

.warning-box {
    background: rgba(120,80,10,0.3);
    border: 1px solid rgba(212,175,55,0.4);
    border-radius: 10px;
    padding: 10px 16px;
    color: #d4af37;
    font-size: 0.88rem;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)

# ── Title ──────────────────────────────────────────────
st.markdown('<div class="suits">♠ ♥ ♦ ♣</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">POKER SETTLEMENT</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Track · Borrow · Settle</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

# ── Step 1: Players ─────────────────────────────────────
st.markdown('<div class="section-header">① Players & Buy-in</div>', unsafe_allow_html=True)

suits = ["♠", "♥", "♦", "♣"]

num_players = st.number_input(
    "Number of Players",
    min_value=2, max_value=20, step=1, value=2
)

players = []
boot_data = {}

for i in range(int(num_players)):
    col1, col2, col3 = st.columns([0.3, 1.5, 1.2])
    with col1:
        st.markdown(
            f'<div style="font-size:1.6rem;text-align:center;padding-top:28px;color:#d4af37">'
            f'{suits[i % 4]}</div>',
            unsafe_allow_html=True
        )
    with col2:
        name = st.text_input(
            f"Player {i+1} Name",
            key=f"name_{i}",
            placeholder=f"Enter name for Player {i+1}"
        )
    with col3:
        boot = st.number_input(
            f"Buy-in Amount (₹)",
            min_value=0, step=10, key=f"boot_{i}"
        )
    if name.strip():
        players.append(name.strip())
        boot_data[name.strip()] = boot

st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

# ── Step 2: Borrowings ─────────────────────────────────
st.markdown('<div class="section-header">② Borrowings During Game</div>', unsafe_allow_html=True)

if not players:
    st.markdown(
        '<div class="warning-box">⚠️ Add player names above to record borrowings.</div>',
        unsafe_allow_html=True
    )

loan_count = st.number_input(
    "Number of Borrowing Transactions",
    min_value=0, max_value=50, step=1, value=0
)

loan_entries = []

for i in range(int(loan_count)):
    st.markdown(
        f'<div style="font-size:0.78rem;color:#6b8f71;letter-spacing:1px;margin:8px 0 4px;">TRANSACTION #{i+1}</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1.2, 1.2, 1])
    with col1:
        giver = st.selectbox(
            "Who Gave?",
            options=players if players else ["—"],
            key=f"giver_{i}"
        )
    with col2:
        receiver = st.selectbox(
            "Who Took?",
            options=players if players else ["—"],
            key=f"receiver_{i}"
        )
    with col3:
        amount = st.number_input(
            "Amount (₹)",
            min_value=0, step=10, key=f"loan_{i}"
        )
    if players and giver != receiver:
        loan_entries.append((giver, receiver, amount))
    elif players and giver == receiver:
        st.markdown(
            '<div class="warning-box">⚠️ Giver and receiver cannot be the same player.</div>',
            unsafe_allow_html=True
        )

st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

# ── Step 3: Final Chip Counts ───────────────────────────
st.markdown('<div class="section-header">③ Final Chip Count</div>', unsafe_allow_html=True)

if not players:
    st.markdown(
        '<div class="warning-box">⚠️ Add player names in Step 1 first.</div>',
        unsafe_allow_html=True
    )

final_amounts = {}

for i, player in enumerate(players):
    col1, col2, col3 = st.columns([0.3, 1.5, 1.2])
    with col1:
        st.markdown(
            f'<div style="font-size:1.6rem;text-align:center;padding-top:28px;color:#d4af37">'
            f'{suits[i % 4]}</div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f'<div style="padding-top:30px;color:#e8d5a0;font-weight:600;font-size:1rem;">'
            f'{player}'
            f'<span style="color:#6b8f71;font-size:0.82rem;font-weight:400;margin-left:10px;">'
            f'Bought in: ₹{boot_data[player]:,}</span></div>',
            unsafe_allow_html=True
        )
    with col3:
        amt = st.number_input(
            f"Final Chips (₹)",
            min_value=0, step=10, key=f"final_{player}"
        )
    final_amounts[player] = amt

st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

# ── Calculate ───────────────────────────────────────────
if st.button("🃏  CALCULATE SETTLEMENT", use_container_width=True):

    if len(players) < 2:
        st.error("Add at least 2 players with names to calculate.")
    else:
        # Compute net balances
        balances = {}
        for p in players:
            balances[p] = final_amounts[p] - boot_data[p]

        for giver, receiver, amount in loan_entries:
            balances[giver] += amount
            balances[receiver] -= amount

        total_pool = sum(final_amounts[p] for p in players)
        total_buy_in = sum(boot_data[p] for p in players)
        winners = sum(1 for p in players if balances[p] > 0)

        # Stats row
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="stat-box"><div class="stat-label">Players</div><div class="stat-value">{len(players)}</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="stat-box"><div class="stat-label">Total Buy-in</div><div class="stat-value">₹{total_buy_in:,}</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="stat-box"><div class="stat-label">Final Pool</div><div class="stat-value">₹{total_pool:,}</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="stat-box"><div class="stat-label">Winners</div><div class="stat-value">{winners}</div></div>', unsafe_allow_html=True)

        st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

        # Profit / Loss
        st.markdown('<div class="section-header">📊 Profit / Loss</div>', unsafe_allow_html=True)

        for i, player in enumerate(players):
            bal = balances[player]
            suit = suits[i % 4]
            if bal > 0:
                st.markdown(
                    f'<div class="result-card profit-card">'
                    f'<span style="font-size:1.3rem">{suit}</span>'
                    f'<span style="flex:1">{player}</span>'
                    f'<span>Profit&nbsp;</span>'
                    f'<span style="color:#52e87a;font-size:1.2rem">▲ ₹{bal:,}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            elif bal < 0:
                st.markdown(
                    f'<div class="result-card loss-card">'
                    f'<span style="font-size:1.3rem">{suit}</span>'
                    f'<span style="flex:1">{player}</span>'
                    f'<span>Loss&nbsp;</span>'
                    f'<span style="color:#ff6666;font-size:1.2rem">▼ ₹{abs(bal):,}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="result-card even-card">'
                    f'<span style="font-size:1.3rem">{suit}</span>'
                    f'<span style="flex:1">{player}</span>'
                    f'<span style="color:#a0b0c0">— Broke Even at ₹0</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

        # Settlement Transactions
        st.markdown('<div class="section-header">💸 Settlement Transactions</div>', unsafe_allow_html=True)

        creditors = [[p, balances[p]] for p in players if balances[p] > 0]
        debtors = [[p, abs(balances[p])] for p in players if balances[p] < 0]

        i, j = 0, 0
        transactions = []

        while i < len(debtors) and j < len(creditors):
            debtor, d_amt = debtors[i]
            creditor, c_amt = creditors[j]
            pay = min(d_amt, c_amt)
            transactions.append((debtor, creditor, pay))
            debtors[i][1] -= pay
            creditors[j][1] -= pay
            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        if not transactions:
            st.success("✅ All balances are perfectly settled — no transfers needed!")
        else:
            for idx, (frm, to, amt) in enumerate(transactions):
                st.markdown(
                    f'<div class="txn-card">'
                    f'<span style="color:#ff8080;font-weight:700">{frm}</span>'
                    f'<span style="color:#6b8f71;margin:0 6px">pays</span>'
                    f'<span class="amount-badge">₹{amt:,}</span>'
                    f'<span style="color:#6b8f71;margin:0 6px">to</span>'
                    f'<span style="color:#74c69d;font-weight:700">{to}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        st.markdown('<hr class="divider-gold">', unsafe_allow_html=True)

        # Summary Table
        st.markdown('<div class="section-header">📋 Game Summary</div>', unsafe_allow_html=True)

        rows = []
        for p in players:
            bal = balances[p]
            rows.append({
                "Player": p,
                "Buy-in (₹)": boot_data[p],
                "Final Chips (₹)": final_amounts[p],
                "Net P/L (₹)": bal,
                "Result": "✅ Profit" if bal > 0 else "❌ Loss" if bal < 0 else "— Even"
            })

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Net P/L (₹)": st.column_config.NumberColumn(
                    "Net P/L (₹)",
                    format="₹%d"
                ),
                "Buy-in (₹)": st.column_config.NumberColumn(format="₹%d"),
                "Final Chips (₹)": st.column_config.NumberColumn(format="₹%d"),
            }
        )

        st.markdown(
            '<div style="text-align:center;color:#3a5a3a;font-size:0.8rem;'
            'letter-spacing:2px;margin-top:1.5rem">♠ ♥ PLAY RESPONSIBLY ♦ ♣</div>',
            unsafe_allow_html=True
        )