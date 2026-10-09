# New Life Preparatory Academy Website

Next.js site for www.newlifeprep.org. Brand: Navy #0D1F3C, Gold #C9A84C. Motto: Excellence · Faith · Purpose.

## Start of every session
    git pull

## End of every session (always deploy)
    git add .
    git commit -m "Describe what changed"
    git push

## Run locally
    npm install
    npm run dev

## Netlify settings
Build command: npm run build. Netlify detects Next.js automatically (netlify.toml included).
Environment variables (Site configuration, Environment variables):
- STRIPE_SECRET_KEY: your Stripe secret key (payments go to New Life Apostolic Church of Jesus, Inc.)
- RESEND_API_KEY: your Resend key for the contact form
- INQUIRY_TO: where inquiries are sent (default newlifeprep@gmail.com)
- INQUIRY_FROM: a verified sender such as NLPA Website <info@newlifeprep.org>
- SITE_URL: https://www.newlifeprep.org

Until the keys are added the forms show a message asking visitors to call or email.

## Where to edit
- Page text: src/content/*.html
- Name, phone, email, ministry line, EIN switch: src/site.ts
- Payment items and amounts: src/lib/catalog.ts
- Colors and layout: src/styles/
