import { test, expect } from '@playwright/test';

const baseURL = 'http://localhost:3000';

test('homepage loads', async ({ page }) => {
  await page.goto(baseURL);
  await expect(page.locator('h1')).toHaveText('Task Manager');
});
