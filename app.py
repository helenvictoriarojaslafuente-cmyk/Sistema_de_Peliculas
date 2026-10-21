import streamlit as st
from PIL import Image
import Usuario
import Funciones
st.set_page_config(
    page_title="Tienda Virtual de Películas", 
    page_icon="🎬", 
    layout="wide")
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: #ffffff;}
    h1, h2, h3 {
        color: #e50914 !important;}
    .pelicula-card {
        background-color: #1f1f1f;
        padding: 15px;
        border-radius: 10px;
        text-align: center;}
    </style>
""", unsafe_allow_html=True)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.title(" Bienvenido a la Tienda de Películas")
    st.subheader("Por favor, inicia sesión para continuar")   
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user_input = st.text_input("Usuario")
        pass_input = st.text_input("Contraseña", type="password")        
        if st.button("Iniciar Sesión", use_container_width=True):            
            # exito = Usuario.verificar_login(user_input, pass_input)
            if user_input != "" and pass_input != "": 
                st.session_state.logged_in = True
                st.session_state.usuario_actual = user_input
                st.rerun() 
            else:
                st.error("Por favor ingresa usuario y contraseña válidos.")
else:
    st.sidebar.success(f"Sesión activa: {st.session_state.usuario_actual}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.logged_in = False
        st.rerun()
    st.title(" Catálogo de Películas")
    catalogo_generos = {
        "Acción": [
            {"titulo": "Mad Max", "precio": 9.99, "img": "https://via.placeholder.com/150"},
            {"titulo": "John Wick", "precio": 11.50, "img": "https://via.placeholder.com/150"}
        ],
        "Comedia": [
            {"titulo": "Superbad", "precio": 7.99, "img": "https://via.placeholder.com/150"},
            {"titulo": "¿Qué pasó ayer?", "precio": 8.50, "img": "https://via.placeholder.com/150"}
        ],
        "Ciencia Ficción": [
            {"titulo": "Interestelar", "precio": 12.00, "img": "https://via.placeholder.com/150"},
            {"titulo": "Matrix", "precio": 10.00, "img": "https://via.placeholder.com/150"}
        ]
    }
    nombres_generos = [" Recomendadas"] + list(catalogo_generos.keys())
    tabs = st.tabs(nombres_generos)
    with tabs[0]:
        st.header(" Películas Recomendadas para Ti")
        st.write("Las más populares de la semana:")        
        cols = st.columns(4)
        recomendadas = [
            {"titulo": "Interestelar", "precio": 12.00, "img": "https://via.placeholder.com/150"},
            {"titulo": "John Wick", "precio": 11.50, "img": "https://via.placeholder.com/150"},
            {"titulo": "Mad Max", "precio": 9.99, "img": "https://via.placeholder.com/150"},
            {"titulo": "Matrix", "precio": 10.00, "img": "https://via.placeholder.com/150"}
        ]        
        for idx, pelicula in enumerate(recomendadas):
            with cols[idx]:
                st.image(pelicula["img"], use_container_width=True)
                st.markdown(f"**{pelicula['titulo']}**")
                st.write(f"Precio: ${pelicula['precio']}")
                if st.button("Comprar", key=f"rec_{pelicula['titulo']}"):
                    st.success(f"¡Compraste {pelicula['titulo']}!")
    for i, (genero, peliculas_del_genero) in enumerate(catalogo_generos.items()):
        with tabs[i + 1]:
            st.header(f"Películas de {genero}")
            cols = st.columns(3)
            for j, pelicula in enumerate(peliculas_del_genero):
                with cols[j % 3]:
                    st.image(pelicula["img"], use_container_width=True)
                    st.subheader(pelicula["titulo"])
                    st.write(f"**Precio:** ${pelicula['precio']}")
                    
                    if st.button(f"Comprar {pelicula['titulo']}", key=f"{genero}_{pelicula['titulo']}"):
                       
                        st.success(f"¡Has agregado '{pelicula['titulo']}' al carrito!")