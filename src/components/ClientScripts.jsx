"use client"
import { useEffect } from "react"

export default function ClientScripts() {
  useEffect(() => {
    // navbar scroll
    const nb = document.getElementById("navbar")
    const onScroll = () => nb?.classList.toggle("scrolled", window.scrollY > 20)
    window.addEventListener("scroll", onScroll, { passive: true })

    // hamburger
    const hb = document.getElementById("hamburger")
    const mm = document.getElementById("mobMenu")
    const toggleMenu = () => {
      const o = mm?.classList.toggle("open")
      const sp = hb?.querySelectorAll("span")
      if (sp) {
        sp[0].style.transform = o ? "translateY(7px) rotate(45deg)" : ""
        sp[1].style.opacity   = o ? "0" : ""
        sp[2].style.transform = o ? "translateY(-7px) rotate(-45deg)" : ""
      }
    }
    hb?.addEventListener("click", toggleMenu)
    mm?.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
      mm.classList.remove("open")
      hb?.querySelectorAll("span").forEach(s => { s.style.transform = ""; s.style.opacity = "" })
    }))

    // scroll-to-top
    const st = document.getElementById("scrollTop")
    const onScrollTop = () => st?.classList.toggle("visible", window.scrollY > 400)
    window.addEventListener("scroll", onScrollTop, { passive: true })
    st?.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }))

    // FAQ accordion
    document.querySelectorAll(".faq-q").forEach(q => {
      q.addEventListener("click", () => {
        const item = q.parentElement
        document.querySelectorAll(".faq-item").forEach(i => { if (i !== item) i.classList.remove("open") })
        item.classList.toggle("open")
      })
    })

    // contact form
    const cf = document.getElementById("contactForm")
    if (cf) cf.addEventListener("submit", function(e) {
      e.preventDefault()
      const btn = this.querySelector(".form-submit")
      const orig = btn.innerHTML
      btn.innerHTML = "✓ Sent!"
      btn.style.background = "#22c55e"
      setTimeout(() => { btn.innerHTML = orig; btn.style.background = ""; this.reset() }, 3000)
    })

    // video player
    const overlay = document.getElementById("playOverlay")
    const vid = document.getElementById("heroVideo")
    if (vid && overlay) {
      overlay.addEventListener("click", () => { vid.play(); overlay.style.display = "none" })
      vid.addEventListener("pause", () => { overlay.style.display = "flex" })
      vid.addEventListener("ended", () => { overlay.style.display = "flex"; vid.currentTime = 0 })
    }

    return () => {
      window.removeEventListener("scroll", onScroll)
      window.removeEventListener("scroll", onScrollTop)
    }
  }, [])

  return null
}
