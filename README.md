# R Sandeep & Associates - Website

A professional, modern website for R Sandeep & Associates, a Company Secretary and Legal Advisory firm based in Greater Noida, Uttar Pradesh, India.

## Features

- **Professional Design**: Modern, corporate aesthetic with trust-inspiring elements
- **Responsive**: Fully mobile, tablet, and desktop responsive
- **Service Sections**: 6 comprehensive service cards with detailed descriptions
- **Contact Form**: Integrated contact form for client inquiries
- **Social Integration**: WhatsApp and Instagram links
- **Smooth Animations**: Fade-in effects and smooth scrolling
- **Trust Badges**: ICSI Registered, GST Verified, 8+ Years Experience

## Files

- `index.html` - Main website (standalone HTML file with embedded CSS and JavaScript)
- `streamlit_app.py` - Streamlit application to host the website
- `requirements.txt` - Python dependencies

## How to Run

### Option 1: Open HTML Directly
Simply open `index.html` in any modern web browser.

```bash
# On Windows
start index.html

# On macOS
open index.html

# On Linux
xdg-open index.html
```

### Option 2: Run with Streamlit

1. **Install Python** (if not already installed): [Download Python](https://www.python.org/downloads/)

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit App**:
```bash
streamlit run streamlit_app.py
```

4. The app will open in your browser at `http://localhost:8501`

## Deployment Options

### Streamlit Cloud (Free)
1. Push your repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and `streamlit_app.py`
5. Deploy!

### Other Platforms
- **Netlify**: Upload `index.html` directly
- **Vercel**: Deploy as static site
- **GitHub Pages**: Host `index.html` for free
- **Traditional Hosting**: Upload `index.html` to any web server

## Customization

### Colors
Edit the color variables in the `<style>` section of `index.html`:
```css
--primary: #1D8480;      /* Teal */
--navy: #1a1a2e;         /* Dark Navy */
--gold: #d4a017;         /* Gold */
--white: #FFFFFF;        /* White */
```

### Content
All text content, contact information, and social links can be edited directly in the HTML file.

### Contact Information
Update in the HTML:
- Phone: +91-8047654476
- Email: info@rsandeepandassociates.com
- Instagram: @rsandeep_associates
- Address: Greater Noida, Gautam Buddha Nagar, UP

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

© 2025 R Sandeep & Associates. All Rights Reserved.
