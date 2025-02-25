import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="✪")

# App title
st.title("Growth Mindset Challenge App:")

# Welcome message
st.header("💫 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This 🤖 AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🚀")

# Growth Mindset Quote
st.header("📖 Today's Growth Mindset Quote")
st.write("📢 *Success is not final, failure is not fatal: it is the courage to continue that counts.* - _Winston Churchill_ 💡")

# Challenge Input
st.header("🤔 What's Your Challenge Today?")
user_input = st.text_input("📝 Describe a challenge you're facing:", "")

# Display user challenge
if user_input:
    st.success(f"🎯 You're facing: {user_input}. Keep moving ahead toward your goal! 💪")
else:
    st.warning("⚠️ Tell us about your challenge to get started!")

# Reflection Section
st.header("🔍 Reflect On Your Learning")  
reflection = st.text_area("💭 Write your reflections here:", "")

# Display user reflection
if reflection:
    st.success(f"🌟 Great Insight! Your reflection: {reflection}")
else:
    st.info("📌 Reflecting on past experiences helps you grow! Share your challenges.")

# Celebrate Wins
st.header("🎉 Celebrate Your Wins!")
achievement = st.text_input("🏆 Share something you've recently accomplished:", "")  

# Display user achievement
if achievement:
    st.success(f"👏 Amazing! You achieved: {achievement} 🎊")
else:
    st.info("💖 Big or small, every achievement counts! Share one now!")

st.markdown("---")

# Final motivation message
st.write("🌱 Keep trusting yourself. Growth is a journey, not a destination! ✨")

# Footer
st.write("🌟 **Created by Muhammad Nafees 🚀💡 Keep shining!** ✨")
