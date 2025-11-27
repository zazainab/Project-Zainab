import streamlit as st

st.title("🎬 Movie Mood!")
st.write("Pilihlah kondisimu dan kamu akan diberi rekomendasi film yang cocok!")

mood = st.selectbox(
    "Bagaimana mood kamu hari ini?",
    ["Senang", "Sedih", "Motivasi", "Santai", "Tegang", "Horor"]
)

rekomendasi = {
    "Senang": ["La La Land", "Paddington", "The Lego Movie"],
    "Sedih": ["The Pursuit of Happyness", "Inside Out", "A Silent Voice", "20th Century Girl"],
    "Motivasi": ["The Social Network", "The Martian", "Whiplash"],
    "Santai": ["Chef", "The Secret Life of Walter Mitty", "Kiki's Delivery Service", "Hear Me: Our Summer"],
    "Tegang": ["Inception", "Shutter Island", "Gone Girl", "Unlocked"],
    "Horor": ["Hereditary", "The Conjuring", "The Babadook", "Insidious", "Train to Busan"]
}

if st.button("Dapatkan Rekomendasi"):
    st.subheader("Rekomendasi untukmu:")
    for film in rekomendasi[mood]:
        st.write(f"- {film}")

st.caption("Aplikasi sederhana untuk rekomendasi film berdasarkan suasana hati")
