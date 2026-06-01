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
          <a href="/plant-setup">RO Plant, ETP &amp; STP Plant</a>
          <a href="/electrical-plant">Complete Electrical Solutions</a>
        </div>
      </li>
      <li><a href="/#projects">Projects</a></li>
      <li><a href="https://api.whatsapp.com/send/?phone=919073409444&text&type=phone_number&app_absent=0" target="_blank" rel="noopener">Contact Us</a></li>
    </ul>

    <a href="/#contact" className="nav-cta">
      <img src="/img/callicon.png" alt="call" style={{width:'17px',height:'17px'}}/>
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
  <a href="/plant-setup" className="mob-sub">RO Plant, ETP &amp; STP Plant</a>
  <a href="/electrical-plant" className="mob-sub">Complete Electrical Solutions</a>
  <a href="/#projects">Projects</a>
  <a href="https://api.whatsapp.com/send/?phone=919073409444&text&type=phone_number&app_absent=0" target="_blank" rel="noopener">Contact Us</a>
  <a href="/#contact" className="mob-cta">Get In Touch</a>
</div>
    </>
  )
}
