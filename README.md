# 📱 QR Code Generator

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Free](https://img.shields.io/badge/free-100%25-brightgreen.svg)
![Languages](https://img.shields.io/badge/languages-4-orange.svg)

[![Live Demo](https://img.shields.io/badge/demo-live-blue.svg)](https://codeqr.streamlit.app/)
[![Made with Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

</div>

## 🚀 Live Demo

**Try it now:** [https://codeqr.streamlit.app/](https://codeqr.streamlit.app/)

## 🌟 About

A simple, free, and powerful QR code generator. No signup, no ads, no expiration. Generate QR codes instantly for any URL or text.

**Available in:** 🇫🇷 Français | 🇬🇧 English | 🇸🇦 العربية | 🇪🇸 Español

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🆓 **100% Free** | No payment, no subscription ever |
| 🚫 **No Ads** | Clean interface without distractions |
| ⏰ **No Expiration** | QR codes never expire |
| 🌍 **4 Languages** | French, English, Arabic, Spanish |
| 🎨 **Custom Colors** | Choose your QR code colors |
| 📏 **Size Control** | Adjust QR code size from 5-20px |
| 📥 **Easy Download** | Save as PNG instantly |
| 📊 **Statistics** | Track number of generated codes |
| 🔒 **Privacy First** | No data storage, no tracking |

## 🎯 What Can You Generate?

| Type | Example |
|------|---------|
| 🔗 **Website URLs** | `https://example.com` |
| 📝 **Google Forms** | Any form link |
| 📱 **Text Messages** | Any text or note |
| 📞 **Contact Info** | vCard format |
| 📶 **WiFi Credentials** | `WIFI:S:Network;T:WPA;P:Password;;` |
| 🎓 **Educational Links** | Course materials, quizzes |
| 🏢 **Business Links** | Product pages, surveys |

## 🚀 Quick Start

### Online (No installation needed)
Simply visit: [https://codeqr.streamlit.app/](https://codeqr.streamlit.app/)

### Local Installation (Optional)

```bash
# Clone the repository
git clone https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR.git
cd -G-n-rateur-de-code-QR

# Install dependencies
pip install qrcode[pil] streamlit

# Run the app
streamlit run qr_generator.py
```

## 📖 How to Use

1. **Enter** your URL or text in the input field
2. **Customize** colors and size (optional)
3. **Click** "Generate QR Code"
4. **Download** your QR code as PNG file

### Quick Demo
```
Example URL to test:
https://docs.google.com/forms/d/e/1FAIpQLSd8tTc3E1qklY38rSM0cwJuMwRBPfd9VXKo2BYw31IAETOtDg/viewform
```

## 🎨 Customization Options

| Option | Range | Description |
|--------|-------|-------------|
| Box Size | 5-20 px | Size of each QR block |
| Border | 1-10 px | White space around QR |
| QR Color | Any color | Main QR code color |
| Background | Any color | Background color |
| Language | 4 options | FR, EN, AR, ES |

## 💡 Use Cases

### For Business
- 📱 Marketing materials and flyers
- 🏪 Product information pages
- 📋 Customer feedback forms
- 🎉 Event registration
- 💼 Digital business cards

### For Personal
- 📶 Share WiFi credentials
- 📞 Send contact information
- 🌐 Share social media profiles
- 📝 Create digital notes
- 🎁 Gift messages

### For Education
- 📚 Share resources with students
- 📝 Link to online quizzes
- 🎓 Provide quick access to assignments
- 🔗 Course materials and references

## 🔧 Technical Details

### Built With
- **Streamlit** - Web interface framework
- **Python** - Backend logic
- **QRCode library** - QR generation engine
- **Pillow (PIL)** - Image processing

### Requirements
- Python 3.11 or higher
- pip package manager
- Internet connection (for online version)

### File Structure
```
-G-n-rateur-de-code-QR/
├── qr_generator.py      # Main application
├── requirements.txt     # Dependencies
├── runtime.txt         # Python version
├── packages.txt        # System packages
├── README.md           # Documentation
└── .streamlit/         # Streamlit config
    └── config.toml     # App configuration
```

## 🌐 Language Support

| Language | Status | RTL Support |
|----------|--------|-------------|
| 🇫🇷 French | ✅ Full | No |
| 🇬🇧 English | ✅ Full | No |
| 🇸🇦 Arabic | ✅ Full | Yes |
| 🇪🇸 Spanish | ✅ Full | No |

## 📱 Mobile Friendly

Works perfectly on all devices:
- 📱 Smartphones (iOS & Android)
- 💻 Tablets
- 🖥️ Desktop computers
- 📺 Large screens

## 🔒 Privacy & Security

- ✅ **No data storage** - Everything stays on your device
- ✅ **No tracking** - No analytics or monitoring
- ✅ **No registration** - Use immediately
- ✅ **No API calls** - All processing local
- ✅ **Open source** - Code is transparent

## 🎯 Why Choose This Tool?

| Problem | Our Solution |
|---------|--------------|
| Paid QR generators | ✅ **100% Free forever** |
| QR codes with ads | ✅ **No ads at all** |
| Expiring QR codes | ✅ **Never expire** |
| Complex interfaces | ✅ **Simple & clean** |
| Limited languages | ✅ **4 languages** |
| Registration required | ✅ **No signup** |
| Data privacy concerns | ✅ **No data stored** |

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Generation Time | < 1 second |
| File Size | 5-50 KB |
| Max URL Length | 2953 characters |
| Output Format | PNG |
| Max QR Size | 20px per block |
| Error Correction | 15% (M-level) |

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| QR code not scanning | Increase box size or check color contrast |
| File not downloading | Check browser permissions |
| Language not changing | Refresh the page after selection |
| Error generating QR | Verify URL format is correct |
| App not loading | Check internet connection |

## 🚀 Future Updates

- [ ] Dynamic QR codes (updatable content)
- [ ] Batch generation (multiple QR codes)
- [ ] SVG output format
- [ ] QR code analytics
- [ ] Custom logo embedding
- [ ] API endpoints
- [ ] Mobile app version
- [ ] Dark mode support

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Bug fixes
- New features
- Documentation improvements
- Language translations
- UI/UX enhancements

## 📝 License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2026 Bourzgui Fatima zahra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👥 Author

**Bourzgui Fatima zahra**
- GitHub: [@Bourzguifatimazahra](https://github.com/Bourzguifatimazahra)
- Project: [-G-n-rateur-de-code-QR](https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR)
- Live Demo: [codeqr.streamlit.app](https://codeqr.streamlit.app/)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [QRCode](https://github.com/lincolnloop/python-qrcode) - QR generation library
- [Pillow](https://python-pillow.org/) - Image processing library
- All contributors and users of this project

## 📞 Support & Contact

- 🐛 **Report bugs:** [GitHub Issues](https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR/issues)
- 💡 **Feature requests:** [GitHub Discussions](https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR/discussions)
- 📧 **Email:** bourzguifatimazahra@gmail.com
- 🌐 **Live Demo:** [https://codeqr.streamlit.app/](https://codeqr.streamlit.app/)

---

<div align="center">

### ⭐ Show your support

If you find this project useful, please give it a star on GitHub!

**Star this repo** ⭐

---

**Made with ❤️ for the community**

[![GitHub stars](https://img.shields.io/github/stars/Bourzguifatimazahra/-G-n-rateur-de-code-QR?style=social)](https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Bourzguifatimazahra/-G-n-rateur-de-code-QR?style=social)](https://github.com/Bourzguifatimazahra/-G-n-rateur-de-code-QR/network/members)

[![Live Demo](https://img.shields.io/badge/Try%20Now-Live%20Demo-blue?style=for-the-badge)](https://codeqr.streamlit.app/)

</div>
```
 
