import google.generativeai as genai

# Your API Key
GOOGLE_API_KEY = "AIzaSyAcV_wcdsFZjYwhMXZ-h3qq5PjmNDgt3mA"
genai.configure(api_key=GOOGLE_API_KEY)

print("🔎 Checking available models for your key...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Found: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")