# GramLingo cloud setup

1. Create a Supabase project and apply `migrations/20260803150000_cloud_progress.sql`.
2. Copy `.env.example` to `.env.local` and add the project URL and publishable key.
3. Create the admin account through GramLingo, then set its trusted app metadata in the Supabase SQL editor:

```sql
update auth.users
set raw_app_meta_data = coalesce(raw_app_meta_data, '{}'::jsonb) || '{"role":"admin"}'::jsonb
where email = 'ADMIN_EMAIL';
```

Sign out and back in after granting the role. Never put a secret or service-role key in the browser environment.
