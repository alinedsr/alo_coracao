import streamlit as st

def main():
    st.set_page_config(page_title="Teste do Espectro Romântico", layout="wide")
    st.title("🌈 Teste do Espectro Romântico")
    st.write("Descubra onde você pode se encaixar no espectro romântico e relacional!")
    
    st.header("📝 Responda às perguntas abaixo")
    
    # Perguntas
    q1 = st.radio("Você sente atração romântica por alguém frequentemente?", ["Sim, sempre", "Às vezes", "Muito raramente", "Nunca"])
    q2 = st.radio("Como você se sente em relação ao romance?", ["Amo e preciso disso!", "Gosto, mas não é essencial", "Indiferente", "Não gosto e evito"])
    q3 = st.radio("Você se sente confortável com demonstrações de afeto romântico?", ["Sim, adoro!", "Depende da situação", "Gosto mais de carinho não-romântico", "Não gosto nem um pouco"])
    q4 = st.radio("Se pudesse escolher, qual tipo de relação seria perfeita para você?", ["Um namoro romântico tradicional", "Uma parceria forte com romance ocasional", "Uma amizade intensa e comprometida", "Nenhum tipo de romance"])
    q5 = st.radio("Você se sente pressionado(a) pela sociedade para estar em um relacionamento romântico?", ["Não, eu gosto disso", "Às vezes", "Sim, bastante", "Totalmente, e não me identifico com isso"])
    
    if st.button("🔍 Ver Resultado"):
        resultado = determinar_resultado(q1, q2, q3, q4, q5)
        st.subheader("🎭 Seu resultado:")
        st.write(resultado)

def determinar_resultado(q1, q2, q3, q4, q5):
    if q1 == "Nunca" and q2 in ["Não gosto e evito", "Indiferente"] and q4 == "Nenhum tipo de romance":
        return "🌿 **Arromântico**: Você não sente atração romântica ou não se interessa por relacionamentos românticos! Isso não significa que você não pode ter conexões significativas, apenas que sua forma de amar é diferente do tradicional. 💚"
    
    if q1 == "Muito raramente" and q4 in ["Uma amizade intensa e comprometida", "Nenhum tipo de romance"]:
        return "⚖️ **Grayromântico**: Você sente atração romântica ocasionalmente, mas não com a frequência ou intensidade que a sociedade espera. Sua abordagem para relacionamentos pode ser única! 🌘"
    
    if q1 == "Às vezes" and q5 in ["Sim, bastante", "Totalmente, e não me identifico com isso"]:
        return "🌀 **Demirromântico**: Você só sente atração romântica depois de criar um vínculo emocional forte. Para você, conexão vem antes do romance! 🔗"
    
    if q4 == "Uma amizade intensa e comprometida" and q2 == "Indiferente":
        return "🤝 **Queerplatônico**: Você valoriza conexões profundas que não precisam seguir as regras de namoro ou romance. Suas relações podem ser mais fortes do que um romance tradicional! 🔥"
    
    return "💖 **Alorromântico**: Você se sente atraído romanticamente e gosta da ideia de relacionamentos tradicionais, o que é totalmente válido também! 🥰"

if __name__ == "__main__":
    main()
