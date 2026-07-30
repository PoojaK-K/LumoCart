# 🛍️ LumoCart

> **A modern Streamlit-based e-commerce application with OTP authentication, shopping cart, wishlist, and an elegant dark-themed user interface.**

---

## 📖 Overview

LumoCart is a lightweight e-commerce web application built using **Python** and **Streamlit**. It provides users with a simple and interactive online shopping experience, including user authentication, product browsing, search functionality, cart management, wishlist support, and order checkout.

The application demonstrates the implementation of core e-commerce concepts while maintaining a clean, responsive, and visually appealing interface.

---

## ✨ Features

### 🔐 User Authentication

* User Login
* New User Registration
* Email OTP Verification
* Secure OTP generation

### 🛍️ Shopping Experience

* Browse multiple product categories
* Product search
* Product ratings
* Responsive product cards
* Attractive dark-themed interface

### ❤️ Wishlist

* Add products to wishlist
* Remove products from wishlist
* View saved items anytime

### 🛒 Shopping Cart

* Add items to cart
* Remove products
* View cart contents
* Checkout process

### 🎨 User Interface

* Modern dark gradient design
* Responsive layout
* Interactive buttons
* Toast notifications
* Balloons animation after successful order

---

## 📂 Product Categories

* 👔 Men Wear
* 👗 Women Wear
* 💍 Jewelry
* 💻 Gadgets

---

## 🛠️ Tech Stack

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Programming Language                |
| Streamlit    | Web Application Framework           |
| HTML/CSS     | UI Styling                          |
| SMTP (Gmail) | Email OTP Verification              |
| Pyngrok      | Public Deployment from Google Colab |
| Google Colab | Cloud Development Environment       |

---

## 📸 Application Workflow

```text
Login
   │
   ▼
Register (New Users)
   │
   ▼
Email OTP Verification
   │
   ▼
Home Categories
   │
   ▼
Browse Products
   │
   ├── Search Products
   ├── Add to Cart
   └── Add to Wishlist
   │
   ▼
Shopping Cart
   │
   ▼
Checkout
   │
   ▼
Order Successfully Placed
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/PoojaK-K/LumoCart.git
```

Move into the project directory

```bash
cd LumoCart
```

Install dependencies

```bash
pip install streamlit pyngrok
```

Run the application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
LumoCart/
│
├── app.py
├── LumoCart.ipynb
├── README.md
└── assets/
```

---

## 🌟 Highlights

* Clean and modern UI
* Email OTP verification
* Product search
* Shopping cart management
* Wishlist functionality
* Category-wise shopping
* Interactive checkout flow
* Lightweight and beginner-friendly architecture

---

## 🔮 Future Enhancements

* User database integration
* Secure password hashing
* Admin dashboard
* Product inventory management
* Payment gateway integration
* Order history
* Product recommendations
* Discount coupons
* User profile management
* Product reviews and comments
* Database support (MySQL/PostgreSQL)
* FastAPI backend integration

---

## 📚 Learning Outcomes

This project helped in understanding:

* Streamlit application development
* State management using `st.session_state`
* Email authentication using SMTP
* Dynamic UI rendering
* Search functionality
* Shopping cart implementation
* Wishlist management
* Python web application deployment using ngrok

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👩‍💻 Author

**Pooja K K**

* GitHub: https://github.com/PoojaK-K
* LinkedIn: https://www.linkedin.com/in/poojak-k/

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub!

It motivates future improvements and helps others discover the project.
