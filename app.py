import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Poker Settlement",
    page_icon="🃏",
    layout="centered"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #080e0a;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2d6a4f; border-radius: 4px; }

/* ── Layout ── */
.block-container {
    padding: 1.2rem 1rem 3rem 1rem !important;
    max-width: 540px !important;
}

/* ── Title area ── */
.hero-wrap {
    text-align: center;
    padding: 1.2rem 0 1rem;
}
.hero-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(212,175,55,0.08);
    border: 1px solid rgba(212,175,55,0.25);
    border-radius: 30px;
    padding: 5px 14px;
    font-size: 0.72rem;
    color: #d4af37;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.hero-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #f0e0a0;
    letter-spacing: 3px;
    line-height: 1.1;
    margin: 0;
}
.hero-sub {
    color: #3a6b4a;
    font-size: 0.78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 6px;
}

/* ── Section header ── */
.sec-head {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.6rem 0 0.9rem;
}
.sec-num {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.35);
    color: #d4af37;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.sec-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #c8a850;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.sec-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(212,175,55,0.25), transparent);
}

/* ── Player card ── */
.player-card {
    background: linear-gradient(135deg, rgba(18,40,22,0.9) 0%, rgba(12,28,16,0.9) 100%);
    border: 1px solid rgba(45,106,79,0.5);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.player-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.4), transparent);
}
.player-label {
    font-size: 0.7rem;
    color: #3a6b4a;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-weight: 600;
}

/* ── Loan card ── */
.loan-card {
    background: linear-gradient(135deg, rgba(20,25,35,0.9) 0%, rgba(12,18,28,0.9) 100%);
    border: 1px solid rgba(80,100,140,0.4);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    position: relative;
    overflow: hidden;
}
.loan-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(100,140,220,0.3), transparent);
}
.loan-label {
    font-size: 0.7rem;
    color: #4a6080;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-weight: 600;
}
.arrow-badge {
    display: inline-block;
    background: rgba(100,140,220,0.1);
    border: 1px solid rgba(100,140,220,0.25);
    color: #7090d0;
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.8rem;
    letter-spacing: 1px;
    margin: 6px 0;
}

/* ── Final chip card ── */
.chip-card {
    background: linear-gradient(135deg, rgba(25,20,10,0.9) 0%, rgba(18,14,6,0.9) 100%);
    border: 1px solid rgba(140,100,30,0.4);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    position: relative;
    overflow: hidden;
}
.chip-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.5), transparent);
}
.chip-name {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #e8d070;
    letter-spacing: 1px;
    margin-bottom: 2px;
}
.chip-buyin {
    font-size: 0.75rem;
    color: #5a7a50;
    margin-bottom: 8px;
}

/* ── Inputs ── */
.stTextInput input, .stNumberInput input {
    background: rgba(5,15,8,0.95) !important;
    border: 1px solid rgba(45,80,55,0.7) !important;
    border-radius: 10px !important;
    color: #d8f0d8 !important;
    font-size: 0.95rem !important;
    padding: 10px 14px !important;
    height: 44px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: rgba(212,175,55,0.5) !important;
    box-shadow: 0 0 0 3px rgba(212,175,55,0.07) !important;
    outline: none !important;
}
.stSelectbox > div > div {
    background: rgba(5,15,8,0.95) !important;
    border: 1px solid rgba(45,80,55,0.7) !important;
    border-radius: 10px !important;
    color: #d8f0d8 !important;
    min-height: 44px !important;
}
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    color: #3a6040 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.4px !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #1a3d22 0%, #225530 100%) !important;
    color: #d4af37 !important;
    border: 1px solid rgba(212,175,55,0.4) !important;
    border-radius: 12px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    height: 50px !important;
    text-transform: uppercase !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #225530 0%, #2d6a3c 100%) !important;
    border-color: rgba(212,175,55,0.7) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result cards ── */
.res-card {
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 9px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    position: relative;
    overflow: hidden;
}
.res-card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 14px;
    pointer-events: none;
}
.res-profit {
    background: rgba(20,60,30,0.5);
    border: 1px solid rgba(60,180,80,0.35);
}
.res-loss {
    background: rgba(70,15,15,0.5);
    border: 1px solid rgba(220,60,60,0.35);
}
.res-even {
    background: rgba(25,30,40,0.5);
    border: 1px solid rgba(80,100,130,0.3);
}
.res-name {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #e0e8e0;
    letter-spacing: 0.5px;
}
.res-label {
    font-size: 0.7rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 2px;
}
.res-amount {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    text-align: right;
    white-space: nowrap;
}
.bar-wrap {
    width: 100%;
    height: 3px;
    background: rgba(255,255,255,0.05);
    border-radius: 3px;
    margin-top: 8px;
    overflow: hidden;
}

/* ── Transaction card ── */
.txn-card {
    background: rgba(12,20,14,0.8);
    border: 1px solid rgba(212,175,55,0.2);
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 9px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
}
.txn-from {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.0rem;
    font-weight: 700;
    color: #ff7070;
    background: rgba(200,50,50,0.1);
    border: 1px solid rgba(200,50,50,0.25);
    border-radius: 8px;
    padding: 4px 12px;
}
.txn-to {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.0rem;
    font-weight: 700;
    color: #60d090;
    background: rgba(50,180,80,0.1);
    border: 1px solid rgba(50,180,80,0.25);
    border-radius: 8px;
    padding: 4px 12px;
}
.txn-amt {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #d4af37;
    background: rgba(212,175,55,0.1);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 8px;
    padding: 4px 12px;
}
.txn-word {
    font-size: 0.8rem;
    color: #3a5040;
    letter-spacing: 0.5px;
}

/* ── Stat grid ── */
.stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 1.2rem 0;
}
.stat-tile {
    background: rgba(14,28,16,0.85);
    border: 1px solid rgba(45,80,50,0.5);
    border-radius: 14px;
    padding: 14px 16px;
    text-align: center;
}
.stat-lbl {
    font-size: 0.68rem;
    color: #3a6040;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.stat-val {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #d4af37;
    line-height: 1;
}

/* ── Divider ── */
.gold-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.25), transparent);
    margin: 1.4rem 0;
}

/* ── Warning ── */
.warn-box {
    background: rgba(90,55,10,0.35);
    border: 1px solid rgba(200,150,30,0.3);
    border-radius: 10px;
    padding: 10px 14px;
    color: #c8a040;
    font-size: 0.83rem;
    margin: 6px 0;
}

/* ── Table ── */
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
.stDataFrame thead tr th {
    background: rgba(14,35,18,0.95) !important;
    color: #3a7050 !important;
    font-size: 0.75rem !important;
    letter-spacing: 1px !important;
}
.stDataFrame tbody tr td { font-size: 0.88rem !important; }

/* ── Number input arrows hide ── */
input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; }
input[type=number] { -moz-appearance: textfield; }

/* ── Footer ── */
.footer {
    text-align: center;
    color: #1e3a24;
    font-size: 0.72rem;
    letter-spacing: 2.5px;
    margin-top: 2rem;
    padding-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# HERO
# ─────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-chip">🃏 &nbsp; Night Game</div>
    <div class="hero-title">POKER<br>SETTLEMENT</div>
    <div class="hero-sub">Track · Borrow · Settle</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────
# STEP 1 — PLAYERS
# ─────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-num">1</div>
    <div class="sec-title">Players &amp; Buy-in</div>
    <div class="sec-line"></div>
</div>
""", unsafe_allow_html=True)

num_players = st.number_input(
    "Number of players", min_value=2, max_value=20, step=1, value=2
)

players = []
boot_data = {}

for i in range(int(num_players)):
    st.markdown(
        f'<div class="player-card">'
        f'<div class="player-label">Player {i + 1}</div>',
        unsafe_allow_html=True
    )
    name = st.text_input(
        "Name", key=f"name_{i}", placeholder=f"Enter name",
        label_visibility="collapsed"
    )
    buy = st.number_input(
        "Buy-in (₹)", min_value=0, step=10, key=f"boot_{i}",
        placeholder="Buy-in amount"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if name.strip():
        players.append(name.strip())
        boot_data[name.strip()] = buy

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────
# STEP 2 — BORROWINGS
# ─────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-num">2</div>
    <div class="sec-title">Borrowings</div>
    <div class="sec-line"></div>
</div>
""", unsafe_allow_html=True)

if not players:
    st.markdown(
        '<div class="warn-box">⚠️ Add player names above first.</div>',
        unsafe_allow_html=True
    )

loan_count = st.number_input(
    "Number of borrowing transactions",
    min_value=0, max_value=50, step=1, value=0
)

loan_entries = []

for i in range(int(loan_count)):
    st.markdown(
        f'<div class="loan-card">'
        f'<div class="loan-label">Transaction {i + 1}</div>',
        unsafe_allow_html=True
    )
    opts = players if players else ["—"]
    giver = st.selectbox("Who gave the chips?", opts, key=f"giver_{i}")
    st.markdown('<div class="arrow-badge">↓ &nbsp; Lent to</div>', unsafe_allow_html=True)
    receiver = st.selectbox("Who received the chips?", opts, key=f"recv_{i}")
    amount = st.number_input("Amount (₹)", min_value=0, step=10, key=f"loan_{i}")
    st.markdown('</div>', unsafe_allow_html=True)

    if players:
        if giver == receiver:
            st.markdown(
                '<div class="warn-box">⚠️ Giver and receiver must be different.</div>',
                unsafe_allow_html=True
            )
        else:
            loan_entries.append((giver, receiver, amount))

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────
# STEP 3 — FINAL CHIPS
# ─────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-num">3</div>
    <div class="sec-title">Final Chip Count</div>
    <div class="sec-line"></div>
</div>
""", unsafe_allow_html=True)

if not players:
    st.markdown(
        '<div class="warn-box">⚠️ Add player names in Step 1 first.</div>',
        unsafe_allow_html=True
    )

final_amounts = {}

for p in players:
    buyin = boot_data[p]
    st.markdown(
        f'<div class="chip-card">'
        f'<div class="chip-name">{p}</div>'
        f'<div class="chip-buyin">Bought in: ₹{buyin:,}</div>',
        unsafe_allow_html=True
    )
    amt = st.number_input(
        "Final chips (₹)", min_value=0, step=10, key=f"final_{p}",
        placeholder="Count chips and enter"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    final_amounts[p] = amt

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────
# CALCULATE
# ─────────────────────────────────────────
calc = st.button("🃏  Calculate Settlement", use_container_width=True)

if calc:
    if len(players) < 2:
        st.error("Add at least 2 players with names to calculate.")
    else:
        # Net balances
        balances = {p: final_amounts[p] - boot_data[p] for p in players}
        for giver, receiver, amount in loan_entries:
            balances[giver] += amount
            balances[receiver] -= amount

        total_buy  = sum(boot_data[p] for p in players)
        total_pool = sum(final_amounts[p] for p in players)
        winners    = sum(1 for p in players if balances[p] > 0)
        max_abs    = max((abs(balances[p]) for p in players), default=1) or 1

        # ── Stats ──
        st.markdown(f"""
        <div class="stat-grid">
            <div class="stat-tile">
                <div class="stat-lbl">Players</div>
                <div class="stat-val">{len(players)}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-lbl">Winners</div>
                <div class="stat-val">{winners}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-lbl">Total Buy-in</div>
                <div class="stat-val">₹{total_buy:,}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-lbl">Final Pool</div>
                <div class="stat-val">₹{total_pool:,}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

        # ── P/L ──
        st.markdown("""
        <div class="sec-head">
            <div class="sec-num">✦</div>
            <div class="sec-title">Profit / Loss</div>
            <div class="sec-line"></div>
        </div>
        """, unsafe_allow_html=True)

        for p in players:
            bal   = balances[p]
            pct   = int(abs(bal) / max_abs * 100)
            if bal > 0:
                bar_color = "#3cb86a"
                card_cls  = "res-profit"
                lbl_html  = '<span style="color:#3cb86a;font-size:0.7rem;letter-spacing:1px">▲ PROFIT</span>'
                amt_color = "#52e87a"
                sign      = "+"
            elif bal < 0:
                bar_color = "#e05050"
                card_cls  = "res-loss"
                lbl_html  = '<span style="color:#e05050;font-size:0.7rem;letter-spacing:1px">▼ LOSS</span>'
                amt_color = "#ff6060"
                sign      = "−"
            else:
                bar_color = "#5a7080"
                card_cls  = "res-even"
                lbl_html  = '<span style="color:#5a7080;font-size:0.7rem;letter-spacing:1px">— EVEN</span>'
                amt_color = "#7090a0"
                sign      = ""

            st.markdown(f"""
            <div class="res-card {card_cls}">
                <div style="flex:1;min-width:0">
                    <div class="res-name">{p}</div>
                    {lbl_html}
                    <div class="bar-wrap">
                        <div style="height:3px;width:{pct}%;background:{bar_color};border-radius:3px;transition:width 0.6s"></div>
                    </div>
                </div>
                <div class="res-amount" style="color:{amt_color}">
                    {sign}₹{abs(bal):,}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

        # ── Settlement ──
        st.markdown("""
        <div class="sec-head">
            <div class="sec-num">✦</div>
            <div class="sec-title">Settlements</div>
            <div class="sec-line"></div>
        </div>
        """, unsafe_allow_html=True)

        creditors = [[p, balances[p]]       for p in players if balances[p] > 0]
        debtors   = [[p, abs(balances[p])]  for p in players if balances[p] < 0]

        ci = di = 0
        transactions = []
        while di < len(debtors) and ci < len(creditors):
            debtor, da   = debtors[di]
            creditor, ca = creditors[ci]
            pay          = min(da, ca)
            transactions.append((debtor, creditor, pay))
            debtors[di][1]   -= pay
            creditors[ci][1] -= pay
            if debtors[di][1]   == 0: di += 1
            if creditors[ci][1] == 0: ci += 1

        if not transactions:
            st.success("✅ Everyone is settled — no transfers needed!")
        else:
            for frm, to, amt in transactions:
                st.markdown(f"""
                <div class="txn-card">
                    <span class="txn-from">{frm}</span>
                    <span class="txn-word">pays</span>
                    <span class="txn-amt">₹{amt:,}</span>
                    <span class="txn-word">to</span>
                    <span class="txn-to">{to}</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

        # ── Summary table ──
        st.markdown("""
        <div class="sec-head">
            <div class="sec-num">✦</div>
            <div class="sec-title">Summary</div>
            <div class="sec-line"></div>
        </div>
        """, unsafe_allow_html=True)

        df = pd.DataFrame([{
            "Player":         p,
            "Buy-in (₹)":     boot_data[p],
            "Final (₹)":      final_amounts[p],
            "Net P/L (₹)":    balances[p],
            "Result":         "✅ Profit" if balances[p] > 0 else "❌ Loss" if balances[p] < 0 else "— Even"
        } for p in players])

        st.dataframe(
            df, use_container_width=True, hide_index=True,
            column_config={
                "Buy-in (₹)":  st.column_config.NumberColumn(format="₹%d"),
                "Final (₹)":   st.column_config.NumberColumn(format="₹%d"),
                "Net P/L (₹)": st.column_config.NumberColumn(format="₹%d"),
            }
        )

        st.markdown('<div class="footer">♠ &nbsp; PLAY RESPONSIBLY &nbsp; ♣</div>', unsafe_allow_html=True)
