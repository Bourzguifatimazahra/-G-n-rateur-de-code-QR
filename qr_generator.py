# Requires: pip install qrcode[pil] pillow streamlit
import qrcode
from PIL import Image
import streamlit as st
import io
import time

# Dictionary for translations
translations = {
    'fr': {
        'title': "📱 Générateur de Code QR",
        'subtitle': "Générez des codes QR pour n'importe quelle URL ou texte - parfait pour partager des liens, formulaires, et plus encore!",
        'url_label': "Entrez l'URL ou le texte à encoder:",
        'url_placeholder': "https://example.com ou n'importe quel texte...",
        'url_help': "Collez n'importe quelle URL ou texte que vous souhaitez convertir en code QR",
        'customization': "🔧 Options de personnalisation",
        'box_size': "Taille des blocs (pixels par bloc):",
        'border': "Bordure (taille de la zone calme):",
        'color_scheme': "Schéma de couleurs:",
        'bw': "Noir & Blanc",
        'custom_colors': "Couleurs personnalisées",
        'qr_color': "Couleur du QR Code:",
        'bg_color': "Couleur d'arrière-plan:",
        'generate': "Générer le Code QR",
        'generating': "Génération du code QR...",
        'success': "✅ Code QR généré avec succès!",
        'error': "❌ Erreur lors de la génération du code QR:",
        'error_info': "💡 Vérifiez que l'URL ou le texte est valide.",
        'warning': "⚠️ Veuillez entrer une URL ou un texte à encoder.",
        'your_qr': "📸 Votre Code QR",
        'details': "📋 Informations détaillées",
        'encoded_content': "Contenu encodé:",
        'file_size': "Taille du fichier:",
        'generation_date': "Date de génération:",
        'download': "📥 Télécharger le Code QR (PNG)",
        'another': "🔄 Générer un autre Code QR",
        'examples': "💡 Exemples et conseils",
        'what_to_encode': "📝 Qu'est-ce que vous pouvez encoder ?",
        'websites': "URLs de sites web",
        'google_forms': "Formulaires Google",
        'text': "Texte",
        'contact': "Informations de contact",
        'wifi': "Identifiants WiFi",
        'tips': "🎯 Conseils pour de meilleurs résultats",
        'high_contrast': "Contraste élevé",
        'optimal_size': "Taille optimale",
        'test': "Testez toujours",
        'avoid_long': "Évitez les URLs trop longues",
        'verify': "Vérifiez la lisibilité",
        'example_google_form': "🔗 Exemple de formulaire Google",
        'copy_url': "💡 Copiez cette URL et collez-la dans le champ ci-dessus pour tester!",
        'footer': "✨ Fabriqué avec ❤️ utilisant Streamlit et QRCode | Version 2.0 ✨",
        'kb': "KB",
        'pixels': "pixels par bloc",
        'quiet_zone': "Bordure blanche autour du code QR",
        'larger_values': "Des valeurs plus grandes créent des codes QR plus grands",
        'choose_scheme': "Choisissez entre standard ou couleurs personnalisées"
    },
    'en': {
        'title': "📱 QR Code Generator",
        'subtitle': "Generate QR codes for any URL or text - perfect for sharing links, forms, and more!",
        'url_label': "Enter URL or text to encode:",
        'url_placeholder': "https://example.com or any text...",
        'url_help': "Paste any URL or text you want to convert to a QR code",
        'customization': "🔧 Customization Options",
        'box_size': "Box Size (pixels per block):",
        'border': "Border (quiet zone size):",
        'color_scheme': "Color Scheme:",
        'bw': "Black & White",
        'custom_colors': "Custom Colors",
        'qr_color': "QR Code Color:",
        'bg_color': "Background Color:",
        'generate': "Generate QR Code",
        'generating': "Generating QR code...",
        'success': "✅ QR Code generated successfully!",
        'error': "❌ Error generating QR code:",
        'error_info': "💡 Please make sure the URL or text is valid.",
        'warning': "⚠️ Please enter a URL or text to encode.",
        'your_qr': "📸 Your QR Code",
        'details': "📋 Detailed Information",
        'encoded_content': "Encoded content:",
        'file_size': "File size:",
        'generation_date': "Generation date:",
        'download': "📥 Download QR Code (PNG)",
        'another': "🔄 Generate Another QR Code",
        'examples': "💡 Examples and Tips",
        'what_to_encode': "📝 What can you encode?",
        'websites': "Website URLs",
        'google_forms': "Google Forms",
        'text': "Text",
        'contact': "Contact information",
        'wifi': "WiFi credentials",
        'tips': "🎯 Tips for best results",
        'high_contrast': "High contrast",
        'optimal_size': "Optimal size",
        'test': "Always test",
        'avoid_long': "Avoid long URLs",
        'verify': "Verify readability",
        'example_google_form': "🔗 Google Form Example",
        'copy_url': "💡 Copy this URL and paste it in the field above to test!",
        'footer': "✨ Made with ❤️ using Streamlit and QRCode | Version 2.0 ✨",
        'kb': "KB",
        'pixels': "pixels per block",
        'quiet_zone': "White border around the QR code",
        'larger_values': "Larger values create bigger QR codes",
        'choose_scheme': "Choose between standard or custom colors"
    },
    'ar': {
        'title': "📱 مولد رمز QR",
        'subtitle': "إنشاء رموز QR لأي عنوان URL أو نص - مثالي لمشاركة الروابط والنماذج والمزيد!",
        'url_label': "أدخل عنوان URL أو النص للتشفير:",
        'url_placeholder': "https://example.com أو أي نص...",
        'url_help': "الصق أي عنوان URL أو نص تريد تحويله إلى رمز QR",
        'customization': "🔧 خيارات التخصيص",
        'box_size': "حجم المربع (بكسل لكل كتلة):",
        'border': "الحدود (حجم المنطقة الهادئة):",
        'color_scheme': "نظام الألوان:",
        'bw': "أسود وأبيض",
        'custom_colors': "ألوان مخصصة",
        'qr_color': "لون رمز QR:",
        'bg_color': "لون الخلفية:",
        'generate': "إنشاء رمز QR",
        'generating': "جاري إنشاء رمز QR...",
        'success': "✅ تم إنشاء رمز QR بنجاح!",
        'error': "❌ خطأ في إنشاء رمز QR:",
        'error_info': "💡 يرجى التأكد من أن عنوان URL أو النص صالح.",
        'warning': "⚠️ يرجى إدخال عنوان URL أو نص للتشفير.",
        'your_qr': "📸 رمز QR الخاص بك",
        'details': "📋 معلومات مفصلة",
        'encoded_content': "المحتوى المشفر:",
        'file_size': "حجم الملف:",
        'generation_date': "تاريخ الإنشاء:",
        'download': "📥 تحميل رمز QR (PNG)",
        'another': "🔄 إنشاء رمز QR آخر",
        'examples': "💡 أمثلة ونصائح",
        'what_to_encode': "📝 ماذا يمكنك تشفير؟",
        'websites': "عناوين URLs المواقع",
        'google_forms': "نماذج Google",
        'text': "نص",
        'contact': "معلومات الاتصال",
        'wifi': "بيانات اعتماد WiFi",
        'tips': "🎯 نصائح للحصول على أفضل النتائج",
        'high_contrast': "تباين عالي",
        'optimal_size': "حجم مثالي",
        'test': "اختبر دائمًا",
        'avoid_long': "تجنب URLs الطويلة",
        'verify': "تحقق من قابلية القراءة",
        'example_google_form': "🔗 مثال على نموذج Google",
        'copy_url': "💡 انسخ هذا URL والصقه في الحقل أعلاه للاختبار!",
        'footer': "✨ تم الصنع بحب باستخدام Streamlit و QRCode | الإصدار 2.0 ✨",
        'kb': "كيلوبايت",
        'pixels': "بكسل لكل كتلة",
        'quiet_zone': "حدود بيضاء حول رمز QR",
        'larger_values': "القيم الأكبر تخلق رموز QR أكبر",
        'choose_scheme': "اختر بين الألوان القياسية أو المخصصة"
    },
    'es': {
        'title': "📱 Generador de Código QR",
        'subtitle': "Genere códigos QR para cualquier URL o texto - ¡perfecto para compartir enlaces, formularios y más!",
        'url_label': "Ingrese URL o texto para codificar:",
        'url_placeholder': "https://example.com o cualquier texto...",
        'url_help': "Pegue cualquier URL o texto que desee convertir en código QR",
        'customization': "🔧 Opciones de personalización",
        'box_size': "Tamaño de bloque (píxeles por bloque):",
        'border': "Borde (tamaño de zona tranquila):",
        'color_scheme': "Esquema de colores:",
        'bw': "Blanco y Negro",
        'custom_colors': "Colores Personalizados",
        'qr_color': "Color del Código QR:",
        'bg_color': "Color de fondo:",
        'generate': "Generar Código QR",
        'generating': "Generando código QR...",
        'success': "✅ ¡Código QR generado con éxito!",
        'error': "❌ Error al generar el código QR:",
        'error_info': "💡 Asegúrese de que la URL o el texto sea válido.",
        'warning': "⚠️ Por favor, ingrese una URL o texto para codificar.",
        'your_qr': "📸 Tu Código QR",
        'details': "📋 Información detallada",
        'encoded_content': "Contenido codificado:",
        'file_size': "Tamaño del archivo:",
        'generation_date': "Fecha de generación:",
        'download': "📥 Descargar Código QR (PNG)",
        'another': "🔄 Generar Otro Código QR",
        'examples': "💡 Ejemplos y Consejos",
        'what_to_encode': "📝 ¿Qué puedes codificar?",
        'websites': "URLs de sitios web",
        'google_forms': "Formularios de Google",
        'text': "Texto",
        'contact': "Información de contacto",
        'wifi': "Credenciales WiFi",
        'tips': "🎯 Consejos para mejores resultados",
        'high_contrast': "Alto contraste",
        'optimal_size': "Tamaño óptimo",
        'test': "Prueba siempre",
        'avoid_long': "Evita URLs largas",
        'verify': "Verifica la legibilidad",
        'example_google_form': "🔗 Ejemplo de Formulario de Google",
        'copy_url': "💡 ¡Copia esta URL y pégala en el campo de arriba para probar!",
        'footer': "✨ Hecho con ❤️ usando Streamlit y QRCode | Versión 2.0 ✨",
        'kb': "KB",
        'pixels': "píxeles por bloque",
        'quiet_zone': "Borde blanco alrededor del código QR",
        'larger_values': "Valores más grandes crean códigos QR más grandes",
        'choose_scheme': "Elige entre colores estándar o personalizados"
    }
}

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
            "Select your language / اختر لغتك / Seleccione su idioma:",
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
        st.info("Generate professional QR codes instantly! Perfect for businesses, events, and personal use.")
        
        st.markdown("### 📊 Statistics")
        if 'qr_count' not in st.session_state:
            st.session_state.qr_count = 0
        st.metric("QR Codes Generated", st.session_state.qr_count)
    
    # Get translations for selected language
    t = translations[language]
    
    # Handle RTL for Arabic
    if language == 'ar':
        st.markdown("""
            <style>
            .stApp {
                direction: rtl;
            }
            .stMarkdown, .stTextInput, .stButton {
                text-align: right;
            }
            </style>
        """, unsafe_allow_html=True)
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .stTextInput > div > div > input {
            font-size: 16px;
        }
        .stButton > button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .qr-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .success-message {
            padding: 10px;
            border-radius: 5px;
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title and description
    st.title(t['title'])
    st.markdown(t['subtitle'])
    st.markdown("---")
    
    # Initialize session state to store QR code
    if 'qr_generated' not in st.session_state:
        st.session_state.qr_generated = False
        st.session_state.qr_image = None
        st.session_state.qr_content = ""
        st.session_state.qr_bytes = None
    
    # Input form
    with st.form("qr_form"):
        url = st.text_input(
            t['url_label'],
            placeholder=t['url_placeholder'],
            help=t['url_help']
        )
        
        # Optional customization
        with st.expander(t['customization']):
            col1, col2 = st.columns(2)
            with col1:
                box_size = st.slider(
                    t['box_size'],
                    min_value=5,
                    max_value=20,
                    value=10,
                    help=t['larger_values']
                )
            with col2:
                border = st.slider(
                    t['border'],
                    min_value=1,
                    max_value=10,
                    value=4,
                    help=t['quiet_zone']
                )
            
            color_scheme = st.selectbox(
                t['color_scheme'],
                [t['bw'], t['custom_colors']],
                help=t['choose_scheme']
            )
            
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
    
    # Generate QR code when form is submitted
    if submitted:
        if url:
            try:
                with st.spinner(t['generating']):
                    # Generate QR code
                    qr = qrcode.QRCode(
                        version=None,
                        error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=box_size,
                        border=border,
                    )
                    qr.add_data(url)
                    qr.make(fit=True)
                    
                    # Create image with custom colors
                    img = qr.make_image(
                        fill_color=fill_color,
                        back_color=back_color
                    )
                    
                    # Convert to bytes immediately
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='PNG', optimize=True)
                    img_byte_arr.seek(0)
                    
                    # Store in session state
                    st.session_state.qr_generated = True
                    st.session_state.qr_image = img
                    st.session_state.qr_content = url
                    st.session_state.qr_bytes = img_byte_arr.getvalue()
                    st.session_state.qr_count += 1
                    
                    # Show success message
                    st.markdown(f'<div class="success-message">{t["success"]}</div>', unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"{t['error']} {str(e)}")
                st.info(t['error_info'])
        else:
            st.warning(t['warning'])
    
    # Display QR code if generated
    if st.session_state.qr_generated and st.session_state.qr_bytes:
        # Create columns for layout
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("---")
            st.markdown(f"### {t['your_qr']}")
            
            # Display QR code
            st.markdown('<div class="qr-container">', unsafe_allow_html=True)
            st.image(st.session_state.qr_bytes, caption=t['your_qr'], use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Information about the QR code
            with st.expander(t['details']):
                st.write(f"**{t['encoded_content']}**")
                st.code(st.session_state.qr_content, language="text")
                st.write(f"**{t['file_size']}** {len(st.session_state.qr_bytes) / 1024:.2f} {t['kb']}")
                st.write(f"**{t['generation_date']}** {time.strftime('%d/%m/%Y %H:%M:%S')}")
            
            # Download button
            col_download1, col_download2, col_download3 = st.columns([1, 2, 1])
            with col_download2:
                st.download_button(
                    label=t['download'],
                    data=st.session_state.qr_bytes,
                    file_name=f"qrcode_{int(time.time())}.png",
                    mime="image/png",
                    use_container_width=True
                )
            
            # Option to create another QR code
            if st.button(t['another'], use_container_width=True):
                st.session_state.qr_generated = False
                st.session_state.qr_image = None
                st.session_state.qr_content = ""
                st.session_state.qr_bytes = None
                st.rerun()
    
    # Example section
    with st.expander(t['examples']):
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            st.markdown(f"### {t['what_to_encode']}")
            st.markdown(f"- **{t['websites']}**: `https://www.example.com`")
            st.markdown(f"- **{t['google_forms']}**: N'importe quel lien de formulaire")
            st.markdown(f"- **{t['text']}**: Messages ou notes")
            st.markdown(f"- **{t['contact']}**: Format vCard")
            st.markdown(f"- **{t['wifi']}**: `WIFI:S:Nom;T:WPA;P:MotDePasse;;`")
        
        with col_ex2:
            st.markdown(f"### {t['tips']}")
            st.markdown(f"- **{t['high_contrast']}**: Couleurs foncées sur fond clair")
            st.markdown(f"- **{t['optimal_size']}**: 10-15 {t['pixels']}")
            st.markdown(f"- **{t['test']}** avant impression")
            st.markdown(f"- **{t['avoid_long']}**")
            st.markdown(f"- **{t['verify']}** avec différents scanners")
        
        st.markdown("---")
        st.markdown(f"### {t['example_google_form']}")
        st.code("https://docs....", language="text")
        st.info(t['copy_url'])
    
    # Footer
    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center; color: gray;'>{t['footer']}</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()