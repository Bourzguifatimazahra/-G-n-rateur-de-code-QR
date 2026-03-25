# Requires: pip install qrcode[pil] pillow streamlit
import qrcode
from PIL import Image
import streamlit as st
import io
import time
import sys

# Vérification de la version de Python
if sys.version_info >= (3, 12):
    st.warning("⚠️ Version Python 3.12+ détectée. Assurez-vous que Pillow est compatible.")

def main():
    # Page configuration
    st.set_page_config(
        page_title="QR Code Generator",
        page_icon="📱",
        layout="centered"
    )
    
    # Language selector in sidebar
    with st.sidebar:
        st.markdown("### 🌐 Language / اللغة / Idioma")
        language = st.selectbox(
            "Select your language:",
            options=['fr', 'en', 'ar', 'es'],
            format_func=lambda x: {
                'fr': 'Français 🇫🇷',
                'en': 'English 🇬🇧',
                'ar': 'العربية 🇸🇦',
                'es': 'Español 🇪🇸'
            }[x]
        )
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.info("Generate professional QR codes instantly!")
        
        st.markdown("### 📊 Statistics")
        if 'qr_count' not in st.session_state:
            st.session_state.qr_count = 0
        st.metric("QR Codes Generated", st.session_state.qr_count)
    
    # Dictionary for translations
    translations = {
        'fr': {
            'title': "📱 Générateur de Code QR",
            'subtitle': "Générez des codes QR pour n'importe quelle URL ou texte!",
            'url_label': "Entrez l'URL ou le texte à encoder:",
            'url_placeholder': "https://example.com ou n'importe quel texte...",
            'customization': "🔧 Options de personnalisation",
            'box_size': "Taille des blocs:",
            'border': "Bordure:",
            'color_scheme': "Schéma de couleurs:",
            'bw': "Noir & Blanc",
            'custom_colors': "Couleurs personnalisées",
            'qr_color': "Couleur du QR Code:",
            'bg_color': "Couleur d'arrière-plan:",
            'generate': "Générer le Code QR",
            'generating': "Génération...",
            'success': "✅ Code QR généré avec succès!",
            'error': "❌ Erreur:",
            'warning': "⚠️ Veuillez entrer une URL ou un texte.",
            'your_qr': "📸 Votre Code QR",
            'details': "📋 Informations",
            'encoded_content': "Contenu encodé:",
            'file_size': "Taille du fichier:",
            'generation_date': "Date:",
            'download': "📥 Télécharger (PNG)",
            'another': "🔄 Nouveau QR Code",
            'examples': "💡 Exemples",
            'footer': "✨ Fabriqué avec ❤️"
        },
        'en': {
            'title': "📱 QR Code Generator",
            'subtitle': "Generate QR codes for any URL or text!",
            'url_label': "Enter URL or text to encode:",
            'url_placeholder': "https://example.com or any text...",
            'customization': "🔧 Customization Options",
            'box_size': "Box Size:",
            'border': "Border:",
            'color_scheme': "Color Scheme:",
            'bw': "Black & White",
            'custom_colors': "Custom Colors",
            'qr_color': "QR Code Color:",
            'bg_color': "Background Color:",
            'generate': "Generate QR Code",
            'generating': "Generating...",
            'success': "✅ QR Code generated successfully!",
            'error': "❌ Error:",
            'warning': "⚠️ Please enter a URL or text.",
            'your_qr': "📸 Your QR Code",
            'details': "📋 Details",
            'encoded_content': "Encoded content:",
            'file_size': "File size:",
            'generation_date': "Date:",
            'download': "📥 Download (PNG)",
            'another': "🔄 New QR Code",
            'examples': "💡 Examples",
            'footer': "✨ Made with ❤️"
        },
        'ar': {
            'title': "📱 مولد رمز QR",
            'subtitle': "إنشاء رموز QR لأي عنوان URL أو نص!",
            'url_label': "أدخل عنوان URL أو النص:",
            'url_placeholder': "https://example.com أو أي نص...",
            'customization': "🔧 خيارات التخصيص",
            'box_size': "حجم المربع:",
            'border': "الحدود:",
            'color_scheme': "نظام الألوان:",
            'bw': "أسود وأبيض",
            'custom_colors': "ألوان مخصصة",
            'qr_color': "لون رمز QR:",
            'bg_color': "لون الخلفية:",
            'generate': "إنشاء رمز QR",
            'generating': "جاري الإنشاء...",
            'success': "✅ تم الإنشاء بنجاح!",
            'error': "❌ خطأ:",
            'warning': "⚠️ يرجى إدخال عنوان URL أو نص.",
            'your_qr': "📸 رمز QR الخاص بك",
            'details': "📋 معلومات",
            'encoded_content': "المحتوى:",
            'file_size': "حجم الملف:",
            'generation_date': "التاريخ:",
            'download': "📥 تحميل (PNG)",
            'another': "🔄 رمز جديد",
            'examples': "💡 أمثلة",
            'footer': "✨ تم الصنع بحب"
        },
        'es': {
            'title': "📱 Generador de Código QR",
            'subtitle': "¡Genere códigos QR para cualquier URL o texto!",
            'url_label': "Ingrese URL o texto:",
            'url_placeholder': "https://example.com o cualquier texto...",
            'customization': "🔧 Opciones",
            'box_size': "Tamaño:",
            'border': "Borde:",
            'color_scheme': "Esquema:",
            'bw': "Blanco y Negro",
            'custom_colors': "Colores Personalizados",
            'qr_color': "Color del QR:",
            'bg_color': "Color de fondo:",
            'generate': "Generar QR",
            'generating': "Generando...",
            'success': "✅ ¡QR generado con éxito!",
            'error': "❌ Error:",
            'warning': "⚠️ Ingrese una URL o texto.",
            'your_qr': "📸 Tu Código QR",
            'details': "📋 Detalles",
            'encoded_content': "Contenido:",
            'file_size': "Tamaño:",
            'generation_date': "Fecha:",
            'download': "📥 Descargar (PNG)",
            'another': "🔄 Nuevo QR",
            'examples': "💡 Ejemplos",
            'footer': "✨ Hecho con ❤️"
        }
    }
    
    t = translations[language]
    
    # Title and description
    st.title(t['title'])
    st.markdown(t['subtitle'])
    st.markdown("---")
    
    # Initialize session state
    if 'qr_generated' not in st.session_state:
        st.session_state.qr_generated = False
        st.session_state.qr_bytes = None
        st.session_state.qr_content = ""
    
    # Input form
    with st.form("qr_form"):
        url = st.text_input(
            t['url_label'],
            placeholder=t['url_placeholder']
        )
        
        with st.expander(t['customization']):
            col1, col2 = st.columns(2)
            with col1:
                box_size = st.slider(t['box_size'], 5, 20, 10)
            with col2:
                border = st.slider(t['border'], 1, 10, 4)
            
            color_scheme = st.selectbox(t['color_scheme'], [t['bw'], t['custom_colors']])
            
            if color_scheme == t['custom_colors']:
                col1, col2 = st.columns(2)
                with col1:
                    fill_color = st.color_picker(t['qr_color'], "#000000")
                with col2:
                    back_color = st.color_picker(t['bg_color'], "#FFFFFF")
            else:
                fill_color = "#000000"
                back_color = "#FFFFFF"
        
        submitted = st.form_submit_button(t['generate'], type="primary")
    
    # Generate QR code
    if submitted and url:
        try:
            with st.spinner(t['generating']):
                # Create QR code
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                    box_size=box_size,
                    border=border,
                )
                qr.add_data(url)
                qr.make(fit=True)
                
                # Generate image
                img = qr.make_image(fill_color=fill_color, back_color=back_color)
                
                # Convert to bytes
                buf = io.BytesIO()
                img.save(buf, format='PNG')
                buf.seek(0)
                
                # Store in session
                st.session_state.qr_bytes = buf.getvalue()
                st.session_state.qr_content = url
                st.session_state.qr_generated = True
                st.session_state.qr_count += 1
                
                st.success(t['success'])
                
        except Exception as e:
            st.error(f"{t['error']} {str(e)}")
    
    elif submitted and not url:
        st.warning(t['warning'])
    
    # Display QR code
    if st.session_state.qr_generated and st.session_state.qr_bytes:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"### {t['your_qr']}")
            st.image(st.session_state.qr_bytes, use_container_width=True)
            
            with st.expander(t['details']):
                st.code(st.session_state.qr_content[:200])
                st.write(f"**{t['file_size']}** {len(st.session_state.qr_bytes) / 1024:.2f} KB")
                st.write(f"**{t['generation_date']}** {time.strftime('%d/%m/%Y %H:%M')}")
            
            # Download button
            st.download_button(
                label=t['download'],
                data=st.session_state.qr_bytes,
                file_name=f"qrcode_{int(time.time())}.png",
                mime="image/png",
                use_container_width=True
            )
            
            if st.button(t['another'], use_container_width=True):
                st.session_state.qr_generated = False
                st.session_state.qr_bytes = None
                st.rerun()
    
    # Examples section
    with st.expander(t['examples']):
        st.markdown("""
        - **Google Forms**: `https://docs.google.com/forms/...`
        - **Website**: `https://example.com`
        - **Text**: Any message
        - **WiFi**: `WIFI:S:Network;T:WPA;P:Password;;`
        """)
    
    st.markdown("---")
    st.markdown(f"<p style='text-align: center;'>{t['footer']}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
