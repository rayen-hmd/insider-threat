import streamlit as st

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="etape 2 et 3: methode mise en ligne",
    layout="centered"
)

# -----------------------------
# INITIALISATION SESSION STATE
# -----------------------------
if 'etape' not in st.session_state:
    st.session_state.etape = 0

# -----------------------------
# STYLE GLOBAL
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0d1b2a;
}

/* TITRE */
h1 {
    text-align: center;
    color: #ffffff;
    font-size: 42px;
    font-weight: bold;
}

/* PARAGRAPHE */
p {
    text-align: center;
    color: #0d1b2a;
    font-size: 18px;
}

/* INPUT */
input {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
    border-radius: 20px !important;
    border: 2px solid #4a90e2 !important;
    padding: 12px !important;
    font-size: 18px !important;
}

/* BOUTON */
.stButton > button {
    background-color: #2c3e50;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 15px;
    padding: 10px 30px;
    display: block;
    margin: auto;
    border: 2px solid #4a90e2;
}

.stButton > button:hover {
    background-color: #34495e;
}

/* MESSAGE BOX */
.box {
    background-color: #1a1a1a;
    color: #ffffff;
    font-size: 20px;
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
    text-align: center;
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# CONTENU
# -----------------------------

# ---------- ÉTAPE 0 ----------
if st.session_state.etape >= 0:
    st.markdown(
        "<h1>Zs htzufgqj ufwrn stzx, xznaje qjx nsinhjx utzw qj ywtzajw.</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p>Il faut trouver le coupable. Entrez la phrase correcte pour continuer.</p>",
        unsafe_allow_html=True
    )
    phrase = st.text_input(
        "", 
        placeholder="Écrivez la réponse ici...", 
        key="phrase_input"
    )
    if st.button("Exécuter"):
        if phrase == "un coupable parmi nous, suivez les indices pour le trouver.":
            st.session_state.etape = max(st.session_state.etape, 1)
            st.rerun()
        else:
            st.markdown("""
            <div class="box">
            ❌ Phrase incorrecte. Essayez de nouveau.
            </div>
            """, unsafe_allow_html=True)
            st.session_state.phrase_input = ""  # vider champ

# ---------- ÉTAPE 1 ----------
if st.session_state.etape >= 1:
    st.markdown("""
    <div class="box">
    ✅ <b>Bon travail !</b><br><br>
    Les caméras de surveillance ont capturé une image d'une personne
    quittant l'entreprise à <b>22 h du soir</b>.<br>
    Malheureusement, l'image est floue.<br><br>
    Pour révéler la vérité, il faudra appliquer une <b>technique de restauration d'image</b>
    basée sur la <b>mise en ligne des postes de traitement</b>.
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "C:/Users/wiki/Desktop/Orion/avant.png",
        caption="Image issue des caméras de surveillance"
    )

    code = st.text_input(
        "", 
        placeholder="Écrivez le code ici...", 
        key="code_input"
    )
    if st.button("Valider"):
        if code == "7342615":
            st.session_state.etape = max(st.session_state.etape, 2)
            st.rerun()
        else:
            st.markdown("""
            <div class="box">
            ❌ Code incorrect. Analysez de nouveau les postes de traitement.
            </div>
            """, unsafe_allow_html=True)
            st.session_state.code_input = ""  # vider champ

# ---------- ÉTAPE 2 ----------
if st.session_state.etape >= 2:
    st.image(
        "C:/Users/wiki/Desktop/Orion/apres.png",
        caption="Image restaurée finale"
    )
    st.markdown("""
    <div class="box">
    🎉 <b>Bravo ! Voici votre premier indice.</b><br><br>
    L'image a été restaurée avec succès.<br>
    Les caméras de surveillance ont capturé une image d’une personne
entrant dans l’entreprise après 22h.<br><br>
    <b>Qui est cette personne mystérieuse ?</b><br>
    Pour le trouver, passez à l'étape 4 dans les pages de navigation.
    </div>
    """, unsafe_allow_html=True)
