import "./globals.css"
import Navbar from "@/components/Navbar"
import Footer from "@/components/Footer"
import CTASection from "@/components/CTASection"
import ClientScripts from "@/components/ClientScripts"

export const metadata = {
  title: "The Team The Consultants | Healthcare Operation Management",
  description: "End-to-end Healthcare Project Management, NABH/NABL Accreditation, Operational Management and more.",
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous"/>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,600&display=swap" rel="stylesheet"/>
      </head>
      <body>
        <Navbar/>
        <main>{children}</main>
        <CTASection/>
        <Footer/>
        <ClientScripts/>
      </body>
    </html>
  )
}
