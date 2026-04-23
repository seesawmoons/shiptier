import random
import streamlit as st

st.title("fight fight fight")
st.write(
    "if something breaks, don't sue me! no graphics bc im a loser"
)

charas = ["One", "Two", "Three", "Four"]
S = int((len(charas)*len(charas) - len(charas)) / 2 )
# 4 charas = 6 ships

ships = ["yes"]*S
a = 0
b = 1
for x in ships:
    #something loop
	x = charas[a] + " x " + charas[b]
	b += 1
	if (b == len(charas)):
		a += 1
		b = a + 1
		
	

rows, cols = (S, S)
rank = [[0]*cols]*rows

# buttons go here
while (0 in rank):
    P1 = random.randint(0, S-1)
    while 0 not in rank[P1]:
        P1 = (P1 + 1) % S
    P2 = random.randint(0, S-1)

    while (P2 == P1) or (rank[P1][P2] != 0):
        P2 = (P2 + 1) % S
    st.write("Option 1: " + ships[P1])
    st.write("Option 2: " + ships[P2])
    if st.button("First one"):
        rank[P1][P2] = 1
        rank[P2][P1] = 3
    elif st.button("🤷‍♀️"):
        rank[P1][P2] = 2
        rank[P2][P1] = 2
    elif st.button("Second one"):
        rank[P2][P1] = 1
        rank[P1][P2] = 3




