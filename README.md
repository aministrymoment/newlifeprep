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

## Student portal (Supabase)
Address: /portal (sign in at /portal/login). Project URL and public anon key are set in netlify.toml.

One time database setup:
1. Supabase, SQL Editor, New query. Paste all of supabase/schema.sql and click Run.
2. Authentication, Users, Add user: create your own login (check Auto Confirm User).
3. Make yourself an administrator. In the SQL Editor run (use your email):

        update public.profiles set role = 'admin' where email = 'YOUR EMAIL';

4. Authentication, Sign In / Providers: turn OFF "Allow new users to sign up" so only the office can create students.
5. Authentication, URL Configuration: set Site URL to your live address (later https://www.newlifeprep.org).

Adding a student: Authentication, Users, Add user. Then sign in as admin, open /portal/admin, set the name and Student ID (NLPA-20XX-XXX) and enroll the student in courses.

Study help panel: add ANTHROPIC_API_KEY in Netlify environment variables. Optional: ANTHROPIC_MODEL.

Courses: each course has a Focus, Topics, Assessments, Discussions and Quizzes. Quiz answers are stored in the admin only table quiz_keys and quizzes are graded in the database (grade_quiz), 70 percent to pass, unlimited retakes.
