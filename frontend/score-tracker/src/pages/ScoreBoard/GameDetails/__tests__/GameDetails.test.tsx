import { render, screen } from '@testing-library/react';
import GameDetails from '../GameDetails';
import { expect, test } from 'vitest';

test('renders without error', () => {
  render(<GameDetails winsLeft={50} winsRight={19} mode='Search and Destroy'/>);

  const winsLeft = screen.getByText('50');
  const winsRight = screen.getByText('19');
  const mode = screen.getByText('Search and Destroy');

  expect(winsLeft).toBeInTheDocument();
  expect(winsRight).toBeInTheDocument();
  expect(mode).toBeInTheDocument();
});