import random
import streamlit as st

st.title("fight fight fight")
st.write(
    "v1.2 - if something breaks, don't sue me! no graphics bc it's hard\n"
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
st.text("")
progressBar = st.text("PROGRESS : 0/" + str(total) + " ranked")
choose1 = st.button("i like the first one")
chooseTie = st.button("🤷‍♀️")
choose2 = st.button("i like the second one")

Option1 = st.text("")
Option2 = st.text("")
total = int((S*S - S) / 2)

progress = 0

# buttons go here
finished = False
selection = False
while (not finished) and (not selection):
    finished = True
    selection = True
    progress = total
    for i in range(S):
        for j in range(S):
            if rank[i][j] == 0:
                finished = False
                progress -= 1
    P1 = random.randint(0, S-1)
    while 0 not in rank[P1]:
        P1 = (P1 + 1) % S
    P2 = random.randint(0, S-1)

    while (P2 == P1) or (rank[P1][P2] != 0):
        P2 = (P2 + 1) % S
    progressBar.write("PROGRESS : " + str(progress) + "/" + str(total) + " ranked")
    Option1.write(ships[P1] + "!!")
    Option2.write(ships[P2] + "!!")

    while (selection):
        if choose1:
            rank[P1][P2] = 1
            rank[P2][P1] = 3
            for i in range(S):
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
            selection = False
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
            selection = False
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
            selection = False

st.title("final rankings")
maxWins = S
noEntries = 0
tentEntries = 0;
wins = [0] * S
for i in range(S):
    for j in range(S):
        if rank[i][j] == 1:
            wins[i] += 1


for i in range(S):
    noEntries = tentEntries
    maxWins -= 1
    for j in range(S):
        if wins[j] == maxWins:
            st.write(str(noEntries + 1) + ". " + ships[j])
            tentEntries += 1



