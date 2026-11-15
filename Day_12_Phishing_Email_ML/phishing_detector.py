import csv
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# 1 = Phishing, 0 = Legitimate

phishing_emails = [
    "Verify your account immediately or it will be suspended",
    "Click here to claim your free prize today",
    "Urgent update your bank details to avoid account closure",
    "Your password has expired click this link to reset it",
    "Congratulations you have won a cash reward claim now",
    "Unusual login detected verify your identity immediately",
    "Your account is locked submit your credentials to unlock it",
    "Payment failed update your card information now",
    "Act now your account will be permanently deleted",
    "Confirm your banking password to prevent suspension",
    "You have received a refund click to collect it",
    "Your mailbox is full login here to increase storage",
    "Security alert verify your account through this link",
    "Your package is waiting pay the delivery fee now",
    "Claim your exclusive gift by entering your details",
    "Your tax refund is ready provide bank information",
    "Immediate action required confirm your login details",
    "Your account access is limited verify your password",
    "Click the attachment to receive your prize money",
    "Update your payment details to avoid service termination",
    "Your email account needs urgent security verification",
    "You are selected for a reward submit personal details",
    "Suspicious activity found sign in to secure your account",
    "Your subscription will end today renew using this link",
    "Confirm your identity now to receive your bank refund"
]

legitimate_emails = [
    "The team meeting is scheduled for Monday at ten",
    "Please review the attached quarterly project report",
    "Your appointment is confirmed for tomorrow afternoon",
    "The office will remain closed during the public holiday",
    "Here are the notes from yesterday's team discussion",
    "The monthly sales report is ready for review",
    "Please submit your project update by Friday",
    "The training session begins at nine in the conference room",
    "Your invoice for the previous month is attached",
    "The development team fixed the reported software issue",
    "Lunch with the department is planned for Thursday",
    "Please find the revised presentation attached",
    "The maintenance schedule has been updated",
    "Your registration for the workshop is confirmed",
    "The weekly newsletter is available on the company portal",
    "The project deadline has been moved to next week",
    "Please review the meeting agenda before the call",
    "Your order has been shipped and is on its way",
    "The library will close early this evening",
    "The HR team shared the updated leave policy",
    "Your course completion certificate is ready",
    "The server maintenance is scheduled for Sunday",
    "Please confirm your availability for the team meeting",
    "The annual performance review starts next month",
    "Attached is the final copy of the project proposal"
]

# 1. Create a balanced 50-email dataset
emails = phishing_emails + legitimate_emails
labels = [1] * 25 + [0] * 25

with open("emails_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["email_text", "label"])
    writer.writerows(zip(emails, labels))

print("[+] Dataset created: 50 emails")
print(f"1    {labels.count(1)}\n0    {labels.count(0)}")

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

# 3. Build Naive Bayes machine-learning pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# 4. Train the model
model.fit(X_train, y_train)

# 5. Predict test emails
predictions = model.predict(X_test)

# 6. Evaluate model
accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions, labels=[0, 1])

report = classification_report(
    y_test,
    predictions,
    labels=[0, 1],
    target_names=["LEGITIMATE", "PHISHING"],
    zero_division=0
)

print("\n" + "=" * 50)
print("       PHISHING EMAIL DETECTION - ML")
print("=" * 50)

print(f"\nDataset size: {len(emails)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

print("\nCONFUSION MATRIX")
print("Rows = Actual | Columns = Predicted")
print("                 LEGIT  PHISHING")
print(f"LEGITIMATE       {matrix[0][0]:5}  {matrix[0][1]:5}")
print(f"PHISHING         {matrix[1][0]:5}  {matrix[1][1]:5}")

print(f"\nAccuracy: {accuracy * 100:.2f}%")
print("\nCLASSIFICATION REPORT")
print(report)

# 7. Save trained model
joblib.dump(model, "phishing_model.pkl")

# 8. Test new sample emails
test_emails = [
    "Urgent verify your bank password immediately",
    "The team meeting starts at three tomorrow",
    "Claim your reward now by clicking this link",
    "Please review the project report before Friday"
]

print("\nNEW EMAIL PREDICTIONS")

for email in test_emails:
    prediction = model.predict([email])[0]
    result = "PHISHING" if prediction == 1 else "LEGITIMATE"
    print(f"{result}: {email}")

# 9. Save results
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("DAY 12 - PHISHING EMAIL DETECTION WITH ML\n\n")
    file.write(f"Dataset size: {len(emails)}\n")
    file.write(f"Training samples: {len(X_train)}\n")
    file.write(f"Testing samples: {len(X_test)}\n")
    file.write(f"Accuracy: {accuracy * 100:.2f}%\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(matrix))
    file.write("\n\nClassification Report:\n")
    file.write(report)

print("\n[+] Dataset saved to emails_dataset.csv")
print("[+] Model saved to phishing_model.pkl")
print("[+] Results saved to output.txt")
print("[+] SCAN COMPLETED")
