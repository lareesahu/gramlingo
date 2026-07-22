import { test, expect } from '@playwright/test';

test.describe('Gramlingo E2E — Login Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();
  });

  test('shows loading screen then welcome page', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    await expect(page.locator('.welcome-screen')).toBeVisible({ timeout: 8000 });
    await expect(page.locator('.welcome-title')).toHaveText('GramLingo');
  });

  test('can create a new player', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    await expect(page.locator('.welcome-screen')).toBeVisible({ timeout: 8000 });

    await page.getByText('New Player').click();
    await page.locator('input').first().fill('testplayer');
    await page.getByText('Start Learning').click();

    await expect(page.getByText('Learning Path')).toBeVisible({ timeout: 5000 });
    await expect(page.locator('.module-overview-card').first()).toBeVisible();
  });
});

test.describe('Gramlingo E2E — Language Switch', () => {
  test('switches to Chinese and back', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    await expect(page.locator('.welcome-screen')).toBeVisible({ timeout: 8000 });
    await page.getByText('New Player').click();
    await page.locator('input').first().fill('lingotest');
    await page.getByText('Start Learning').click();
    await expect(page.getByText('Learning Path')).toBeVisible({ timeout: 5000 });

    await page.locator('.user-menu').click();
    await page.getByText('中文').click();
    await expect(page.getByText('学习路径')).toBeVisible();

    await page.locator('.user-menu').click();
    await page.getByText('English').click();
    await expect(page.getByText('Learning Path')).toBeVisible();
  });
});

test.describe('Gramlingo E2E — Module Navigation', () => {
  test('opens a module and sees phase list', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => localStorage.clear());
    await page.reload();

    await expect(page.locator('.welcome-screen')).toBeVisible({ timeout: 8000 });
    await page.getByText('New Player').click();
    await page.locator('input').first().fill('explorer');
    await page.getByText('Start Learning').click();
    await expect(page.getByText('Learning Path')).toBeVisible({ timeout: 5000 });

    await page.locator('.module-overview-card').first().click();
    await expect(page.locator('.ms-phase-list')).toBeVisible({ timeout: 5000 });
    await expect(page.getByText('Start').first()).toBeVisible();
  });
});
