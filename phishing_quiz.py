import sys
import time

def clear_screen():
    print("\n" + "=" * 65 + "\n")

def run_phishing_training():
    clear_screen()
    print("      🛡️  CodeAlpha Cyber Security Internship - Task 2  🛡️")
    print("               Phishing Awareness Training Module")
    print("=" * 65)
    print("Developed by: Razin Hossain Sagor\n")
    print("Welcome! This interactive module tests your ability to spot")
    print("common phishing indicators, spoofed links, and social engineering.")
    print("-" * 65)
    time.sleep(1)

    questions = [
        {
            "scenario": "Scenario 1: Urgent Account Suspension",
            "email_body": (
                "From: security@paypa1-support.com\n"
                "Subject: URGENT: Your Account Has Been Locked!\n\n"
                "Dear Customer,\n"
                "We detected suspicious activity. Click below within 24 hours\n"
                "or your account will be permanently deleted:\n"
                "http://login.paypal.account-verify-sec.net/update"
            ),
            "is_phishing": True,
            "indicators": [
                "1. Look-alike/spoofed domain (@paypa1-support.com)",
                "2. False sense of urgency (24 hours lock threat)",
                "3. Malicious link path (not paypal.com)",
                "4. Generic greeting ('Dear Customer')"
            ]
        },
        {
            "scenario": "Scenario 2: Password Reset Confirmation",
            "email_body": (
                "From: no-reply@accounts.google.com\n"
                "Subject: Security alert: New sign-in on Windows device\n\n"
                "Hi Razin,\n"
                "A new login was detected on your Google Account from Chrome on Windows.\n"
                "If this was you, you don't need to do anything. If not, check your account activity at:\n"
                "https://myaccount.google.com/notifications"
            ),
            "is_phishing": False,
            "indicators": [
                "1. Legitimate official sender domain (@accounts.google.com)",
                "2. Personalized name used (Razin)",
                "3. Secure HTTPS official domain URL (myaccount.google.com)",
                "4. No threatening tone or demand for immediate credential entry"
            ]
        },
        {
            "scenario": "Scenario 3: Fake HR / Payroll Bonus",
            "email_body": (
                "From: hr-desk@company-internal-portal.info\n"
                "Subject: Q4 Performance Bonus - Review Attached Excel\n\n"
                "Hello Team,\n"
                "Please review the attached macro-enabled spreadsheet 'Bonus_List.xlsm'\n"
                "to confirm your payout. Enable macros when prompted to view sheet."
            ),
            "is_phishing": True,
            "indicators": [
                "1. External unfamiliar domain (.info instead of company domain)",
                "2. Macro-enabled file attachment (.xlsm - common malware dropper)",
                "3. Financial lure prompting security bypass (Enable Macros)",
                "4. Unsolicited attachment"
            ]
        }
    ]

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\n--- {q['scenario']} ---")
        print(q['email_body'])
        print("-" * 65)
        
        while True:
            ans = input("Is this email [P]hishing or [L]egitimate? (Enter P or L): ").strip().upper()
            if ans in ["P", "L"]:
                break
            print("Invalid input! Please enter 'P' for Phishing or 'L' for Legitimate.")

        user_choice_is_phishing = (ans == "P")
        if user_choice_is_phishing == q["is_phishing"]:
            print("✅ CORRECT ANSWER!")
            score += 1
        else:
            print("❌ INCORRECT!")

        print("\n🔍 Key Security Indicators:")
        for indicator in q["indicators"]:
            print(f"   {indicator}")
        print("-" * 65)
        time.sleep(1)

    print("\n" + "=" * 65)
    print(f"Training Complete! Your Awareness Score: {score} / {len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You demonstrated strong awareness against phishing threats.")
    else:
        print("⚠️  Keep practicing! Always verify sender domains and link destinations.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_phishing_training()