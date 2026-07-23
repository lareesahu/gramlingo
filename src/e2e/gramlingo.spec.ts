import { test, expect, type Page } from '@playwright/test';

async function openFresh(page: Page, width: number, height: number) {
  await page.setViewportSize({ width, height });
  await page.goto('/gramlingo/', { waitUntil: 'domcontentloaded', timeout: 15000 });
  await page.evaluate(() => localStorage.clear());
  await page.reload();
  await expect(page.locator('.welcome-screen')).toBeVisible({ timeout: 8000 });
}

async function createPlayer(page: Page, name: string) {
  await page.getByRole('button', { name: 'New Player' }).click();
  await page.getByPlaceholder('Username').fill(name);
  await page.getByRole('button', { name: 'Start Learning' }).click();
  await expect(page.locator('.lp__card')).toHaveCount(12);
}

test('fresh mobile visitor sees content and completes a real answer loop', async ({ page }) => {
  const errors: string[] = [];
  page.on('console', message => {
    if (message.type() === 'error') errors.push(message.text());
  });
  page.on('pageerror', error => errors.push(error.message));

  await openFresh(page, 390, 844);
  await expect(page.getByText('Grammar Quest — Learn by playing')).toBeVisible();
  await createPlayer(page, 'MobileQA');

  const bodyOverflow = await page.evaluate(() => document.body.scrollWidth - innerWidth);
  expect(bodyOverflow).toBeLessThanOrEqual(1);

  await page.getByRole('button', { name: /Relative Clauses: Lesson plan/ }).click();
  await expect(page.locator('.lp__phase')).toHaveCount(8);
  await page.getByRole('button', { name: /Identify Relative Clauses/ }).click();

  await expect(page.getByText(/Which part of this sentence is the relative clause/)).toBeVisible();
  await page.locator('.option-btn').nth(0).click();
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.getByText(/antecedent/)).toBeVisible();

  await page.locator('.option-btn').nth(1).click();
  await expect(page.getByText(/Correct.*relative clause/)).toBeVisible();

  await page.getByRole('button', { name: 'Back' }).click();
  await expect(page.locator('.lp__panel')).toBeVisible();
  await expect(page.locator('.module-screen')).toHaveCount(0);
  expect(errors).toEqual([]);
});

test('tablet can inspect all module plans without entering an empty lesson', async ({ page }) => {
  await openFresh(page, 768, 1024);
  await createPlayer(page, 'TabletQA');

  await page.getByRole('button', { name: /Verb Tenses: Lesson plan/ }).click();
  await expect(page.locator('.lp__phase')).toHaveCount(8);
  await expect(page.locator('.lp__phase:disabled')).toHaveCount(8);
  await expect(page.locator('.lp__phase-status').first()).toHaveText('Coming soon');
  await expect(page.locator('.lesson-screen')).toHaveCount(0);

  const bodyOverflow = await page.evaluate(() => document.body.scrollWidth - innerWidth);
  expect(bodyOverflow).toBeLessThanOrEqual(1);
});

test('desktop renders every latest cover and supports horizontal navigation', async ({ page }) => {
  await openFresh(page, 1440, 900);
  await createPlayer(page, 'DesktopQA');

  const grid = page.locator('.lp__grid');
  const before = await grid.evaluate(element => element.scrollLeft);
  await page.getByRole('button', { name: 'Next modules' }).click();
  await expect.poll(() => grid.evaluate(element => element.scrollLeft)).toBeGreaterThan(before);

  const cards = page.locator('.lp__card');
  for (let index = 0; index < await cards.count(); index += 1) {
    const image = cards.nth(index).locator('img');
    await image.scrollIntoViewIfNeeded();
    await expect(image).toBeVisible();
    expect(await image.evaluate(element => (element as HTMLImageElement).naturalWidth)).toBeGreaterThan(0);
  }

});
