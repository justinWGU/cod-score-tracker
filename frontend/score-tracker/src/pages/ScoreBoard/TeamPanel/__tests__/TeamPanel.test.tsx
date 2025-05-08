import { render } from '@testing-library/react';
import TeamPanel from '../TeamPanel';
import { test } from 'vitest';

test('renders without error', () => {
  render(<TeamPanel team='Optic Gaming' score={200}/>);
});