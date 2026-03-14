import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText

# --- CONFIG & STYLING ---
st.set_page_config(page_title="LumoCart Global", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d0d0d 0%, #1a1a2e 100%); }
    h1, h2, h3, h4, p, label, span, .stMarkdown { color: #ffffff !important; }
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px; border-radius: 15px; border: 1px solid #c19ee0;
        height: 520px; display: flex; flex-direction: column; justify-content: space-between;
        margin-bottom: 20px;
    }
    .img-box { width: 100%; height: 240px; object-fit: cover; border-radius: 10px; background-color: #222; }
    .stButton > button { background-color: #c19ee0 !important; color: #121212 !important; font-weight: bold; border-radius: 8px; width: 100%; }
    .stTextInput > div > div > input { background-color: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid #c19ee0 !important; }
    </style>
""", unsafe_allow_html=True)

# --- OTP LOGIC ---
def send_otp_email(receiver_email, otp):
    sender_email = "policynavinfo@gmail.com"
    sender_password = "olbj ksit ozpt nbun"
    try:
        msg = MIMEText(f"Your LumoCart OTP is: {otp}")
        msg["Subject"] = "LumoCart Verification"; msg["From"] = sender_email; msg["To"] = receiver_email
        server = smtplib.SMTP("smtp.gmail.com", 587); server.starttls()
        server.login(sender_email, sender_password); server.send_message(msg); server.quit()
        return True
    except: return False

# --- DATA WITH RATINGS ---
PRODUCTS = {
    "men": [
        {"id": 1, "name": "Oxford Cotton Shirt", "price": 1200, "rating": 4.5, "img": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500"},
        {"id": 2, "name": "Slim Fit Suit", "price": 6500, "rating": 4.8, "img": "https://images.pexels.com/photos/1321943/pexels-photo-1321943.jpeg?w=500"},
        {"id": 3, "name": "Denim Jacket", "price": 2500, "rating": 4.2, "img": "https://images.unsplash.com/photo-1551537482-f2075a1d41f2?w=500"}
    ],
    "women": [
        {"id": 4, "name": "Pure Silk Saree", "price": 4500, "rating": 4.9, "img": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=500"},
        {"id": 5, "name": "Designer Lehenga", "price": 8500, "rating": 4.7, "img": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=500"},
        {"id": 6, "name": "Western Party Gown", "price": 3200, "rating": 4.6, "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=500"}
    ],
    "jewelry": [
        {"id": 7, "name": "Necklace Set", "price": 3000, "rating": 4.4, "img": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400"},
        {"id": 8, "name": "Watch", "price": 12000, "rating": 4.9, "img": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=400"}
    ],
    "gadgets": [
        {"id": 9, "name": "Professional Laptop", "price": 75000, "rating": 4.8, "img": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},
        {"id": 10, "name": "Headphones", "price": 2800, "rating": 4.3, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"}
    ]
}

# --- STATE ---
for key in ["page", "user", "cart", "wishlist", "otp", "category"]:
    if key not in st.session_state: st.session_state[key] = [] if key in ["cart", "wishlist"] else None

def go(p): st.session_state.page = p; st.rerun()

# --- SIDEBAR ---
def sidebar():
    with st.sidebar:
        st.title("LumoCart 🌙")
        if st.session_state.user:
            st.write(f"Logged in:{st.session_state.user}")
            if st.button("🏠 Home"): go("categories")
            if st.button(f"🛒 Cart ({len(st.session_state.cart)})"): go("cart")
            if st.button(f"❤️ Wishlist ({len(st.session_state.wishlist)})"): go("wishlist")
            st.divider()
            if st.button("Logout"): st.session_state.user = None; go("login")

# --- PAGES ---
if st.session_state.page == "login" or st.session_state.page is None:
    st.title("LumoCart Login")
    u = st.text_input("Username"); p = st.text_input("Password", type="password")
    if st.button("Login"): st.session_state.user = u; go("categories")
    st.button("New User? Register", on_click=lambda: go("register"))

elif st.session_state.page == "register":
    st.title("Register")
    email = st.text_input("Email")
    if st.button("Send OTP"):
        otp = str(random.randint(1000, 9999))
        if send_otp_email(email, otp): st.session_state.otp = otp; go("otp_verify")

elif st.session_state.page == "otp_verify":
    code = st.text_input("Enter OTP")
    if st.button("Verify"):
        if code == st.session_state.otp: go("login")
        else: st.error("Wrong OTP")

elif st.session_state.page == "categories":
    sidebar(); st.header("Shop Categories")
    cols = st.columns(4)
    cats = [("Men Wear", "men", "https://images.unsplash.com/photo-1488161628813-04466f872be2?w=400"),
            ("Women Wear", "women", "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400"),
            ("Jewelry", "jewelry", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=400"),
            ("Gadgets", "gadgets", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8")]
    for i, (n, k, img) in enumerate(cats):
        with cols[i]:
            st.markdown(f'<img src="{img}" class="img-box">', unsafe_allow_html=True)
            if st.button(n, key=k): st.session_state.category = k; go("products")

elif st.session_state.page == "products":
    sidebar(); st.header(f"Browsing {st.session_state.category.title()}")
    
    # SEARCH BAR LOGIC
    search_query = st.text_input("🔍 Search products...", "").lower()
    items = [i for i in PRODUCTS[st.session_state.category] if search_query in i['name'].lower()]
    
    if not items:
        st.warning("No items found.")
    else:
        cols = st.columns(3)
        for i, p in enumerate(items):
            with cols[i % 3]:
                st.markdown(f'''
                    <div class="main-card">
                        <img src="{p["img"]}" class="img-box">
                        <h4>{p["name"]}</h4>
                        <p style="font-weight: bold; margin:0;">₹{p["price"]:,}</p>
                        <p style="color: #FFD700; font-weight: bold;">{p['rating']} ⭐</p>
                    </div>
                ''', unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                if c1.button("🛒 Add", key=f"a{p['id']}"): 
                    st.session_state.cart.append(p); st.toast("Added!")
                if c2.button("❤️ Wish", key=f"w{p['id']}"): 
                    st.session_state.wishlist.append(p); st.toast("Saved!")

elif st.session_state.page == "cart":
    sidebar(); st.header("🛒 My Cart")
    if not st.session_state.cart: st.info("Empty")
    else:
        for idx, item in enumerate(st.session_state.cart):
            col_a, col_b = st.columns([5, 1])
            col_a.write(f"🛍️ {item['name']} - ₹{item['price']:,}")
            if col_b.button("❌", key=f"rc_{idx}"): st.session_state.cart.pop(idx); st.rerun()
        if st.button("Checkout"): go("checkout")

elif st.session_state.page == "wishlist":
    sidebar(); st.header("❤️ Wishlist")
    if not st.session_state.wishlist: st.info("Empty")
    else:
        for idx, item in enumerate(st.session_state.wishlist):
            col_a, col_b = st.columns([5, 1])
            col_a.write(f"✨ {item['name']}")
            if col_b.button("❌", key=f"rw_{idx}"): st.session_state.wishlist.pop(idx); st.rerun()

elif st.session_state.page == "checkout":
    sidebar(); st.header("Checkout")
    with st.form("f"):
        st.text_input("Address")
        if st.form_submit_button("Place Order"):
            st.balloons(); st.session_state.cart = []; st.success("Ordered!"); st.button("Home", on_click=lambda: go("categories"))
