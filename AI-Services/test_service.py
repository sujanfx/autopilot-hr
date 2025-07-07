import requests
import json
import sys
import os

BASE_URL = "http://localhost:8000"

def test_health():
    """Test API health"""
    print("🏥 Testing API health...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   OpenAI: {data.get('openai_connection', 'unknown')}")
        return response.status_code == 200
    except Exception as e:
        print(f"   Error: {e}")
        return False

def test_resume_parsing():
    """Test resume parsing"""
    print("\n📄 Testing resume parsing...")

    sample_resume = """
    John Smith
    Software Engineer
    john.smith@email.com | (555) 123-4567
    San Francisco, CA

    EXPERIENCE
    Senior Developer at TechCorp (2020-2024)
    - Built scalable web applications using Python and React
    - Led team of 3 developers
    - Implemented CI/CD pipelines with Docker

    Software Engineer at StartupXYZ (2018-2020)
    - Developed REST APIs using Django and PostgreSQL
    - Reduced application load time by 40%

    EDUCATION
    Bachelor of Science in Computer Science
    University of California, Berkeley (2014-2018)

    SKILLS
    Programming: Python, JavaScript, Java, TypeScript
    Frameworks: React, Django, Node.js
    Cloud: AWS, Docker, Kubernetes
    Databases: PostgreSQL, MongoDB
    """

    try:
        payload = {"text": sample_resume}
        response = requests.post(f"{BASE_URL}/parse-resume", json=payload, timeout=30)

        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            message = response.json()
            print("   GPT-4 Response:")
            print(message)
            return True
        else:
            print(f"   Error: {response.text}")
            return False
    except Exception as e:
        print(f"   Error: {e}")
        return False

def main():
    """Run basic API test suite"""
    print("🚀 AutoPilot HR API Test Suite - Windows Edition")
    print("=" * 60)

    # Check if virtual environment is activated
    if not os.environ.get('VIRTUAL_ENV'):
        print("⚠  Warning: Virtual environment not detected!")
        print("   Make sure to activate: autopilot_env\\Scripts\\activate")
        print()

    # Test 1: Health check
    if not test_health():
        print("\n❌ Health check failed! Make sure the API is running.")
        input("Press Enter to exit...")
        sys.exit(1)

    # Test 2: Resume parsing
    if not test_resume_parsing():
        print("\n❌ Resume parsing failed!")
        input("Press Enter to exit...")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ All tests passed! API is ready for UiPath integration.")
    print("📡 API Documentation: http://localhost:8000/docs")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
