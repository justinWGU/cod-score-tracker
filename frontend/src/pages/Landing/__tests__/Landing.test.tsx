import { render, screen } from '@testing-library/react';
import Landing from '../Landing';
import { describe, it, expect } from 'vitest';
import { Route, MemoryRouter as Router, Routes } from 'react-router-dom';
import userEvent from '@testing-library/user-event';
import ScoreBoard from '../../ScoreBoard/ScoreBoard';

describe('Landing', () => {
  it('renders without error', () => {
    render(<Router><Landing /></Router>);
    const title = screen.getByRole('heading', { name: /call of duty score tracker landing page/i });
    expect(title).toBeInTheDocument();
  });
  it('navigates to demo page when "View Demo" button is clicked', async () => { 
    render(
      <Router initialEntries={['/']}>
        <Routes>
          <Route path={'/'} element={<Landing />} />
          <Route path={'/scoreboard'} element={<ScoreBoard />} />;   
        </Routes>
      </Router>
    );
    const btn = screen.getByRole('button', { name: 'View Demo' });
    await userEvent.click(btn);
    const header = screen.getByRole('heading', { name: /call of duty score tracker/i });
    expect(header).toBeInTheDocument();
  });
  it('has the url value to project repo on Github button', () => {
    render(<Router><Landing /></Router>);
    const lnk = screen.getByRole('link', { name: /github/i });
    userEvent.click(lnk);
    expect(lnk).toHaveAttribute('href', 'https://github.com/justinWGU/cod-score-tracker');
  });
  it('has the correct href value to the project\'s email on "Contact" button', () => {
    render(<Router><Landing /></Router>);
    expect(screen.getByRole('link', { name: /contact/i })).toHaveAttribute('href', 'mailto:codscoretracker@gmail.com');
  });
  it('navigates to #get-involved section of page when "Get Involved" link is clicked', () => {
    render(<Router><Landing /></Router>);
    const lnk = screen.getByRole('link', { name: /get involved/i});
    expect(lnk).toHaveAttribute('href', '#get-involved');
  }) 
});