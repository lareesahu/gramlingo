create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text not null,
  created_at timestamptz not null default now()
);

create table public.progress_state (
  user_id uuid primary key references public.profiles(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.profiles enable row level security;
alter table public.progress_state enable row level security;

create policy "Learners can create their own profile"
on public.profiles for insert to authenticated
with check ((select auth.uid()) = id);

create policy "Learners can read their own profile"
on public.profiles for select to authenticated
using (
  (select auth.uid()) = id
  or (select auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
);

create policy "Learners can create their own progress"
on public.progress_state for insert to authenticated
with check ((select auth.uid()) = user_id);

create policy "Learners and admins can read permitted progress"
on public.progress_state for select to authenticated
using (
  (select auth.uid()) = user_id
  or (select auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
);

create policy "Learners can update their own progress"
on public.progress_state for update to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create index progress_state_updated_at_idx on public.progress_state(updated_at desc);
