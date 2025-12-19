import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="etape 4: Tri",
    layout="centered"
)
# -----------------------------
# 1️⃣ Lecture du fichier Excel (CACHÉE)
# -----------------------------
fichier = "datatime.xlsx"
df = pd.read_excel(fichier)

# 4ème colonne : Heure de sortie
heures_sortie = df.iloc[:, 3].tolist()

# -----------------------------
# 2️⃣ Interface (SANS afficher les données)
# -----------------------------
st.title("ÉTAPE 4 – Tri de la base de données")
st.markdown("""
**Consigne :**  
Complétez la fonction `tri(liste)` en utilisant **l’algorithme du tri à bulles**.  
Si votre fonction est correcte, vous auriez le deuxieme indice.
""")

# Zone de code à compléter par l'utilisateur
user_code = st.text_area(
    "✍️ Écrire votre code ici :",
    value="""
def tri(liste):
    # compléter le tri à bulles
    pass
""",
    height=180
)

# -----------------------------
# 3️⃣ Test de la fonction
# -----------------------------
if st.button("Tester mon code"):
    local_vars = {}

    try:
        exec(user_code, {}, local_vars)

        if "tri" not in local_vars:
            st.error("❌ La fonction tri() n'a pas été définie.")
        else:
            tri_user = local_vars["tri"]
            resultat = tri_user(heures_sortie.copy())

            if resultat == sorted(heures_sortie):
                st.success("✅ Bravo ! Votre algorithme est correct.")

                # -----------------------------
                # 4️⃣ Affichage DU RÉSULTAT SEULEMENT
                # -----------------------------
                df_trie = df.sort_values(df.columns[3])

                st.subheader("📊 Base de données triée (par heure de sortie)")
                st.dataframe(df_trie)

                

            else:
                st.error("❌ Le tri est incorrect.")
                st.write("Résultat obtenu :", resultat)

    except Exception as e:
        st.error("❌ Erreur dans votre code")
        st.code(e)




#streamlit run "C:\Users\wiki\Desktop\Orion\tri.py"
