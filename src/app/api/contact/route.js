import { Resend } from "resend"

export async function POST(req) {
  try {
    const { firstName, lastName, email, phone, company, message } = await req.json()

    const resend = new Resend(process.env.RESEND_API_KEY)

    await resend.emails.send({
      from: "The Team The Consultants <onboarding@resend.dev>",
      to: "info@theteamtheconsultants.com",
      replyTo: email,
      subject: `New Enquiry from ${firstName} ${lastName}`,
      html: `
        <h2>New Website Enquiry</h2>
        <table style="border-collapse:collapse;width:100%;font-family:sans-serif">
          <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold">Name</td><td style="padding:8px;border:1px solid #ddd">${firstName} ${lastName}</td></tr>
          <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold">Email</td><td style="padding:8px;border:1px solid #ddd">${email}</td></tr>
          <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold">Phone</td><td style="padding:8px;border:1px solid #ddd">${phone || "—"}</td></tr>
          <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold">Company</td><td style="padding:8px;border:1px solid #ddd">${company || "—"}</td></tr>
          <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold">Message</td><td style="padding:8px;border:1px solid #ddd">${message || "—"}</td></tr>
        </table>
      `,
    })

    return Response.json({ success: true })
  } catch (err) {
    console.error("Email error:", err)
    return Response.json({ success: false, error: err.message }, { status: 500 })
  }
}
