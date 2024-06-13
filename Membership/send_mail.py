from django.core.mail import send_mail, EmailMessage


send_mail(
    "Test Mail",
    "Hi, Chisom, here is the message.",
    "from@example.com",
    ["marcusjobng@gmail.com"],
    fail_silently=False,
)
