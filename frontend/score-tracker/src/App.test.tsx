import { describe, it, expect } from 'vitest';
import { screen, render } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { userEvent } from '@testing-library/user-event';
import App from './App.tsx';

describe('App', () => {
  it('renders without error', () => {
    render(<App />, { wrapper: Router });
  });
  it('navigates to correct pages', async () => {
    render(<App />, { wrapper: Router });
    expect(screen.getByRole('heading', { name: /call of duty score tracker landing page/i })).toBeInTheDocument();
    // should navigate to demo page
    await userEvent.click(screen.getByRole('button', { name: /view demo/i }));
    expect(screen.getByRole('heading', { name: /call of duty score tracker/i })).toBeInTheDocument();
  });
});