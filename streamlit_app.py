import streamlit as st

st.set_page_config(
    page_title="InterCap",
    initial_sidebar_state="expanded" #força abrir o menu
)

# titulo
st.title("InterCap")

# header
st.header("Entre capítulos, suas ideias ganham vida!")

# subcabeçalho
st.subheader("Sub Cabeçalho para vcer como é")

st.subheader("Primeira seção")

# texto qualquer
st.text("Essa é a primeira seção e isso aqui é só um texto")

st.subheader("Segunda Seção")

# escrever - write
st.write("Isso aqui é só uma escrita de texto")



#markdown
st.markdown("""---""")
st.markdown("Esse é um texto usando Markdown")
st.markdown("# Esse é um cabeçalho em Markdown")
st.markdown("## Esse é um subtitulo")
st.markdown("### Terceiro nivel de titulo em markdown")

st.markdown("Esse aqui é um tutorial, **preste atenção** *é importante*")

st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")

st.text("Lista de tarefas:")
st.markdown("""
            1. Criar uma conta no [streamlit.io](www.streamlit.io)
            2. Criar uma conta no github.com
            3. Criar um projeto no streamlit
            4. Assistir os videos do tutorial :)
            5. praticar, praticar, praticar
            """)

st.markdown("""---""")

# Emojis
st.markdown("### Emojis")
st.markdown("[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)")
st.markdown(":+1::heart: :books: :rocket: :smile::checkered_flag:")

st.markdown("""---""")

#HTML
st.markdown("### HTML")

html_code = """
    <h1 style='color: pink;'>Esse é um cabeçalho rosa</h1>
    <p style='color: purple;'> Esse é um paragrafo</p>
"""

st.markdown(html_code, unsafe_allow_html=True)