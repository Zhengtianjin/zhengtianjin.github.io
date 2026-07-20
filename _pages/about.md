---
layout: default
title: about
permalink: /
subtitle: Active Perception · Event-based Vision · Embodied Intelligence

profile:
  image: pic.png

selected_papers: false
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<link rel="stylesheet" href="{{ '/assets/css/robotics-home.css' | relative_url | bust_file_cache }}">

<main class="robotics-home">
  <section class="robotics-hero" aria-labelledby="home-title">
    <div class="robotics-hero__copy">
      <div class="robotics-eyebrow">
        <span class="robotics-status-dot" aria-hidden="true"></span>
        Johns Hopkins University · Robotics
      </div>

      <h1 id="home-title" class="robotics-title">
        {{ site.first_name }}
        {{ site.middle_name }}
        {{ site.last_name }}
      </h1>

      <p class="robotics-subtitle">{{ page.subtitle }}</p>

      <p class="robotics-lead">Building robots that actively perceive, reason about, and interact with the physical world.</p>

      <div class="robotics-actions" aria-label="Homepage links">
        <a class="robotics-button robotics-button--primary" href="#research">Explore research</a>
        <a class="robotics-button" href="https://github.com/Zhengtianjin" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
      </div>

      {% if page.social %}
        <div class="robotics-social" aria-label="Social links">{% social_links %}</div>
      {% endif %}
    </div>

    {% if page.profile and page.profile.image %}
      <aside class="robotics-profile" aria-label="Profile">
        <div class="robotics-profile__frame">
          {% assign profile_image_path = page.profile.image | prepend: 'assets/img/' %}
          {% capture sizes %}(min-width: 900px) 360px, 82vw{% endcapture %}
          {%
            include figure.liquid
            loading="eager"
            path=profile_image_path
            class="robotics-profile__image"
            sizes=sizes
            alt="Portrait of Ziyue Darcy Zheng"
            cache_bust=true
          %}
          <span class="robotics-corner robotics-corner--tl" aria-hidden="true"></span>
          <span class="robotics-corner robotics-corner--br" aria-hidden="true"></span>
        </div>

        <div class="robotics-profile__meta">
          <span>JHU · Baltimore, MD</span>
          <span class="robotics-profile__availability">Researching now</span>
        </div>
      </aside>
    {% endif %}

  </section>

  <div class="robotics-content">

<section class="robotics-intro" aria-labelledby="about-heading">
  <div class="robotics-intro__label" id="about-heading">01 / About</div>
  <p class="robotics-intro__body">
    I am a Master's student at <strong>Johns Hopkins University</strong> studying how robots can sense deliberately, build useful world models, and turn perception into action.
  </p>
</section>

<section class="robotics-section" id="research" aria-labelledby="research-heading">
  <div class="robotics-section__head">
    <div>
      <p class="robotics-kicker">02 / Research focus</p>
      <h2 id="research-heading">Perception that moves.</h2>
    </div>
    <p class="robotics-section__note">
      My work sits at the intersection of sensing, planning, and learning for robots operating beyond the lab bench.
    </p>
  </div>

  <div class="robotics-grid">
    <article class="robotics-card">
      <span class="robotics-card__index">R-01</span>
      <h3>Active Perception</h3>
      <p>Information-efficient sensing, autonomous exploration, and 3D scene understanding for mobile robots.</p>
      <span class="robotics-card__tags">Planning · Reconstruction</span>
    </article>

    <article class="robotics-card">
      <span class="robotics-card__index">R-02</span>
      <h3>Event-based Vision</h3>
      <p>High-speed asynchronous sensing and uncertainty-aware perception for dynamic environments.</p>
      <span class="robotics-card__tags">Events · Efficient sensing</span>
    </article>

    <article class="robotics-card">
      <span class="robotics-card__index">R-03</span>
      <h3>Embodied Intelligence</h3>
      <p>Learning-based perception and control that connects intelligent models with physical robot behavior.</p>
      <span class="robotics-card__tags">Learning · Deployment</span>
    </article>

  </div>

  <div class="robotics-signal">
    <div class="robotics-signal__label">Current signal / work in progress</div>
    <p>I am currently exploring information-aware mobile sensing and reliable 3D scene understanding. Project details will be shared after the work is ready for release.</p>
  </div>
</section>

<section class="robotics-section" aria-labelledby="platforms-heading">
  <div class="robotics-section__head">
    <div>
      <p class="robotics-kicker">03 / Platforms</p>
      <h2 id="platforms-heading">From simulation to hardware.</h2>
    </div>
    <p class="robotics-section__note">Real systems keep the research honest: sensing, planning, control, and deployment all have to work together.</p>
  </div>

  <div class="robotics-platforms">
    <article class="robotics-platform">
      <span class="robotics-platform__type">Quadruped / Mobile</span>
      <h3>Unitree Go2</h3>
      <p>Active sensing and autonomous exploration.</p>
    </article>
    <article class="robotics-platform">
      <span class="robotics-platform__type">Manipulator / 7-DoF</span>
      <h3>Franka Research 3</h3>
      <p>Manipulation, control, and active sensing.</p>
    </article>
    <article class="robotics-platform">
      <span class="robotics-platform__type">Low-cost / Bimanual</span>
      <h3>SO-101</h3>
      <p>Imitation learning and embodied AI experiments.</p>
    </article>
  </div>

  <div class="robotics-closing">
    <p>Previously, I have worked on optimal control and path planning. I am always interested in thoughtful collaborations across robotics, perception, and intelligent systems.</p>
    <a class="robotics-button" href="https://github.com/Zhengtianjin" target="_blank" rel="noopener noreferrer">See my work on GitHub ↗</a>
  </div>
</section>

  </div>
</main>
