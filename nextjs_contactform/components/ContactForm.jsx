'use client';

// components/ContactForm.jsx
export default function ContactForm() {
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    
    // Call your API route to send the data to SendGrid
    const res = await fetch('/api/send-email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    
    // Handle response...
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block">Name</label>
        <input type="text" name="name" id="name" required className="w-full px-3 py-2 border"/>
      </div>
      <div>
        <label htmlFor="email" className="block">Email</label>
        <input type="email" name="email" id="email" required className="w-full px-3 py-2 border"/>
      </div>
      <div>
        <label htmlFor="message" className="block">Message</label>
        <textarea name="message" id="message" rows="4" required className="w-full px-3 py-2 border"></textarea>
      </div>
      <button type="submit" className="px-4 py-2 bg-blue-500 text-white">Send</button>
    </form>
  );
}
