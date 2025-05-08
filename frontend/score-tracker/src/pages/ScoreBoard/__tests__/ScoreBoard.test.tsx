import { render } from '@testing-library/react';
import ScoreBoard from '../ScoreBoard';
import { test } from 'vitest';


// smoke test
test('renders ScoreBoard without crashing', () => {
  render(<ScoreBoard />);
});

