import random
import streamlit as st

st.title("fight fight fight")
st.write(
    "if something breaks, don't sue me! no graphics bc im a loser\n"
)

charas = ["One", "Two", "Three", "Four"]
S = int((len(charas)*len(charas) - len(charas)) / 2 )
# 4 charas = 6 ships

ships = ["yes"] * S
a = 0
b = 1
for x in range(len(ships)):
	ships[x] = charas[a] + " x " + charas[b]
	b += 1
	if (b == len(charas)):
		a += 1
		b = a + 1
		

rows, cols = (S, S)
rank = [[0]*cols]*rows

choose1 = st.button("i like the first one")
choose2 = st.button("i like the second one")
chooseTie = st.button("🤷‍♀️")

Option1 = st.text("")
Option2 = st.text("")

# buttons go here
finished = False
selection = True
while (not finished) and (selection == True):
    finished = True
    selection = False
    for i in range(S):
        for j in range(S):
            if rank[i][j] == 0:
                finished = False
    P1 = random.randint(0, S-1)
    while 0 not in rank[P1]:
        P1 = (P1 + 1) % S
    P2 = random.randint(0, S-1)

    while (P2 == P1) or (rank[P1][P2] != 0):
        P2 = (P2 + 1) % S
    Option1.write(ships[P1] + "!!")
    Option2.write(ships[P2] + "!!")
    if choose1:
        rank[P1][P2] = 1
        rank[P2][P1] = 3
        if rank[i][P1] == 1:
                rank[i][P2] = 1
                rank[P2][i] = 3
        elif rank[i][P1] == 2:
            rank[i][P2] = 1
            rank[P2][i] = 3

        if rank[i][P2] == 3:
            rank[i][P1] = 3
            rank[P1][i] = 1
        elif rank[i][P2] == 2:
            rank[i][P1] = 3
            rank[P1][i] = 1
        selection = True
    elif chooseTie:
        rank[P1][P2] = 2
        rank[P2][P1] = 2
        for i in range(S):
            if rank[i][P2] == 1: # Wins against P2
                rank[i][P1] = 1
                rank[P1][i] = 3
            elif rank[i][P2] == 3: # Loses against P2
                rank[i][P1] = 3
                rank[P1][i] = 1
            elif rank[i][P2] == 2:
                rank[i][P1] = 2
                rank[P1][i] = 2
            
            if rank[i][P1] == 1: # Wins against P1
                rank[i][P2] = 1
                rank[P2][i] = 3
            elif rank[i][P1] == 3: # Loses against P1
                rank[i][P2] = 3
                rank[P2][i] = 1
            elif rank[i][P1] == 2:
                rank[i][P2] = 2
                rank[P2][i] = 2
        selection = True
    elif choose2:
        rank[P2][P1] = 1
        rank[P1][P2] = 3
        for i in range(S):
            if rank[i][P2] == 1:
                rank[i][P1] = 1
                rank[P1][i] = 3
            elif rank[i][P2] == 2:
                rank[i][P1] = 1
                rank[P1][i] = 3

            if rank[i][P1] == 3:
                rank[i][P2] = 3
                rank[P2][i] = 1
            elif rank[i][P1] == 2:
                rank[i][P2] = 3
                rank[P2][i] = 1
        selection = True
    else:
        selection = False

st.title("the results!")



