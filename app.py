import streamlit as st
from collections import defaultdict

st.title("🃏 Poker Settlement")

num_players = st.number_input(
    "Number of Players",
    min_value=2,
    step=1
)

players = []

for i in range(num_players):
    name = st.text_input(f"Player {i+1} Name", key=f"name{i}")
    if name:
        players.append(name)

boot = st.number_input(
    "Boot Amount",
    min_value=0,
    value=20
)

st.divider()

transactions = []

if len(players) >= 2:

    st.subheader("Borrow Transactions")

    t_count = st.number_input(
        "Number of Transactions",
        min_value=0,
        step=1
    )

    for i in range(t_count):

        col1, col2, col3 = st.columns(3)

        with col1:
            lender = st.selectbox(
                f"Lender {i}",
                players,
                key=f"lend{i}"
            )

        with col2:
            borrower = st.selectbox(
                f"Borrower {i}",
                players,
                key=f"borrow{i}"
            )

        with col3:
            amount = st.number_input(
                f"Amount {i}",
                min_value=0,
                key=f"amt{i}"
            )

        transactions.append(
            (lender, borrower, amount)
        )

    st.divider()

    st.subheader("Final Chips")

    final_chips = {}

    for player in players:

        chips = st.number_input(
            f"{player} Final Chips",
            min_value=0,
            key=f"chips{player}"
        )

        final_chips[player] = chips

    if st.button("Calculate"):

        loans_given = defaultdict(int)
        loans_taken = defaultdict(int)

        for lender, borrower, amount in transactions:

            loans_given[lender] += amount
            loans_taken[borrower] += amount

        results = {}

        st.header("Results")

        for player in players:

            net = (
                final_chips[player]
                + loans_given[player]
                - loans_taken[player]
                - boot
            )

            results[player] = net

            st.write(f"{player}: {net}")

        creditors = []
        debtors = []

        for p, amt in results.items():

            if amt > 0:
                creditors.append([p, amt])

            elif amt < 0:
                debtors.append([p, -amt])

        st.header("Settlement")

        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):

            d_name, d_amt = debtors[i]
            c_name, c_amt = creditors[j]

            settlement = min(d_amt, c_amt)

            st.write(
                f"{d_name} pays {c_name} → {settlement}"
            )

            debtors[i][1] -= settlement
            creditors[j][1] -= settlement

            if debtors[i][1] == 0:
                i += 1

            if creditors[j][1] == 0:
                j += 1