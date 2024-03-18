// pages/api/send-email.js
import sgMail from '@sendgrid/mail';

sgMail.setApiKey(process.env.SENDGRID_API_KEY); // Ensure this is set in your .env.local

export default async function (req, res) {
  const { email, name, message } = req.body;
  
  const content = {
    to: 'your-email@example.com', // The destination email address
    from: 'your-verified-sendgrid-email@example.com', // Your verified SendGrid email
    subject: `New Contact Form Submission from ${name}`,
    text: message,
    html: `<p>${message}</p>`,
  };

  try {
    await sgMail.send(content);
    res.status(200).json({ message: 'Email sent successfully' });
  } catch (error) {
    console.error('Error sending email:', error);
    res.status(500).json({ error: 'Error sending email' });
  }
}
