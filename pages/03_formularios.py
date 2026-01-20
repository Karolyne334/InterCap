import streamlit as st

st.title("formularios")

st.header("Preencha o formulário abaixo")

st.markdown("""---""")

with st.form("formCadastro"):

        nome = st.text_input("Informe seu nome:", placeholder="Preencha o seu nome")

        idade = st.number_input("Informe sua idade:", min_value=10, max_value=100, step=1)

        dataNascimento = st.date_input("Dt. Nascimento", format="DD/MM/YYYY")

        horaAtual = st.time_input("Selecione a hora:", step=60)

        corPerfil = st.color_picker("Selecione a cor do perfil")

        btnFormCadastro = st.form_submit_button("Cadastrar")

        if btnFormCadastro:
                if not nome:
                        st.error("Preencha o nome")
                elif len(nome) <= 2:
                        st.error("Nome precisa ter no minímo 2 letras")
                else:
                        st.write("Nome:", nome)
                        st.write("Idade:", idade)
                        st.write("Data Nascimento:", dataNascimento)
                        st.write("Hora Atual:", horaAtual)

                        st.markdown(
                        f"<h1 style='color:{corPerfil}'>Essa é a cor que você escolheu para o seu perfil</h1>",
                        unsafe_allow_html=True
                        )


