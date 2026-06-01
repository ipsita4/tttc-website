"use client"
export default function Navbar() {
  return (
    <>
      <nav className="navbar" id="navbar">
  <div className="nav-inner">
    <a href="/" className="nav-logo">
      <img src="/img/logo.png" alt="The Team The Consultants" className="nav-logo-img"/>
    </a>

    <ul className="nav-links">
      <li><a href="/#home" className="active">Home</a></li>
      <li><a href="/#about">About</a></li>
      <li>
                <a href="/#services">Services <svg className="arr" viewBox="0 0 16 16"><polyline points="4,6 8,10 12,6"/></svg></a>
        <div className="dropdown">
          <a href="/project-management">Hospital Project Management</a>
          <a href="/medical-college">Medical College Projects</a>
          <a href="/pathology-laboratory">Pathology Laboratory</a>
          <a href="/nabh-accreditation">NABH Accreditation</a>
          <a href="/nabl-accreditation">NABL Accreditation</a>
          <a href="/operation-management">Operation Management</a>
          <a href="/website-development">Website Development</a>
          <a href="/digital-marketing">Digital Branding &amp; Marketing</a>
          <a href="/healthcare-stationery">Healthcare Stationery Design</a>
          <a href="/plant-setup">Oxygen Generation Plant</a>
        </div>
      </li>
      <li><a href="/#projects">Projects</a></li>
      <li><a href="/#contact">Contact Us</a></li>
    </ul>

    <a href="/#contact" className="nav-cta">
      <svg viewBox="0 0 24 24" fill="none"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.7 10.74 19.79 19.79 0 01.67 2.18 2 2 0 012.67.06h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/></svg>
      Get In Touch
    </a>
    <button className="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>


<div className="mob-menu" id="mobMenu">
  <a href="/#home">Home</a>
  <a href="/#about">About</a>
    <a href="/#services" style={{fontWeight:'700',color:'var(--orange)'}}>Services</a>
  <a href="/project-management" className="mob-sub">Hospital Project Management</a>
  <a href="/medical-college" className="mob-sub">Medical College Projects</a>
  <a href="/pathology-laboratory" className="mob-sub">Pathology Laboratory</a>
  <a href="/nabh-accreditation" className="mob-sub">NABH Accreditation</a>
  <a href="/nabl-accreditation" className="mob-sub">NABL Accreditation</a>
  <a href="/operation-management" className="mob-sub">Operation Management</a>
  <a href="/website-development" className="mob-sub">Website Development</a>
  <a href="/digital-marketing" className="mob-sub">Digital Branding &amp; Marketing</a>
  <a href="/healthcare-stationery" className="mob-sub">Healthcare Stationery Design</a>
  <a href="/plant-setup" className="mob-sub">Oxygen Generation Plant</a>
  <a href="/#projects">Projects</a>
  <a href="/#contact">Contact Us</a>
  <a href="/#contact" className="mob-cta">Get In Touch</a>
</div>
    </>
  )
}
