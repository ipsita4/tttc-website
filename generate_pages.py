import os

BASE = "/Users/ipsita/Documents/untitled folder/the-team-the-consultants-website"

SERVICES = [
  {
    "file": "project-management.html",
    "title": "Hospital & Health Care Project Management",
    "subtitle": "One Stop Solution for Hospital or any kind of Health Care Set Up",
    "icon_color": "#E85D04",
    "nav_label": "Project Management",
    "intro": "We provide end-to-end Hospital and Health Care Project Management services — from architectural planning to final handover. Our highly experienced team ensures every aspect of your healthcare facility is executed flawlessly and on time.",
    "items": [
      {"num":"01","title":"Planning, Drawing & Designing","desc":"Architectural, Civil, Structural, Mechanical, Electrical, Plumbing, Fire Safety, Medical Gas Pipeline."},
      {"num":"02","title":"Compliance & Regulations","desc":"As per National Building Code, NABH Rules and functionality abiding rules and regulations including environment impact assessment / green building rating."},
      {"num":"03","title":"Construction BOQ","desc":"Providing BOQ of all Construction Materials including Estimates."},
      {"num":"04","title":"Furniture & Equipment BOQ","desc":"Providing BOQ of all Hospital Furniture & Medical Equipment."},
      {"num":"05","title":"Project Execution Consultancy","desc":"Total Hospital or Health Care Project Execution Consultancy (if required)."},
      {"num":"06","title":"Technical Supervision","desc":"Technical periodic supervision and evaluation of construction work."},
      {"num":"07","title":"Vendor Selection Support","desc":"Helping the client choosing the vendors for specialized work (if required)."},
      {"num":"08","title":"Coordinated Drawings","desc":"Total liaison with other service consultants for preparation of coordinated drawings."},
      {"num":"09","title":"Licensing & Accreditation","desc":"Taking care of Total Hospital and Health Care Project Licensing and Accreditation Process (if required)."},
      {"num":"10","title":"End-to-End Project Management","desc":"Complete guidance and support from concept to commissioning, ensuring timely and flawless implementation."},
    ]
  },
  {
    "file": "medical-college.html",
    "title": "Medical College Hospital Design & Development",
    "subtitle": "Transforming Healthcare Education with Premier Infrastructure",
    "nav_label": "Medical College",
    "intro": "A Medical College Hospital represents an essential infrastructure initiative designed to deliver high-quality medical education, facilitate research opportunities, and offer comprehensive healthcare services. At 'THE TEAM THE CONSULTANTS,' we specialize in navigating the complexities of planning, designing, and implementing premier Medical College Hospitals across India. Our expertise spans systematic space planning, aesthetically functional architectural design, and MEP solutions, all aligned with the guidelines set by the National Medical Commission, the National Building Act, and Environmental Clearance requirements. Together, let's shape the future of medical education!",
    "items": [
      {"num":"01","title":"Medical College & Hospital Planning","desc":"Systematic space planning for education & healthcare, ensuring optimal utilization of every area for clinical training and patient care."},
      {"num":"02","title":"Architectural & MEP Design","desc":"Functional, aesthetically pleasing layouts with efficient Mechanical, Electrical, and Plumbing (MEP) engineering solutions."},
      {"num":"03","title":"Regulatory Compliance","desc":"Designs fully aligned with National Medical Commission guidelines, National Building Act, and Environmental Clearance norms."},
      {"num":"04","title":"Project Management & Execution","desc":"End-to-end solutions ensuring timely and flawless implementation from concept to commissioning of the medical college hospital."},
    ]
  },
  {
    "file": "operation-management.html",
    "title": "Hospital & Health Care Operational Management",
    "subtitle": "Streamline Your Operations with Expert Management",
    "nav_label": "Operation Management",
    "intro": "We are ready to help you and your organization with Highly Experienced Management Staff, to put everything in the streamline of your Hospital OR Health Care Day to Day Operational Management systems as per NABH Guidelines.",
    "items": [
      {"num":"01","title":"Organizational Audit & GAP Analysis","desc":"Conduct an audit of the organization and analyse GAP — identifying areas for improvement and growth opportunities."},
      {"num":"02","title":"Data Analysis & Interpretation","desc":"Analyse and interpret data, understanding the impact of data on an organization's operations and strategic decisions."},
      {"num":"03","title":"Systems & Process Recommendations","desc":"Make recommendations for new systems, practices and procedures to be implemented for better efficiency."},
      {"num":"04","title":"CRM & Account Management","desc":"Update models, accounts and CRM systems to enable smooth running of the business and better customer relations."},
      {"num":"05","title":"Supply Chain Optimization","desc":"Optimize supply chain logistics to reduce costs, improve efficiency and ensure timely delivery of supplies."},
      {"num":"06","title":"Organizational Restructuring","desc":"Suggest changes to improve the overall structure of the business and examine employee job roles for better alignment."},
      {"num":"07","title":"Supplier Relationship Management","desc":"Analyse relationships between businesses and suppliers/manufacturers and negotiate improved contractual terms."},
      {"num":"08","title":"Financial Process Updates","desc":"Update financial processes and reporting strategies for better transparency and regulatory compliance."},
      {"num":"09","title":"Project Management","desc":"Effectively manage projects from inception to completion, ensuring milestones are met on time and within budget."},
      {"num":"10","title":"Team Leadership","desc":"Lead teams to secure positive outcomes for organizations — fostering collaboration and accountability at every level."},
      {"num":"11","title":"Strategic Planning","desc":"Develop and implement strategic plans and reporting frameworks that drive long-term operational excellence."},
    ]
  },
  {
    "file": "information-technology.html",
    "title": "Hospital Information & Technology (IT)",
    "subtitle": "Fully Automated Digital Networking with High-Class Security Protocols",
    "nav_label": "Information Technology",
    "intro": "We provide full IT (Information & Technology) related Setup & Support with fully Automated Digital Networking Structure along with High Class Security Protocols & Standardized Topologies. Streamlined LAN wire management, Net-Rack Installation, Fiber Optic Facility, and ADSL Router prioritize efficient cabling, accessibility, high-speed transmission, and robust routing for healthcare networks.",
    "items": [
      {"num":"01","title":"Comprehensive Networking Infrastructure","desc":"LAN wire management, Net-Rack Installation, Fiber Optic Facility, and ADSL Router setup for high-speed, reliable connectivity."},
      {"num":"02","title":"Security Solutions","desc":"CCTV Camera Installation with strategic placement, NVR Installation, and access control for comprehensive security coverage."},
      {"num":"03","title":"Server and Cloud Services","desc":"POE, MC, Mapping Switch Installation and cloud infrastructure setup for robust, scalable hospital data management."},
      {"num":"04","title":"Communication & Intercom System","desc":"Intercom Matrix facilitates effective intercom communication across all hospital departments and wings."},
      {"num":"05","title":"Software Solutions","desc":"Comprehensive HIS and LIMS for healthcare, HR software for efficient management, TALLY ERP for secure accounting."},
      {"num":"06","title":"Host and Printing Solutions","desc":"Complete hosting infrastructure and networked printing solutions for seamless document management across the facility."},
      {"num":"07","title":"Digital Presence & Marketing","desc":"Crafting innovative software solutions and amplifying reach through strategic digital marketing for unparalleled success."},
      {"num":"08","title":"Design Services","desc":"Professional graphic design, UI/UX, and branding services to establish a strong visual identity for healthcare organizations."},
      {"num":"09","title":"Data Analysis for Business","desc":"Advanced analytics tools to extract actionable insights from hospital data for better operational and clinical decisions."},
      {"num":"10","title":"Network Monitoring & Cloud Services","desc":"Real-time network monitoring, proactive maintenance, and cloud services ensuring 24/7 uptime for critical systems."},
      {"num":"11","title":"Digital Marketing & Design Services","desc":"Strategic SEO, social media management, and creative design to boost your healthcare brand's online visibility."},
      {"num":"12","title":"Security Systems & Web Development","desc":"Integrated security infrastructure setup alongside custom web development for a secure digital presence."},
      {"num":"13","title":"Complete HMIS & LIS Software Service","desc":"Software related complete Hospital Management Information System (HMIS) and Laboratory Information System (LIS) service."},
    ]
  },
  {
    "file": "nabh-accreditation.html",
    "title": "NABH Accreditation",
    "subtitle": "Complete NABH Accreditation Support for Your Healthcare Facility",
    "nav_label": "NABH Accreditation",
    "intro": "We will assist you to promote your organization through a NABH Accreditation. We are ready to help you and your organization with Highly Experienced Management Staff, to put everything in the streamline of your Hospital OR Health Care Day to Day Operational Management systems as per NABH Guidelines.",
    "items": [
      {"num":"01","title":"Documentation Management","desc":"We keep a record of all the documentation of the hospital, in relation to accreditation — ensuring full compliance at all times."},
      {"num":"02","title":"Document Issuance","desc":"We issue various documents to departments from time to time as required by NABH accreditation standards."},
      {"num":"03","title":"Activity Delegation","desc":"Delegate the activities in departments and ensure timely completion in line with accreditation requirements."},
      {"num":"04","title":"Feedback Collection","desc":"Regularly receive feedbacks from departments regarding status of their work related to accreditation preparation."},
      {"num":"05","title":"Regular Assessment","desc":"Plan and execute regular assessment of the hospital in accordance with accreditation standards and timelines."},
      {"num":"06","title":"Quality Assurance Coordination","desc":"We coordinate all activities required for quality assurance and continuous monitoring of the hospital."},
      {"num":"07","title":"Clinical Studies & Trials","desc":"Conduct Clinical Studies and clinical trials as required by NABH accreditation protocols."},
      {"num":"08","title":"SOP Identification & Preparation","desc":"We are responsible for identification and preparation of SOPs which are missing in the system."},
      {"num":"09","title":"SOP Review & Archiving","desc":"Periodic review, distribution, maintenance, withdrawal and archiving of SOPs as per accreditation requirements."},
      {"num":"10","title":"Internal Audit Preparation","desc":"We prepare you for Internal Audit Policy for the QA department — building a culture of continuous improvement."},
      {"num":"11","title":"Staff Training","desc":"We do induction and train new employees and conduct ongoing training of SOPs for the existing staff."},
      {"num":"12","title":"Corrective Action Verification","desc":"Review and verification of corrective action of the cited observations from internal and external audits."},
      {"num":"13","title":"Strategic Planning","desc":"Undertaking various Projects, Strategic planning and policy development for long-term accreditation maintenance."},
    ]
  },
  {
    "file": "nabl-accreditation.html",
    "title": "NABL Accreditation",
    "subtitle": "Trusted NABL Accreditation Services for Your Pathology Lab",
    "nav_label": "NABL Accreditation",
    "intro": "We have trained and certified manpower, who will introduce and implement all systems and process flows, manage and maintain day to day operations as per guidelines of NABL, and complete the accreditation process for your Health Care Set up.",
    "items": [
      {"num":"01","title":"Quality Assurance","desc":"NABL accreditation ensures that the lab follows standardized procedures and uses calibrated equipment, ensuring accurate and reliable results for better diagnosis, treatment, and disease management."},
      {"num":"02","title":"Compliance with Regulatory Requirements","desc":"NABL accreditation is mandatory for all blood testing laboratories performing medical testing in India. An NABL accredited lab is compliant with all regulatory requirements, vital for patient safety."},
      {"num":"03","title":"Expertise and Experience","desc":"An NABL accredited lab has experienced and trained staff who are knowledgeable in their field. They follow strict protocols and guidelines, ensuring precise and accurate results every time."},
      {"num":"04","title":"Confidence and Trust","desc":"When a pathology lab is NABL accredited, it instils confidence and trust in patients and the medical community — assuring them that results provided are accurate and the lab is reliable."},
      {"num":"05","title":"Continuous Improvement","desc":"NABL accreditation is not a one-time process; it requires regular monitoring and evaluation of the lab's processes and procedures to continuously improve quality and stay current with technological advancements."},
    ]
  },
  {
    "file": "pathology-laboratory.html",
    "title": "Pathology Lab & Diagnostic Centre Set-up",
    "subtitle": "Unparalleled Excellence in Pathology Lab Setup & NABL Accreditation",
    "nav_label": "Pathology Laboratory",
    "intro": "Transform Your Pathology Lab — Unparalleled Excellence in Setup and NABL Accreditation Services Await You! We provide comprehensive pathology laboratory planning, design, and management support to establish world-class diagnostic facilities.",
    "items": [
      {"num":"01","title":"Laboratory Planning, Drawing & Designing","desc":"Pathology Laboratory Planning, Drawing, Designing and Interior — creating optimal workflow spaces for precision diagnostics."},
      {"num":"02","title":"Complete HR Support","desc":"Complete Experienced HR support with skilled laboratory professionals, technicians and management staff."},
      {"num":"03","title":"ISO 15189 Compliance","desc":"Maintaining ISO 15189 rules for NABL Audits — ensuring international standards for medical laboratories are consistently met."},
      {"num":"04","title":"ISO 9001 Compliance","desc":"Following ISO 9001 for ISO Audits — implementing quality management systems across all laboratory operations."},
      {"num":"05","title":"NABL Standards Management","desc":"Management and Technical aspects as per NABL Standards, ensuring every operational area meets accreditation requirements."},
      {"num":"06","title":"Data Management & Storage","desc":"Data Management and Storage as per NABL protocol — secure, organized, and easily retrievable laboratory data systems."},
      {"num":"07","title":"Management Responsibilities","desc":"Comprehensive management responsibilities covering planning, organizing, directing, and controlling laboratory operations."},
      {"num":"08","title":"Facility Management & Safety","desc":"Complete facility management and safety protocols to ensure a safe working environment and compliant laboratory setup."},
      {"num":"09","title":"Bar Code Process Development","desc":"Bar Code Process Development for sample tracking, reducing errors, and improving specimen identification accuracy."},
      {"num":"10","title":"Equipment Integration with Software","desc":"Seamless Equipment Integration with Laboratory Information Software for automated result capture and reporting."},
      {"num":"11","title":"Staff Training & Development","desc":"Training and Development of Staff — building a skilled, knowledgeable team capable of maintaining NABL standards."},
    ]
  },
  {
    "file": "hmis-lims.html",
    "title": "HMIS and LIMS Support",
    "subtitle": "Comprehensive Support for Health & Laboratory Information Management Systems",
    "nav_label": "HMIS & LIMS",
    "intro": "We provide comprehensive support for Health Management Information Systems (HMIS) and Laboratory Information Management Systems (LIMS), ensuring efficient data management, integration, and optimization for healthcare and research institutions.",
    "items": [
      {"num":"01","title":"Health Data Integration","desc":"Integrate health data across departments for informed clinical and administrative decisions, improving overall hospital efficiency."},
      {"num":"02","title":"User Training & Utilization","desc":"Train users for efficient utilization of HMIS and LIMS platforms to maximize the return on your technology investment."},
      {"num":"03","title":"Security & Privacy","desc":"Ensure robust security and privacy protocols for all patient and laboratory data, compliant with healthcare data standards."},
      {"num":"04","title":"Workflow Customization","desc":"Customize for optimized workflows and provide continuous technological updates to adapt to evolving healthcare needs."},
      {"num":"05","title":"Sample Tracking & Accountability","desc":"Track samples throughout the laboratory workflow for complete accountability and chain-of-custody documentation."},
      {"num":"06","title":"Quality Control","desc":"Enforce quality control protocols for reliable data — ensuring laboratory results meet the highest standards of accuracy."},
      {"num":"07","title":"System Interoperability","desc":"Ensure interoperability with lab instruments, hospital systems, and external reporting platforms for seamless data flow."},
      {"num":"08","title":"Scalable System Management","desc":"Train users for efficient workflows and customize and scale systems for evolving organizational needs and growth."},
    ]
  },
  {
    "file": "website-development.html",
    "title": "Website Development",
    "subtitle": "Responsive, User-Friendly Websites with Creative Design & Robust Coding",
    "nav_label": "Website Development",
    "intro": "Develop responsive, user-friendly websites with creative design, robust coding, and optimization for optimal performance, ensuring a compelling online presence for your healthcare organization.",
    "items": [
      {"num":"01","title":"User-Centric Design","desc":"Prioritize intuitive navigation and clear layouts to enhance user satisfaction and interaction across all devices."},
      {"num":"02","title":"Visually Appealing Interface","desc":"Employ visually appealing and brand-aligned design elements to capture and retain visitor attention effectively."},
      {"num":"03","title":"Clean, Standards-Compliant Code","desc":"Implement clean, efficient, and standards-compliant code for a stable, reliable and maintainable website foundation."},
      {"num":"04","title":"Performance Optimization","desc":"Enhance site speed and efficiency through optimization techniques, contributing to a positive user experience and better search engine rankings."},
      {"num":"05","title":"Brand Identity Development","desc":"Develop websites that reflect the brand identity, fostering a strong online presence and leaving a lasting impression on visitors."},
      {"num":"06","title":"Functional & Goal-Aligned","desc":"Ensure that website features and functionalities align with user needs, business goals, and industry standards."},
      {"num":"07","title":"End-to-End User Journey","desc":"Focus on the complete end-to-end user journey, refining interactions to create a smooth, enjoyable, and memorable online experience."},
    ]
  },
  {
    "file": "digital-marketing.html",
    "title": "Digital Branding & Marketing",
    "subtitle": "Optimize Online Presence, Engagement & Conversion for Business Growth",
    "nav_label": "Digital Marketing",
    "intro": "Strategize and implement digital branding and marketing campaigns, optimizing online presence, engagement, and conversion for business growth and success. We help healthcare organizations build a strong, trustworthy digital identity.",
    "items": [
      {"num":"01","title":"Digital Strategy Development","desc":"Develop and implement digital strategies aligned with brand goals for impactful, measurable online presence."},
      {"num":"02","title":"Target Audience Analysis","desc":"Analyze and tailor campaigns to resonate effectively with specific target audiences for increased engagement and conversion."},
      {"num":"03","title":"Brand Consistency","desc":"Maintain uniform brand messaging and visual identity across all digital channels to build trust and recognition."},
      {"num":"04","title":"Content Marketing","desc":"Develop and share relevant, engaging content to connect with and captivate the target audience across online platforms."},
      {"num":"05","title":"Social Media Management","desc":"Utilize social platforms strategically to expand brand reach, foster community, and drive meaningful engagement."},
      {"num":"06","title":"Search Engine Optimization","desc":"Optimize digital content for search engines, enhancing online visibility and improving search rankings for increased discoverability."},
      {"num":"07","title":"Analytics & Performance Tracking","desc":"Employ analytics tools to measure campaign performance, gather actionable insights, and refine marketing strategies."},
      {"num":"08","title":"Conversion Rate Optimization","desc":"Implement strategies to optimize website and campaign conversions, translating engagement into tangible business outcomes."},
    ]
  },
  {
    "file": "plant-setup.html",
    "title": "O2 Generator, RO, ETP & STP Plant Set-up",
    "subtitle": "Critical Healthcare Infrastructure for Sustainable Operations",
    "nav_label": "Plant Setup",
    "intro": "We specialize in establishing critical infrastructure for hospitals, including Oxygen Generators, Reverse Osmosis systems, Effluent Treatment Plants (ETP), and Sewage Treatment Plants (STP). Our tailored solutions ensure reliable and efficient supply of essential resources for your healthcare facility.",
    "items": [
      {"num":"01","title":"Comprehensive Planning","desc":"Develop comprehensive plans for Oxygen Generator, RO, ETP, and STP plant installations tailored to your facility's needs."},
      {"num":"02","title":"Advanced Technology Selection","desc":"Choose advanced technologies suitable for efficient oxygen generation, water purification, and wastewater treatment."},
      {"num":"03","title":"Customized Solutions","desc":"Tailor solutions to meet specific needs, optimizing each plant's functionality for maximum effectiveness and efficiency."},
      {"num":"04","title":"Regulatory Compliance","desc":"Ensure adherence to environmental regulations and safety standards throughout the entire plant setup process."},
      {"num":"05","title":"Quality Equipment Sourcing","desc":"Source and install high-quality machinery and components for reliable, long-lasting, and low-maintenance operation."},
      {"num":"06","title":"Sustainability Optimization","desc":"Optimize resource consumption to promote sustainability and minimize environmental impact in daily operations."},
      {"num":"07","title":"Testing & Commissioning","desc":"Conduct thorough testing and commissioning to guarantee the full functionality and performance of each plant system."},
      {"num":"08","title":"Operator Training","desc":"Provide comprehensive training for operators to ensure proper maintenance and smooth long-term operation of established systems."},
    ]
  },
]

# Navbar HTML (shared)
NAVBAR = '''<nav class="navbar" id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">
      <svg viewBox="0 0 38 38" fill="none">
        <circle cx="19" cy="19" r="18" fill="#E85D04" opacity=".1"/>
        <circle cx="19" cy="19" r="14" fill="#E85D04" opacity=".2"/>
        <rect x="16" y="10" width="6" height="18" rx="2" fill="#E85D04"/>
        <rect x="10" y="16" width="18" height="6" rx="2" fill="#E85D04"/>
        <circle cx="19" cy="19" r="3" fill="white"/>
      </svg>
      <div class="nav-logo-text">
        <span class="brand-top">The Team</span>
        <span class="brand-bottom">The Consultants</span>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="index.html#about">About</a></li>
      <li>
        <a href="index.html#services">Services <svg class="arr" viewBox="0 0 16 16"><polyline points="4,6 8,10 12,6"/></svg></a>
        <div class="dropdown">
          <a href="project-management.html">Hospital &amp; Healthcare Project Management</a>
          <a href="medical-college.html">Medical College Hospital Design &amp; Development</a>
          <a href="operation-management.html">Hospital &amp; Healthcare Operational Management</a>
          <a href="information-technology.html">Information &amp; Technology</a>
          <a href="nabh-accreditation.html">NABH Accreditation</a>
          <a href="nabl-accreditation.html">NABL Accreditation</a>
          <a href="pathology-laboratory.html">Pathology Lab &amp; Diagnostic Centre Set-up</a>
          <a href="hmis-lims.html">HMIS and LIMS Support</a>
          <a href="website-development.html">Website Development</a>
          <a href="digital-marketing.html">Digital Branding &amp; Marketing</a>
          <a href="plant-setup.html">Plant Setup (O2, RO, ETP, STP)</a>
        </div>
      </li>
      <li><a href="index.html#projects">Projects</a></li>
      <li><a href="index.html#contact">Contact Us</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">
      <svg viewBox="0 0 24 24" fill="none"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.7 10.74 19.79 19.79 0 01.67 2.18 2 2 0 012.67.06h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Get In Touch
    </a>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<div class="mob-menu" id="mobMenu">
  <a href="index.html">Home</a>
  <a href="index.html#about">About</a>
  <a href="index.html#services" style="font-weight:700;color:var(--orange)">Services</a>
  <a href="project-management.html" class="mob-sub">Hospital &amp; Healthcare Project Management</a>
  <a href="medical-college.html" class="mob-sub">Medical College Hospital Design &amp; Dev.</a>
  <a href="operation-management.html" class="mob-sub">Hospital &amp; Healthcare Operational Mgmt.</a>
  <a href="information-technology.html" class="mob-sub">Information &amp; Technology</a>
  <a href="nabh-accreditation.html" class="mob-sub">NABH Accreditation</a>
  <a href="nabl-accreditation.html" class="mob-sub">NABL Accreditation</a>
  <a href="pathology-laboratory.html" class="mob-sub">Pathology Lab &amp; Diagnostic Setup</a>
  <a href="hmis-lims.html" class="mob-sub">HMIS and LIMS Support</a>
  <a href="website-development.html" class="mob-sub">Website Development</a>
  <a href="digital-marketing.html" class="mob-sub">Digital Branding &amp; Marketing</a>
  <a href="plant-setup.html" class="mob-sub">Plant Setup (O2, RO, ETP, STP)</a>
  <a href="index.html#projects">Projects</a>
  <a href="index.html#contact">Contact Us</a>
  <a href="index.html#contact" class="mob-cta">Get In Touch</a>
</div>'''

# CTA + Footer (shared)
CTA_FOOTER = '''<section class="cta-banner">
  <div class="container">
    <div class="cta-inner">
      <div class="fade-up">
        <div class="cta-ecg">
          <svg viewBox="0 0 120 36" fill="none"><polyline points="0,18 20,18 26,6 32,30 38,10 44,26 50,18 70,18 76,8 82,28 88,14 94,22 100,18 120,18" stroke="rgba(255,255,255,.7)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h2 class="cta-title">Ready to Build Your<br>Healthcare Facility?</h2>
        <p class="cta-sub">Whenever and wherever you need — it\'s our job to get you started on the correct path for your imminent or existing Health Care Facility.</p>
      </div>
      <div class="cta-contacts fade-up">
        <div class="cta-ci">
          <div class="cta-ci-icon"><svg viewBox="0 0 24 24" fill="none"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.7 10.74 19.79 19.79 0 01.67 2.18 2 2 0 012.67.06h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <div><div class="cta-ci-lbl">Phone</div><div class="cta-ci-val">(+91)-9073409444</div></div>
        </div>
        <div class="cta-ci">
          <div class="cta-ci-icon"><svg viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="white" stroke-width="2"/><polyline points="22,6 12,13 2,6" stroke="white" stroke-width="2"/></svg></div>
          <div><div class="cta-ci-lbl">Email</div><div class="cta-ci-val">info@theteamtheconsultants.com</div></div>
        </div>
        <div class="cta-ci">
          <div class="cta-ci-icon"><svg viewBox="0 0 24 24" fill="none"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" stroke="white" stroke-width="2"/><circle cx="12" cy="10" r="3" stroke="white" stroke-width="2"/></svg></div>
          <div><div class="cta-ci-lbl">Address</div><div class="cta-ci-val">25, A.B. Sarani, Sevoke Road<br>Bhaktinagar, Siliguri – 734001</div></div>
        </div>
      </div>
      <div class="cta-btns fade-up">
        <a href="index.html#contact" class="btn-w">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          Book Free Consultation
        </a>
        <a href="https://wa.me/919073409444" target="_blank" class="btn-wa">
          <svg viewBox="0 0 24 24" fill="none"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" fill="currentColor"/></svg>
          Chat on WhatsApp
        </a>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand-logo">
          <svg viewBox="0 0 38 38" fill="none" width="36" height="36">
            <circle cx="19" cy="19" r="18" fill="#E85D04" opacity=".15"/>
            <rect x="16" y="10" width="6" height="18" rx="2" fill="#E85D04"/>
            <rect x="10" y="16" width="18" height="6" rx="2" fill="#E85D04"/>
            <circle cx="19" cy="19" r="3" fill="white"/>
          </svg>
          <div class="nav-logo-text">
            <span class="brand-top" style="color:white">The Team</span>
            <span class="brand-bottom">The Consultants</span>
          </div>
        </div>
        <p class="footer-desc">We revolutionize Health Care with end-to-end Medical College and Hospital Project Management, NABH/NABL-Compliant services, IT Support, and Digital Branding.</p>
        <div class="footer-socials">
          <a href="https://www.facebook.com/profile.php?id=61551811960790" class="fsoc" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="rgba(255,255,255,.7)"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          <a href="https://www.instagram.com/theteamtheconsultants2023" class="fsoc" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke-width="2.5"/></svg></a>
          <a href="https://www.youtube.com/channel/UCslUT6bCfwrLU4MLGH-Kanw" class="fsoc" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="rgba(255,255,255,.7)"><path d="M22.54 6.42a2.78 2.78 0 00-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 00-1.95 1.96A29 29 0 001 12a29 29 0 00.46 5.58A2.78 2.78 0 003.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 001.95-1.95A29 29 0 0023 12a29 29 0 00-.46-5.58z"/><polygon points="9.75,15.02 15.5,12 9.75,8.98" fill="white"/></svg></a>
          <a href="https://wa.me/919073409444" class="fsoc" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="rgba(255,255,255,.7)"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Services</div>
        <a href="project-management.html">Project Management</a>
        <a href="medical-college.html">Medical College Design</a>
        <a href="operation-management.html">Operational Management</a>
        <a href="nabh-accreditation.html">NABH Accreditation</a>
        <a href="nabl-accreditation.html">NABL Accreditation</a>
        <a href="pathology-laboratory.html">Pathology Lab Setup</a>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">More Services</div>
        <a href="hmis-lims.html">HMIS &amp; LIMS</a>
        <a href="information-technology.html">IT &amp; Technology</a>
        <a href="website-development.html">Website Development</a>
        <a href="digital-marketing.html">Digital Marketing</a>
        <a href="plant-setup.html">Plant Setup</a>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Contact</div>
        <a href="tel:+919073409444">(+91)-9073409444</a>
        <a href="tel:+918637522036">(+91)-863-752-2036</a>
        <a href="mailto:info@theteamtheconsultants.com">info@theteamtheconsultants.com</a>
        <a href="#">25, A.B. Sarani, Sevoke Road,<br>Near ITI Road, Bhaktinagar,<br>Siliguri – 734001</a>
      </div>
    </div>
  </div>
  <div class="footer-bar">
    <div class="container">
      <div class="footer-bar-inner">
        <p class="footer-copy">© 2024 The Team The Consultants. All Rights Reserved.</p>
        <div class="footer-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms &amp; Conditions</a>
        </div>
      </div>
    </div>
  </div>
</footer>
<button class="scroll-top" id="scrollTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5,12 12,5 19,12"/></svg>
</button>'''

JS = '''<script>
const nb=document.getElementById('navbar');
window.addEventListener('scroll',()=>nb.classList.toggle('scrolled',scrollY>20),{passive:true});
const hb=document.getElementById('hamburger'),mm=document.getElementById('mobMenu');
hb.addEventListener('click',()=>{
  const o=mm.classList.toggle('open');
  const sp=hb.querySelectorAll('span');
  sp[0].style.transform=o?'translateY(7px) rotate(45deg)':'';
  sp[1].style.opacity=o?'0':'';
  sp[2].style.transform=o?'translateY(-7px) rotate(-45deg)':'';
});
mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
  mm.classList.remove('open');
  hb.querySelectorAll('span').forEach(s=>{s.style.transform='';s.style.opacity='';});
}));
const st=document.getElementById('scrollTop');
window.addEventListener('scroll',()=>st.classList.toggle('visible',scrollY>400),{passive:true});
st.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
const io=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});
},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.fade-up').forEach((el,i)=>{
  el.style.transitionDelay=(i%8)*0.08+'s';
  io.observe(el);
});
setTimeout(()=>document.querySelectorAll('.sp-hero .fade-up').forEach((el,i)=>setTimeout(()=>el.classList.add('visible'),i*100)),60);
</script>'''

def build_items_html(items):
    cols = 2 if len(items) >= 8 else (2 if len(items) >= 5 else 1)
    html = f'<div class="sp-items-grid sp-grid-{cols}">'
    for item in items:
        html += f'''
      <div class="sp-item fade-up">
        <div class="sp-item-num">{item["num"]}</div>
        <div class="sp-item-body">
          <div class="sp-item-title">{item["title"]}</div>
          <div class="sp-item-desc">{item["desc"]}</div>
        </div>
      </div>'''
    html += '\n    </div>'
    return html

def build_page(svc):
    items_html = build_items_html(svc['items'])
    title_esc = svc['title'].replace('&', '&amp;')
    subtitle_esc = svc['subtitle'].replace('&', '&amp;')
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_esc} | The Team The Consultants</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;1,9..144,300;1,9..144,600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

{NAVBAR}

<!-- Service Hero -->
<section class="sp-hero">
  <div class="sp-hero-bg"></div>
  <div class="container sp-hero-inner">
    <div class="sp-breadcrumb fade-up">
      <a href="index.html">Home</a>
      <svg viewBox="0 0 16 16" fill="none"><polyline points="6,4 10,8 6,12" stroke="currentColor" stroke-width="1.5"/></svg>
      <a href="index.html#services">Services</a>
      <svg viewBox="0 0 16 16" fill="none"><polyline points="6,4 10,8 6,12" stroke="currentColor" stroke-width="1.5"/></svg>
      <span>{svc["nav_label"]}</span>
    </div>
    <h1 class="sp-hero-title fade-up">{svc["title"]}</h1>
    <p class="sp-hero-sub fade-up">{subtitle_esc}</p>
    <div class="sp-hero-actions fade-up">
      <a href="index.html#contact" class="btn-primary">
        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>
        Get a Consultation
      </a>
      <a href="index.html#services" class="btn-outline-light">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12,19 5,12 12,5"/></svg>
        All Services
      </a>
    </div>
  </div>
</section>

<!-- Service Detail -->
<section class="sp-detail">
  <div class="container">
    <div class="sp-intro fade-up">
      <p>{svc["intro"]}</p>
    </div>
    {items_html}
    <div class="sp-ready fade-up">
      <div class="sp-ready-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="28" height="28"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22,4 12,14.01 9,11.01"/></svg>
      </div>
      <div>
        <div class="sp-ready-title">Ready to Help You</div>
        <div class="sp-ready-body">We are ready to help you and your organization with Highly Experienced Management Staff, to put everything in the streamline of your Hospital OR Health Care Day to Day Operational Management systems as per NABH Guidelines.</div>
      </div>
      <a href="index.html#contact" class="btn-primary" style="flex-shrink:0">Contact Us</a>
    </div>
  </div>
</section>

{CTA_FOOTER}

{JS}
</body>
</html>'''

for svc in SERVICES:
    path = os.path.join(BASE, svc['file'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_page(svc))
    print(f"Created: {svc['file']}")

print("\\nAll service pages generated!")
