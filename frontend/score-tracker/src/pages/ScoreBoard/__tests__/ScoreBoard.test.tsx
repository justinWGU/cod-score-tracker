import { render } from '@testing-library/react';
import ScoreBoard from '../ScoreBoard';
import { test } from 'vitest';


// smoke test
test('renders ScoreBoard without crashing', () => {
  render(<ScoreBoard />);
});

// on api error, updates state and renders err message

// on api success, does not update state and renders normally

