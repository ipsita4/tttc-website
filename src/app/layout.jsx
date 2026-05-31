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
        <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,300;1,9..144,600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
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
