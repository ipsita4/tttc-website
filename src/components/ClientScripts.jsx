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

    // ── scroll reveal ──
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("visible"); io.unobserve(e.target) } })
    }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" })
    document.querySelectorAll(".fade-up").forEach(el => io.observe(el))

    // stagger grid children
    document.querySelectorAll(".services-grid,.wf-grid,.promo-grid,.pillars,.faq-grid,.why-grid").forEach(grid => {
      grid.querySelectorAll(".fade-up").forEach((el, i) => { el.style.transitionDelay = `${i * 0.08}s` })
    })

    // ── stats counter ──
    const counterObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return
        const el = entry.target
        const sup = el.querySelector("sup")
        const suffix = sup ? sup.textContent : ""
        const target = parseInt(el.textContent.replace(suffix, "").trim())
        if (isNaN(target)) return
        let startTs = null
        const dur = 1800
        const ease = t => 1 - Math.pow(1 - t, 3)
        const tick = ts => {
          if (!startTs) startTs = ts
          const p = Math.min((ts - startTs) / dur, 1)
          el.innerHTML = Math.floor(ease(p) * target) + (suffix ? `<sup>${suffix}</sup>` : "")
          if (p < 1) requestAnimationFrame(tick)
        }
        requestAnimationFrame(tick)
        counterObs.unobserve(el)
      })
    }, { threshold: 0.6 })
    document.querySelectorAll(".stat-num").forEach(el => counterObs.observe(el))

    // contact form
    const cf = document.getElementById("contactForm")
    if (cf) cf.addEventListener("submit", async function(e) {
      e.preventDefault()
      const btn = this.querySelector(".form-submit")
      const orig = btn.innerHTML
      btn.innerHTML = "Sending..."
      btn.disabled = true
      try {
        const res = await fetch("https://api.web3forms.com/submit", {
          method: "POST",
          body: new FormData(this),
        })
        const json = await res.json()
        if (json.success) {
          btn.innerHTML = "✓ Sent!"
          btn.style.background = "#22c55e"
          btn.style.color = "white"
          this.reset()
          setTimeout(() => { btn.innerHTML = orig; btn.style.background = ""; btn.style.color = ""; btn.disabled = false }, 3000)
        } else {
          btn.innerHTML = "Failed — try again"
          btn.style.background = "#ef4444"
          setTimeout(() => { btn.innerHTML = orig; btn.style.background = ""; btn.disabled = false }, 3000)
        }
      } catch {
        btn.innerHTML = "Failed — try again"
        btn.style.background = "#ef4444"
        setTimeout(() => { btn.innerHTML = orig; btn.style.background = ""; btn.disabled = false }, 3000)
      }
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
      io.disconnect()
      counterObs.disconnect()
    }
  }, [])

  return null
}
