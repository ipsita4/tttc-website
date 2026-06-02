"use client"
import { useState } from "react"

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const close = () => setOpen(false)

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
    <button className="hamburger" aria-label="Menu" onClick={() => setOpen(o => !o)}>
      <span style={{transform: open ? 'translateY(7px) rotate(45deg)' : ''}}></span>
      <span style={{opacity: open ? '0' : ''}}></span>
      <span style={{transform: open ? 'translateY(-7px) rotate(-45deg)' : ''}}></span>
    </button>
  </div>
</nav>


<div className={`mob-menu${open ? ' open' : ''}`}>
  <a href="/#home" onClick={close}>Home</a>
  <a href="/#about" onClick={close}>About</a>
  <a href="/#services" style={{fontWeight:'700',color:'var(--orange)'}} onClick={close}>Services</a>
  <a href="/project-management" className="mob-sub" onClick={close}>Hospital Project Management</a>
  <a href="/medical-college" className="mob-sub" onClick={close}>Medical College Projects</a>
  <a href="/pathology-laboratory" className="mob-sub" onClick={close}>Pathology Laboratory</a>
  <a href="/nabh-accreditation" className="mob-sub" onClick={close}>NABH Accreditation</a>
  <a href="/nabl-accreditation" className="mob-sub" onClick={close}>NABL Accreditation</a>
  <a href="/operation-management" className="mob-sub" onClick={close}>Operation Management</a>
  <a href="/website-development" className="mob-sub" onClick={close}>Website Development</a>
  <a href="/digital-marketing" className="mob-sub" onClick={close}>Digital Branding &amp; Marketing</a>
  <a href="/healthcare-stationery" className="mob-sub" onClick={close}>Healthcare Stationery Design</a>
  <a href="/plant-setup" className="mob-sub" onClick={close}>Oxygen Generation Plant</a>
  <a href="/plant-setup" className="mob-sub" onClick={close}>RO Plant, ETP &amp; STP Plant</a>
  <a href="/electrical-plant" className="mob-sub" onClick={close}>Complete Electrical Solutions</a>
  <a href="/#projects" onClick={close}>Projects</a>
  <a href="https://api.whatsapp.com/send/?phone=919073409444&text&type=phone_number&app_absent=0" target="_blank" rel="noopener" onClick={close}>Contact Us</a>
  <a href="/#contact" className="mob-cta" onClick={close}>Get In Touch</a>
</div>
    </>
  )
}
