---
name: Obsidian Engineer
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#b9c7df'
  on-secondary: '#233144'
  secondary-container: '#3c4a5e'
  on-secondary-container: '#abb9d1'
  tertiary: '#ffb783'
  on-tertiary: '#4f2500'
  tertiary-container: '#d97721'
  on-tertiary-container: '#452000'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#ffdcc5'
  tertiary-fixed-dim: '#ffb783'
  on-tertiary-fixed: '#301400'
  on-tertiary-fixed-variant: '#703700'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
  slate-surface: '#1E1E1E'
  slate-elevated: '#2D2D2D'
  indigo-mute: '#312E81'
  glass-border: rgba(255, 255, 255, 0.1)
typography:
  headline-xl:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  headline-xl-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  section-gap-lg: 120px
  section-gap-sm: 64px
---

## Brand & Style

The design system is engineered to project a persona of technical mastery, precision, and architectural depth. It targets a high-end professional audience—recruiters, technical leads, and founders—who value clarity and structural integrity in software development.

The visual direction is a fusion of **Minimalism** and **Glassmorphism**. By using a "Dark Slate" foundation, we create a low-eye-strain environment that allows code snippets and project visuals to emerge with high contrast. Depth is not communicated through heavy drop shadows, but through semi-transparent layers, backdrop blurs (glassmorphism), and subtle tonal shifts between surface tiers. The result is a premium, "IDE-inspired" aesthetic that feels both futuristic and grounded.

## Colors

The palette is anchored in a monochromatic spectrum of "Dark Slate" to ensure a sophisticated, tech-focused atmosphere. 

- **Foundational Neutrals:** The base background is a deep charcoal (#121212), providing a void-like canvas that eliminates visual noise. Surface containers use Dark Slate (#1E1E1E) to distinguish interactive areas.
- **Accents & Gradients:** A soft Indigo primary color is used sparingly for highlights, active states, and call-to-action elements.
- **Gradients:** Use linear gradients from `indigo-mute` to `secondary_color_hex` at a 135-degree angle to provide a sense of depth in hero sections or featured project cards.
- **Translucency:** For glassmorphic effects, use white with 5-10% opacity for backgrounds and 15% opacity for borders to simulate light catching on glass edges.

## Typography

This design system utilizes a three-font strategy to balance professional impact with technical utility.

- **Headlines:** Hanken Grotesk provides a sharp, contemporary feel with high geometric precision. Use `headline-xl` for hero statements and `headline-md` for section headers.
- **Body:** Inter is the workhorse for long-form content, project descriptions, and experience bullet points, ensuring maximum readability in dark mode.
- **Technical/Labels:** JetBrains Mono is utilized for tags, metadata, and code-related labels, reinforcing the software engineering identity.

Always use a higher line-height (1.6) for body text in dark mode to prevent "character bleeding" and improve scanability.

## Layout & Spacing

The system follows a 12-column fluid grid for desktop, transitioning to a 4-column grid for mobile. 

- **Rhythm:** A base 8px spacing unit dictates all padding and margins.
- **Layout Model:** High-intent whitespace is used to separate major sections (`section-gap-lg`). Content is centered within a maximum width of 1200px to maintain focus.
- **Density:** Maintain a relaxed density for marketing-style sections (Hero, About) and a medium density for information-heavy sections (Experience, Skills).
- **Responsive:** On mobile, side margins should be a minimum of 20px, and vertical section gaps should scale down to `section-gap-sm`.

## Elevation & Depth

Hierarchy is established through a **Tonal Layering** system combined with **Glassmorphism**:

1.  **Level 0 (Base):** `#121212` — The main page background.
2.  **Level 1 (Card/Surface):** `#1E1E1E` — Used for standard content containers.
3.  **Level 2 (Hover/Active):** `#2D2D2D` — Used for interactive surfaces or to indicate a lift from the base.
4.  **Glass Layer:** Use a background blur of `12px` and a semi-transparent fill (`rgba(255, 255, 255, 0.05)`) for fixed navigation bars and floating overlays.

Shadows should be "Ambient" and highly diffused: `0px 20px 40px rgba(0, 0, 0, 0.4)`. Avoid harsh, high-opacity shadows which conflict with the dark slate theme.

## Shapes

The design system uses a "Rounded" (0.5rem) shape language to soften the industrial feel of the slate colors.

- **Standard Elements:** Buttons, cards, and input fields utilize a 0.5rem (8px) radius.
- **Large Containers:** Hero images or featured sections use 1rem (16px) for a more pronounced "premium" look.
- **Interactive Indicators:** Small elements like skill tags or status indicators should use the 0.5rem radius rather than being fully pill-shaped to maintain a structured, architectural aesthetic.

## Components

- **Buttons:** Primary buttons use the Indigo gradient background with white text. Secondary buttons use a `glass-border` with no fill, providing a "ghost" effect that relies on backdrop blur.
- **Cards:** Project cards feature a `slate-surface` background and a subtle `glass-border`. Upon hover, the card should scale slightly (1.02x) and increase its backdrop blur.
- **Chips/Tags:** Use the `label_font` (JetBrains Mono). Backgrounds should be a muted `secondary_color_hex` at 20% opacity with a solid border of the same color.
- **Input Fields:** Darker than the surface (`#121212`) with a focus state that highlights the border in Indigo.
- **Lists:** Career experience lists should use vertical lines (1px width, `#2D2D2D`) to connect chronological nodes, creating a "git-branch" visual metaphor.
- **Glass Overlays:** Modals and Navbars must implement `backdrop-filter: blur(12px)` to maintain context of the content beneath them while ensuring legibility.