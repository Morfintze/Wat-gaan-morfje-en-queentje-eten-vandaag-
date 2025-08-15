import streamlit as st
import random

# Titel en beschrijving
st.title("🍽 Dinner Randomizer")
st.write("Druk op de knop en laat het lot bepalen wat je vanavond eet!")

# Lijst met dinners (exact zoals jij hem gaf)
dinners = [
    "Morfjes bonensalade",
    "Queentjes bonensalade",
    "Baba Ganoush",
    "Courgette aubergine (en vergeet de aardappoltjes niet)",
    "Spinazi en broccolischotel :D",
    "Curry",
    "Pasta pesto met balletjes",
    "Soep (welke dan ook)",
    "Avocado met geroosterd brood en tofu",
    "Lentils",
    "Marielas potato stew",
    "zoete aardappel friet",
    "Sperziebonen en aardappelpuree",
    "Ovenschotel met gegrilde diepvriesgroenten",
    "Sperziebonen en rijst",
    "Queentjes Russian Salad",
    "Spaghetti tomatensaus en spaghettigroenten uit zak",
    "Noodles met wokgroenten"
      
]

# Knop voor randomizer
if st.button("🎲 Kies mijn avondeten"):
    choice = random.choice(dinners)
    st.success(f"**Vanavond eet je:** {choice}")
