import { describe, it, expect } from 'vitest';
import { describeAuthError, CloudAuthError } from './cloud';

describe('describeAuthError', () => {
  it('maps invalid credentials to an actionable wrong-password message', () => {
    const { code, message } = describeAuthError({ code: 'invalid_credentials', message: 'Invalid login credentials' });
    expect(code).toBe('invalid_credentials');
    expect(message).toContain("password isn't right");
    expect(message).toContain('Forgot password?');
  });

  it('maps unconfirmed email to a confirm-first message', () => {
    const { code, message } = describeAuthError({ error_code: 'email_not_confirmed' });
    expect(code).toBe('email_not_confirmed');
    expect(message).toContain("isn't confirmed");
  });

  it('maps existing account to an already-exists message', () => {
    const { code, message } = describeAuthError({ code: 'user_already_exists', message: 'User already registered' });
    expect(code).toBe('user_already_exists');
    expect(message).toContain('already exists');
  });

  it('maps email rate limiting to a wait message', () => {
    const { code, message } = describeAuthError({ code: 'over_email_send_rate_limit', message: 'email rate limit exceeded' });
    expect(code).toBe('rate_limited');
    expect(message).toContain('Wait a few minutes');
  });

  it('maps weak passwords to a length hint', () => {
    const { code, message } = describeAuthError({ code: 'weak_password' });
    expect(code).toBe('weak_password');
    expect(message).toContain('6 characters');
  });

  it('falls back to a generic message for unknown errors', () => {
    const { code, message } = describeAuthError({ code: 'something_weird' });
    expect(message).toBe('Something went wrong. Please try again.');
    expect(code).toBe('something_weird');
  });

  it('CloudAuthError carries code and user-facing message', () => {
    const err = new CloudAuthError('invalid_credentials', 'Wrong password.');
    expect(err.code).toBe('invalid_credentials');
    expect(err.userMessage).toBe('Wrong password.');
    expect(err.message).toBe('Wrong password.');
  });
});
