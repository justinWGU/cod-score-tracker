import { render } from '@testing-library/react';
import GameDetails from '../GameDetails';
import { test } from 'vitest';

test('renders without error', () => {
  render(<GameDetails winsLeft={0} winsRight={1} mode='Search and Destroy'/>);
});