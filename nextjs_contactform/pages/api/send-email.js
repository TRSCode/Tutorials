// import sgMail from '@sendgrid/mail';

// export default async function handler(req, res) {
//   if (req.method !== 'POST') {
//     return res.status(405).json({ error: 'Method not allowed' });
//   }

//   sgMail.setApiKey(process.env.SENDGRID_API_KEY);

//   const { name, email, message } = req.body;

//   const content = {
//     to: process.env.TO_EMAIL, // Recipient email
//     from: {
//       name: 'CONTACT REQUEST',
//       email: process.env.FROM_EMAIL, // Verified email
//     },
//     subject: `New contact form submission from ${name}`,
//     // Plain text version
//     text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`,
//     // HTML version
//     html: `<p><strong>Name:</strong> ${name}</p>
//             <p><strong>Email:</strong> <a href="mailto:${email}">${email}</a></p>
//             <p><strong>Message:</strong> ${message}</p>`,
//   };

//   try {
//     await sgMail.send(content);
//     res.status(200).json({ message: 'Email sent successfully' });
//   } catch (error) {
//     console.error(error);
//     if (error.response) {
//       console.error(error.response.body);
//     }
//     res.status(500).json({ error: 'Failed to send email' });
//   }
// }

// pages/api/send-email.js

// pages/api/send-email.js


// ---------2nd attempt works great with capitalized name, date, and 2 recipients


import sgMail from '@sendgrid/mail';

function capitalizeWords(str) {
  return str.toLowerCase().replace(/\b(\w)/g, s => s.toUpperCase());
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  sgMail.setApiKey(process.env.SENDGRID_API_KEY);

  const { name, email, message } = req.body;
  const capitalizedSenderName = capitalizeWords(name);

  // Generate a formatted date string
  const now = new Date();
  const dateString = now.toLocaleString('en-US', { timeZone: 'UTC', dateStyle: 'full', timeStyle: 'long' });

  const content = {
    // Use environment variables to specify recipients
    to: [process.env.TO_EMAIL_A, process.env.TO_EMAIL_B],
    from: {
      name: 'CONTACT REQUEST',
      email: process.env.FROM_EMAIL,
    },
    subject: `New Contact Form: ${capitalizedSenderName}`,
    text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}\nSent on: ${dateString}`,
    html: `<p><strong>Name:</strong> ${name}</p>
            <p><strong>Email:</strong> <a href="mailto:${email}">${email}</a></p>
            <p><strong>Message:</strong> ${message}</p>
            <p><strong>Sent on:</strong> ${dateString}</p>`,
  };

  try {
    await sgMail.send(content);
    res.status(200).json({ message: 'Email sent successfully' });
  } catch (error) {
    console.error(error);
    if (error.response) {
      console.error(error.response.body);
    }
    res.status(500).json({ error: 'Failed to send email' });
  }
}

